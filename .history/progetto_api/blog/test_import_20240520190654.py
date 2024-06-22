# test_import.py
from .models import Post
try:
    from .models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
