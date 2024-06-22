# test_import.py

try:
    from .blog.models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
