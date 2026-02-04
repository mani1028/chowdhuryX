"""Quick test to verify services route works"""
from app import create_app

app = create_app()

with app.test_client() as client:
    print("Testing /services route...")
    response = client.get('/services')
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.content_type}")
    if response.status_code != 200:
        print(f"Error: {response.data.decode('utf-8')[:500]}")
    else:
        print("✅ Services page loads successfully!")
