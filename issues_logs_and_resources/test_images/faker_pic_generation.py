from faker import Faker
import requests
import os

fake = Faker()
os.makedirs("test_images_faker", exist_ok=True)

# Generate random profile pictures
for i in range(10):
    img_url = fake.image_url(width=800, height=800)
    response = requests.get(img_url)
    
    with open(f"test_images_faker/profile_{i+1}.jpg", "wb") as f:
        f.write(response.content)
    
    print(f"Downloaded profile_{i+1}.jpg")