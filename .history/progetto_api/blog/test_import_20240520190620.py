# test_import.py

try:
    from .models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
