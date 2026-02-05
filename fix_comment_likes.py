"""
Fix Comment Likes - Initialize NULL likes to 0
"""
from app import create_app
from models import db, Comment

def fix_comment_likes():
    """Initialize NULL likes to 0 for existing comments"""
    app = create_app()
    
    with app.app_context():
        print("=" * 60)
        print("💬 Fixing Comment Likes")
        print("=" * 60)
        
        # Count comments with NULL likes
        comments_null_likes = Comment.query.filter(Comment.likes == None).count()
        print(f"\nComments with NULL likes: {comments_null_likes}")
        
        if comments_null_likes > 0:
            # Update comments with NULL likes to 0
            Comment.query.filter(Comment.likes == None).update({Comment.likes: 0})
            db.session.commit()
            print(f"✅ Updated {comments_null_likes} comments with NULL likes to 0")
        else:
            print("✅ All comments already have likes initialized")
        
        # Show current stats
        total_comments = Comment.query.count()
        total_likes = db.session.query(db.func.sum(Comment.likes)).scalar() or 0
        
        print(f"\n📊 Comment Likes Statistics:")
        print(f"  Total comments: {total_comments}")
        print(f"  Total likes: {total_likes}")
        
        print("\n" + "=" * 60)
        print("✅ Comment likes fix completed!")
        print("=" * 60)

if __name__ == '__main__':
    fix_comment_likes()
