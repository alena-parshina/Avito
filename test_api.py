import requests

BASE_URL = "http://your-api-url.com"

def test_create_ad():
    data_samples = [
        ({"sellerID": "123", "name": "Test", "price": 1000, "statistics": {}}, "Create valid ad"),
        ({"sellerID": "123", "name": "Test", "price": 1000}, "Create ad without statistics"),
        ({"name": "Test", "price": 1000}, "Create ad without sellerID"),
        ({"sellerID": "123", "name": "Test", "price": -100}, "Create ad with invalid price")
    ]
    
    for data, description in data_samples:
        response = requests.post(f"{BASE_URL}/api/1/item", json=data)
        print(f"\n[{description}]")
        print(f"Request: {response.request.method} {response.url}")
        print(f"Response status: {response.status_code}, Response body: {response.text}")

def test_get_ad():
    ad_ids = ["valid_id", "invalid_id"]
    
    for ad_id in ad_ids:
        response = requests.get(f"{BASE_URL}/api/1/item/{ad_id}")
        print(f"\n[Get ad {ad_id}]")
        print(f"Request: {response.request.method} {response.url}")
        print(f"Response status: {response.status_code}, Response body: {response.text}")

def test_get_seller_ads():
    seller_ids = ["valid_seller", "invalid_seller"]
    
    for seller_id in seller_ids:
        response = requests.get(f"{BASE_URL}/api/1/{seller_id}/item")
        print(f"\n[Get seller ads {seller_id}]")
        print(f"Request: {response.request.method} {response.url}")
        print(f"Response status: {response.status_code}, Response body: {response.text}")

def test_get_statistics():
    ad_ids = ["valid_id", "invalid_id"]
    
    for ad_id in ad_ids:
        response = requests.get(f"{BASE_URL}/api/1/statistic/{ad_id}")
        print(f"\n[Get statistics {ad_id}]")
        print(f"Request: {response.request.method} {response.url}")
        print(f"Response status: {response.status_code}, Response body: {response.text}")

if __name__ == "__main__":
    test_create_ad()
    test_get_ad()
    test_get_seller_ads()
    test_get_statistics()
