import os
import io
import django
from django.core.management import call_command

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Initialize Django
django.setup()

# Open a file with UTF-8 encoding
with io.open("posts.json", "w", encoding="utf-8") as f:
    # Dump the blog.Post data with proper encoding
    call_command("dumpdata", "blog.Post", indent=2, stdout=f)

print("Data exported successfully to posts.json")