from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.management import call_command

class Command(BaseCommand):
    help = "Creates a superuser and populates blog/course data automatically for Render"

    def handle(self, *args, **kwargs):
        # 1. Create Superuser (admin / password123)
        # This ensures you can always log into /admin/ on the live site
        username = "admin"
        email = "ericngumi01@gmail.com"
        password = "password123"

        if not User.objects.filter(username=username).exists():
            self.stdout.write(f"Creating superuser '{username}'...")
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
        else:
            self.stdout.write(f"Superuser '{username}' already exists.")

        # 2. Populate Blog (Calls your existing repopulate_blog_v2 script)
        self.stdout.write("Running blog population...")
        try:
            call_command('repopulate_blog_v2')
            self.stdout.write(self.style.SUCCESS("Blog population finished."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Blog population failed: {e}"))
            
        # 3. Populate Courses (Calls your existing repopulate_max_volume script)
        self.stdout.write("Running course population...")
        try:
            call_command('repopulate_max_volume')
            self.stdout.write(self.style.SUCCESS("Course population finished."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Course population failed: {e}"))

        self.stdout.write(self.style.SUCCESS("Init Data Complete!"))