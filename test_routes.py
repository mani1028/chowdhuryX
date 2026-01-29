from app import create_app

app = create_app()
client = app.test_client()
routes = ['/', '/about', '/services', '/blog', '/contact', '/careers', '/portfolio', '/faq', '/testimonials', '/privacy-policy', '/terms', '/cookies']

print("\n" + "="*50)
print("ROUTE TEST RESULTS")
print("="*50)

passed = 0
failed = 0

for route in routes:
    try:
        response = client.get(route)
        if response.status_code == 200:
            print(f"✅ {route:30} OK")
            passed += 1
        else:
            print(f"❌ {route:30} ERROR: {response.status_code}")
            failed += 1
    except Exception as e:
        error_msg = str(e)[:80]
        print(f"❌ {route:30} ERROR: {error_msg}")
        failed += 1

print("="*50)
print(f"TOTAL: {passed}/{len(routes)} PASSED, {failed} FAILED")
print("="*50)
