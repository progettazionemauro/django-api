# test_import.py
from blog.models import P

try:
    from blog.models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
