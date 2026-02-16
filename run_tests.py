=import os
from dotenv import load_dotenv

# 1. FORCE testing environment before anything else loads
os.environ['FLASK_ENV'] = 'testing'
load_dotenv()

from app import create_app
from models import db, AdminUser

def setup_test_sqlite():
    # Initialize the app with the testing config
    app = create_app('testing')
    
    with app.app_context():
        print(f"📡 Using Database: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # 2. Create the SQLite tables
        db.create_all()
        print("✅ SQLite tables initialized.")

        # 3. Create a unique Testing Admin
        test_username = "test_admin"
        if not AdminUser.query.filter_by(username=test_username).first():
            tester = AdminUser(
                username=test_username,
                email="tester@chowdhuryx.com",
                full_name="QA Tester",
                role="super_admin",
                is_active=True
            )
            tester.set_password("testpass123")
            db.session.add(tester)
            db.session.commit()
            print(f"✅ Created Test Admin: {test_username} / testpass123")
        
        return app

if __name__ == "__main__":
    app = setup_test_sqlite()
    print("🚀 Starting test server on http://127.0.0.1:5000")
    app.run(debug=True)