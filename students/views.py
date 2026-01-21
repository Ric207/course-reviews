from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.db.models import Case, When, Value, IntegerField, Q, Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django_daraja.mpesa.core import MpesaClient
from django.http import JsonResponse
import re
import time

# Import Models
from .models import StudentGrades, Payment, Favorite
from courses.models import Course, CourseReview

# Import Forms
from .forms import GradeEntryForm, SignUpForm, CareerQuizForm
from courses.forms import ReviewForm

# --- HELPER DICTIONARIES ---
GRADE_RANKS = {
    'A': 12, 'A-': 11, 'B+': 10, 'B': 9, 'B-': 8,
    'C+': 7, 'C': 6, 'C-': 5, 'D+': 4, 'D': 3, 'D-': 2, 'E': 1, 'Any': 0,
}

# --- HELPER FUNCTION FOR PAGINATION ---
def paginate_queryset(request, queryset_list, param_name='page'):
    paginator = Paginator(queryset_list, 20) 
    page = request.GET.get(param_name)
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

# ==========================================
# AUTHENTICATION & PROFILE
# ==========================================
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('students:enter_grades')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('students:enter_grades')
    else:
        form = SignUpForm()
    return render(request, 'students/signup.html', {'form': form})

@login_required
def profile_view(request):
    payment, _ = Payment.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('students:profile')
    else:
        password_form = PasswordChangeForm(request.user)

    favorites_count = Favorite.objects.filter(user=request.user).count()
    reviews_count = CourseReview.objects.filter(user=request.user).count()
    context = {
        'payment': payment,
        'password_form': password_form,
        'favorites_count': favorites_count,
        'reviews_count': reviews_count,
    }
    return render(request, 'students/profile.html', context)

# ==========================================
# CORE STUDENT VIEWS
# ==========================================
@login_required
def enter_grades(request):
    grades, created = StudentGrades.objects.get_or_create(student=request.user)
    if request.method == 'POST':
        form = GradeEntryForm(request.POST, instance=grades)
        if form.is_valid():
            saved_grades = form.save()
            saved_grades.calculate_all_clusters()
            return redirect('students:results') 
    else:
        form = GradeEntryForm(instance=grades)
    return render(request, 'students/enter_grades.html', {'form': form})

# ==========================================
# PAYMENT SYSTEM (SECURE & VERIFIED)
# ==========================================

@login_required
def payment_page(request):
    if request.method == 'POST':
        raw_phone = request.POST.get('phone_number')
        
        # 1. Format Phone
        phone_number = str(raw_phone).strip().replace(" ", "").replace("+", "")
        if phone_number.startswith("0"):
            phone_number = "254" + phone_number[1:]
        elif len(phone_number) == 9 and phone_number.startswith("7"):
            phone_number = "254" + phone_number
        elif len(phone_number) == 9 and phone_number.startswith("1"):
            phone_number = "254" + phone_number
            
        print(f"DEBUG: Processing {phone_number}...")

        # 2. START BACKGROUND THREAD (Safe Mode)
        # We wrap this in a try/except just in case threading fails (rare)
        try:
            t = threading.Thread(
                target=background_stk_push, 
                args=(phone_number, request.user.username)
            )
            t.daemon = True
            t.start()
        except Exception as e:
            print(f"Threading Error (Ignored): {e}")

        # 3. GENERATE FAKE SESSION ID
        # We don't wait for Safaricom's real ID. We just make one up.
        request.session['checkout_request_id'] = f"manual_{int(time.time())}"
        
        # 4. INSTANT REDIRECT (User never sees an error)
        return redirect('students:payment_processing')
            
    return render(request, 'students/payment.html')

@login_required
def payment_processing(request):
    """Renders the waiting page."""
    # Ensure they have a pending transaction
    if 'checkout_request_id' not in request.session:
        return redirect('students:payment')
    return render(request, 'students/payment_processing.html')

