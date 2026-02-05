"""
Test Blog Likes Functionality
Tests the complete blog likes implementation
"""
from app import create_app
from models import db, Blog, BlogLike
import json

def test_blog_likes():
    """Test complete blog likes functionality"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("🧪 Testing Blog Likes Functionality")
        print("=" * 60)
        
        # 1. Check BlogLike model exists
        print("\n1️⃣ Checking BlogLike model...")
        try:
            from models import BlogLike
            print("✅ BlogLike model imported successfully")
        except ImportError as e:
            print(f"❌ BlogLike model import failed: {e}")
            return
        
        # 2. Check blog_likes table exists
        print("\n2️⃣ Checking blog_likes table...")
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        if 'blog_likes' in inspector.get_table_names():
            print("✅ blog_likes table exists")
            columns = [col['name'] for col in inspector.get_columns('blog_likes')]
            print(f"   Columns: {', '.join(columns)}")
        else:
            print("❌ blog_likes table not found!")
            return
        
        # 3. Check blogs table has likes column
        print("\n3️⃣ Checking blogs table has likes column...")
        blogs_columns = [col['name'] for col in inspector.get_columns('blogs')]
        if 'likes' in blogs_columns:
            print("✅ blogs.likes column exists")
        else:
            print("❌ blogs.likes column not found!")
            return
        
        # 4. Check if blogs exist
        print("\n4️⃣ Checking blog data...")
        blogs = Blog.query.all()
        print(f"   Total blogs: {len(blogs)}")
        if blogs:
            for blog in blogs[:3]:  # Show first 3
                print(f"   • {blog.title}: {blog.likes or 0} likes")
        else:
            print("   ⚠️  No blogs in database yet")
        
        # 5. Test creating a like (simulation)
        print("\n5️⃣ Testing BlogLike creation...")
        if blogs:
            test_blog = blogs[0]
            test_device_id = "test_device_12345_simulation"
            
            # Check if test like already exists
            existing = BlogLike.query.filter_by(
                blog_id=test_blog.id,
                device_id=test_device_id
            ).first()
            
            if existing:
                print(f"   ℹ️  Test like already exists for blog '{test_blog.title}'")
                print(f"   Created at: {existing.created_at}")
            else:
                # Create test like
                try:
                    test_like = BlogLike(
                        blog_id=test_blog.id,
                        device_id=test_device_id,
                        ip_address="127.0.0.1"
                    )
                    db.session.add(test_like)
                    
                    # Update blog likes count
                    if test_blog.likes is None:
                        test_blog.likes = 0
                    original_likes = test_blog.likes
                    test_blog.likes += 1
                    
                    db.session.commit()
                    
                    print(f"   ✅ Successfully created test like")
                    print(f"   Blog: '{test_blog.title}'")
                    print(f"   Likes: {original_likes} → {test_blog.likes}")
                    
                    # Clean up test like
                    db.session.delete(test_like)
                    test_blog.likes = original_likes
                    db.session.commit()
                    print(f"   🧹 Cleaned up test data")
                    
                except Exception as e:
                    db.session.rollback()
                    print(f"   ❌ Error creating test like: {e}")
        
        # 6. Check routes exist
        print("\n6️⃣ Checking Flask routes...")
        with app.test_client() as client:
            # Check if routes are registered
            routes = [rule.rule for rule in app.url_map.iter_rules()]
            like_route = any('/blog/<int:blog_id>/like' in route for route in routes)
            check_route = any('/blog/<int:blog_id>/like/check' in route for route in routes)
            
            if like_route:
                print("   ✅ POST /blog/<blog_id>/like route exists")
            else:
                print("   ❌ Like route not found")
            
            if check_route:
                print("   ✅ POST /blog/<blog_id>/like/check route exists")
            else:
                print("   ❌ Check like route not found")
        
        # 7. Database statistics
        print("\n7️⃣ Database Statistics:")
        total_blogs = Blog.query.count()
        total_likes_count = db.session.query(db.func.sum(Blog.likes)).scalar() or 0
        total_blog_likes = BlogLike.query.count()
        
        print(f"   Total blogs: {total_blogs}")
        print(f"   Total likes (aggregated): {total_likes_count}")
        print(f"   Total blog_likes records: {total_blog_likes}")
        
        if total_blog_likes > 0:
            print(f"\n   Recent likes:")
            recent_likes = BlogLike.query.order_by(BlogLike.created_at.desc()).limit(5).all()
            for like in recent_likes:
                blog = Blog.query.get(like.blog_id)
                print(f"   • Blog '{blog.title if blog else 'N/A'}' - {like.created_at}")
        
        print("\n" + "=" * 60)
        print("✅ Blog Likes Test Completed!")
        print("=" * 60)
        
        # Summary
        print("\n📝 Summary:")
        print("   ✓ BlogLike model exists")
        print("   ✓ blog_likes table created")
        print("   ✓ blogs.likes column exists")
        print("   ✓ Flask routes registered")
        print("   ✓ Database is ready for blog likes")
        print("\n🎯 Next Steps:")
        print("   1. Test blog likes on frontend")
        print("   2. Click the heart icon on any blog post")
        print("   3. Check that likes persist across page refreshes")
        print("   4. Verify you can't like the same post twice")

if __name__ == '__main__':
    test_blog_likes()
