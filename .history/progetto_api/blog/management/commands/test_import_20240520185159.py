# test_import.py
from blog.mo

try:
    from blog.models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
