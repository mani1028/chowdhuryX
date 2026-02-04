"""Test brochure download link"""
from app import create_app

app = create_app()

with app.test_client() as client:
    # Test brochure access
    response = client.get('/static/uploads/chowdhuryX.pdf')
    print(f"✅ Brochure Status: {response.status_code}")
    print(f"✅ Content-Type: {response.content_type}")
    if response.status_code == 200:
        print("✅ Brochure download link works successfully!")
        print(f"✅ File size: {len(response.data)} bytes")
    else:
        print("❌ Brochure not accessible")

