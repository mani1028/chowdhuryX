"""
Fix Blog Likes - Initialize NULL likes to 0
"""
from app import create_app
from models import db, Blog

def fix_blog_likes():
    """Initialize NULL likes to 0 for existing blogs"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("🔧 Fixing Blog Likes")
        print("=" * 60)
        
        # Count blogs with NULL likes
        blogs_null_likes = Blog.query.filter(Blog.likes == None).count()
        print(f"\nBlogs with NULL likes: {blogs_null_likes}")
        
        if blogs_null_likes > 0:
            # Update blogs with NULL likes to 0
            Blog.query.filter(Blog.likes == None).update({Blog.likes: 0})
            db.session.commit()
            print(f"✅ Updated {blogs_null_likes} blogs with NULL likes to 0")
        else:
            print("✅ All blogs already have likes initialized")
        
        # Show current stats
        total_blogs = Blog.query.count()
        total_likes = db.session.query(db.func.sum(Blog.likes)).scalar() or 0
        
        print(f"\n📊 Blog Likes Statistics:")
        print(f"  Total blogs: {total_blogs}")
        print(f"  Total likes: {total_likes}")
        
        print("\n" + "=" * 60)
        print("✅ Blog likes fix completed!")
        print("=" * 60)

if __name__ == '__main__':
    fix_blog_likes()