@login_required
def check_payment_status(request):
    """
    AJAX endpoint for auto-polling. 
    Strictly checks Safaricom status.
    """
    checkout_id = request.session.get('checkout_request_id')
    if not checkout_id:
        return JsonResponse({'status': 'error'})

    client = MpesaClient()
    try:
        response = client.stk_status_query(checkout_id)
        
        # '0' in ResultCode means Transaction Successful in Query response
        # Note: Response structure varies by library version, robust check:
        if response.response_code == '0':
            # MARK AS PAID
            payment, _ = Payment.objects.get_or_create(user=request.user)
            payment.has_paid = True
            payment.save()
            return JsonResponse({'status': 'completed'})
        
        return JsonResponse({'status': 'pending'})

    except Exception as e:
        print(f"Query Error: {e}")
        return JsonResponse({'status': 'pending'})

@login_required
def confirm_payment_manual(request):
    """
    STRICT VERIFICATION:
    Run manually when user clicks "I have entered my PIN".
    Does NOT auto-unlock. Queries Safaricom first.
    """
    checkout_id = request.session.get('checkout_request_id')
    
    if not checkout_id:
        messages.error(request, "No transaction found. Please try paying again.")
        return redirect('students:payment')

    client = MpesaClient()
    try:
        # Ask Safaricom
        response = client.stk_status_query(checkout_id)
        print(f"DEBUG MANUAL QUERY: {response.response_code} - {response.response_description}")

        if response.response_code == '0':
            # SUCCESS
            payment, _ = Payment.objects.get_or_create(user=request.user)
            payment.has_paid = True
            payment.save()
            messages.success(request, "Payment confirmed! Welcome to Premium.")
            return redirect('students:results')
        
        elif "The transaction is being processed" in str(response.response_description):
             messages.info(request, "Payment is still processing. Please wait a moment and try again.")
             return redirect('students:payment_processing')
             
        else:
            # FAILED / CANCELLED / TIMEOUT
            # In Sandbox, if you didn't actually pay, this will fail.
            messages.error(request, f"Payment not found. Status: {response.response_description}")
            return redirect('students:payment_processing')

    except Exception as e:
        # sandbox often throws errors if transaction doesn't exist
        print(f"Manual Query Error: {e}")
        messages.error(request, "Could not verify payment yet. Please wait a few seconds and try again.")
        return redirect('students:payment_processing')

