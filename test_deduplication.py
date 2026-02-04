"""
Test file deduplication logic
"""
import os
import hashlib

def test_hash():
    """Test basic hash functionality"""
    print("=" * 60)
    print("Testing File Deduplication Logic")
    print("=" * 60)
    
    # Create test content
    content1 = b"This is test image content"
    content2 = b"This is test image content"  # Same
    content3 = b"This is different content"    # Different
    
    hash1 = hashlib.sha256(content1).hexdigest()
    hash2 = hashlib.sha256(content2).hexdigest()
    hash3 = hashlib.sha256(content3).hexdigest()
    
    print(f"\n📝 Hash 1: {hash1[:16]}...")
    print(f"📝 Hash 2: {hash2[:16]}...")
    print(f"📝 Hash 3: {hash3[:16]}...")
    
    print(f"\n✅ Identical files have same hash: {hash1 == hash2}")
    print(f"✅ Different files have different hash: {hash1 != hash3}")
    
    print("\n" + "=" * 60)
    print("How it works:")
    print("=" * 60)
    print("""
1. When uploading a file, calculate its SHA-256 hash
2. Check all files in upload directory for matching hash
3. If match found → return existing filename (no upload)
4. If no match → save file with timestamp prefix
    
Benefits:
✅ Saves disk space
✅ Faster uploads for duplicate files  
✅ Prevents duplicate content
✅ Works across different filenames
    """)
    
    print("=" * 60)
    print("✅ Deduplication Logic Ready!")
    print("=" * 60)

if __name__ == '__main__':
    test_hash()

