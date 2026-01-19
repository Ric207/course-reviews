#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Install dependencies
pip install -r requirements.txt

# 2. Collect static files (CSS, Images)
python manage.py collectstatic --no-input

# 3. Update the database structure
python manage.py migrate
```

*Note: If you are on Windows, creating `.sh` files is fine, just make sure to save it.*

---

### 📝 Step 4: Freeze Requirements

We need to tell Render exactly which libraries (Django, Pillow, etc.) your project uses.

Run this command in your terminal:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file listing all your installed packages.

---

### 🚀 Step 5: Push to GitHub

Render pulls your code from GitHub.

1.  Go to [GitHub.com](https://github.com/) and create a **New Repository** (e.g., `course-reviews-ke`).
2.  Run these commands in your terminal to upload your code:

```bash
git init
git add .
git commit -m "Ready for deployment"
git branch -M main
git remote add origin https://github.com/Ric207/course-reviews-ke.git
git push -u origin main