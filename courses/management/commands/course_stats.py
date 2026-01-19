from django.core.management.base import BaseCommand
from courses.models import Course

class Command(BaseCommand):
    help = "Displays statistics about the courses in the database"

    def handle(self, *args, **kwargs):
        total = Course.objects.count()
        
        # Count using case-insensitive search to catch "Degree" and "degree"
        degrees = Course.objects.filter(level__icontains='Degree').count()
        diplomas = Course.objects.filter(level__icontains='Diploma').count()
        certificates = Course.objects.filter(level__icontains='Certificate').count()
        artisans = Course.objects.filter(level__icontains='Artisan').count()

        self.stdout.write(self.style.SUCCESS('--- COURSE DATABASE STATISTICS ---'))
        self.stdout.write(f'Total Courses:   {total}')
        self.stdout.write(f'🎓 Degrees:      {degrees}')
        self.stdout.write(f'📚 Diplomas:     {diplomas}')
        self.stdout.write(f'📄 Certificates: {certificates}')
        self.stdout.write(f'🛠️  Artisan:      {artisans}')
        self.stdout.write('----------------------------------')
        
        # Verification check
        sum_levels = degrees + diplomas + certificates + artisans
        if sum_levels < total:
            diff = total - sum_levels
            self.stdout.write(self.style.WARNING(f'⚠️  Warning: {diff} courses have undefined levels.'))