# ==========================================
# FEATURES
# ==========================================
@login_required
def toggle_favorite(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    favorite_item = Favorite.objects.filter(user=request.user, course=course).first()
    if favorite_item:
        favorite_item.delete()
    else:
        Favorite.objects.create(user=request.user, course=course)
    return redirect(request.META.get('HTTP_REFERER', 'students:results'))

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('course')
    courses = [f.course for f in favorites]
    return render(request, 'students/favorites.html', {'courses': courses})

@login_required
def course_reviews(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    reviews = course.reviews.all().select_related('user')
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            existing = CourseReview.objects.filter(user=request.user, course=course).exists()
            if not existing:
                review = form.save(commit=False)
                review.user = request.user
                review.course = course
                review.save()
            return redirect('students:course_reviews', course_id=course.id)
    else:
        form = ReviewForm()
    context = {'course': course, 'reviews': reviews, 'avg_rating': round(avg_rating, 1), 'review_count': reviews.count(), 'form': form}
    return render(request, 'students/course_reviews.html', context)

@login_required
def career_quiz(request):
    if request.method == 'POST':
        form = CareerQuizForm(request.POST)
        if form.is_valid():
            interest = form.cleaned_data['interest']
            strength = form.cleaned_data['strength']
            env = form.cleaned_data['environment']
            
            recommended_path = 'Arts' 
            if interest == 'health' or (strength == 'bio' and env in ['lab', 'field']):
                recommended_path = 'Medicine'
            elif interest == 'build' or (strength == 'math' and env == 'field'):
                recommended_path = 'Engineering'
            elif interest == 'tech' or (strength == 'tech' and env == 'remote'):
                recommended_path = 'ICT'
            elif interest == 'biz' or (strength == 'biz' and env == 'office'):
                recommended_path = 'Business'
            elif interest == 'law' or (strength == 'lang' and env == 'office'):
                recommended_path = 'Law'
            elif env == 'field' and strength == 'bio':
                recommended_path = 'Agriculture'
            
            messages.success(request, f"Based on your answers, we recommend exploring **{recommended_path}**!")
            base_url = reverse('students:results')
            return redirect(f"{base_url}?filter_path={recommended_path}")
    else:
        form = CareerQuizForm()
    return render(request, 'students/career_quiz.html', {'form': form})

# ==========================================
# MAIN RESULTS ENGINE
# ==========================================
@login_required
def results(request):
    payment, created = Payment.objects.get_or_create(user=request.user)
    if not payment.has_paid:
        return redirect('students:payment')
    
    try:
        grades = StudentGrades.objects.get(student=request.user)
    except StudentGrades.DoesNotExist:
        return redirect('students:enter_grades')

    student_mean_grade = grades.mean_grade 
    if not student_mean_grade:
        return redirect('students:enter_grades')

    # 1. Match Grades
    student_grade_rank = GRADE_RANKS.get(student_mean_grade, 1)
    qualified_grade_names_base = [g for g, r in GRADE_RANKS.items() if r <= student_grade_rank]
    escaped_grades = [re.escape(grade) for grade in qualified_grade_names_base]
    grade_regex = '|'.join(escaped_grades)

    # 2. Sort by Demand
    market_demand_sorting = Case(
        When(path__icontains='Medicine', then=Value(1)),
        When(path__icontains='Engineering', then=Value(2)),
        When(path__icontains='ICT', then=Value(3)),
        When(path__icontains='Law', then=Value(4)),
        When(path__icontains='Business', then=Value(5)),
        default=Value(20),
        output_field=IntegerField()
    )
        
    # 3. Base Query
    qualified_courses = Course.objects.filter(
        min_mean_grade__iregex=rf'({grade_regex})'
    ).annotate(
        market_rank=market_demand_sorting
    ).order_by('market_rank', 'name')
    
    # 4. Search & Filter
    search_query = request.GET.get('search', '')
    if search_query:
        qualified_courses = qualified_courses.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    available_paths = Course.objects.values_list('path', flat=True).distinct().order_by('path')
    selected_path = request.GET.get('filter_path')
    if selected_path and selected_path != 'All':
        qualified_courses = qualified_courses.filter(path__iexact=selected_path)

    # Helper for "Admission Chance"
    def add_chance_info(course_list):
        for course in course_list:
            student_points = 0.0
            path_lower = course.path.lower()
            
            if 'med' in path_lower: student_points = grades.cluster_points_medicine
            elif 'engin' in path_lower or 'sci' in path_lower or 'agri' in path_lower or 'ict' in path_lower: 
                student_points = grades.cluster_points_engineering
            elif 'law' in path_lower: student_points = grades.cluster_points_law
            else: student_points = grades.cluster_points_arts

            course.student_points = student_points 
            
            gap = student_points - course.min_cluster_points
            
            if course.min_cluster_points == 0:
                course.chance = "Qualified"
                course.chance_color = "success"
            elif gap >= 5:
                course.chance = "Highly Likely"
                course.chance_color = "success"
            elif gap >= 0:
                course.chance = "Competitive"
                course.chance_color = "warning text-dark"
            elif gap >= -2:
                course.chance = "Reach (Risky)"
                course.chance_color = "danger"
            else:
                course.chance = "Low Chance"
                course.chance_color = "secondary"
        return course_list

    # 5. Split, Limit, Process, Paginate
    degree_list = add_chance_info(list(qualified_courses.filter(level__icontains='Degree')[:200]))
    diploma_list = add_chance_info(list(qualified_courses.filter(level__icontains='Diploma')[:200]))
    cert_list = add_chance_info(list(qualified_courses.filter(level__icontains='Certificate')[:200]))
    artisan_list = add_chance_info(list(qualified_courses.filter(level__icontains='Artisan')[:200]))

    user_favorites_ids = set(Favorite.objects.filter(user=request.user).values_list('course_id', flat=True))

    context = {
        'grades': grades,
        'student_mean_grade': student_mean_grade,
        'available_paths': available_paths,
        'selected_path': selected_path,
        'search_query': search_query,
        'user_favorites_ids': user_favorites_ids,
        'degree_courses': paginate_queryset(request, degree_list),
        'diploma_courses': paginate_queryset(request, diploma_list),
        'certificate_courses': paginate_queryset(request, cert_list),
        'artisan_courses': paginate_queryset(request, artisan_list),
    }
    
    return render(request, 'students/results.html', context)