# test_import.py
from blog

try:
    from blog.models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
