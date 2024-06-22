# test_import.py
from .models
try:
    from .models import Post
    print("Import successful")
except ImportError:
    print("Import failed")
