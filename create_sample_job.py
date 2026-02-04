"""
Test script to create a sample job
"""
from app import create_app, db
from models import Job
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    # Create a sample job
    job = Job(
        title="Senior Python Developer",
        description="""We are looking for an experienced Python developer to join our growing team.

You will be responsible for developing and maintaining our core applications, working with modern frameworks and technologies.

This is a great opportunity to work on challenging projects with a talented team in a collaborative environment.""",
        
        requirements="""5+ years of professional Python development experience
Strong knowledge of Flask or Django frameworks
Experience with PostgreSQL and SQLAlchemy
Proficiency in RESTful API design
Understanding of Git version control
Excellent problem-solving skills
Strong communication and teamwork abilities""",
        
        responsibilities="""Design, develop, and maintain Python applications
Write clean, maintainable, and well-documented code
Collaborate with cross-functional teams
Participate in code reviews
Optimize application performance
Mentor junior developers
Stay updated with latest Python technologies""",
        
        location="Bangalore, India (Hybrid)",
        job_type="Full-time",
        department="Engineering",
        experience_required="5-8 years",
        salary_range="₹15-25 LPA",
        status="active",
        closes_at=datetime.now() + timedelta(days=30)
    )
    
    db.session.add(job)
    db.session.commit()
    
    print("✅ Sample job created successfully!")
    print(f"   Job ID: {job.id}")
    print(f"   Title: {job.title}")
    print(f"   You can now test the job detail page at: /careers/job/{job.id}")
