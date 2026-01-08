from PIL import Image
import os
 
# Create test_images directory
os.makedirs("test_images_python_imaging_library", exist_ok=True)

# Test cases: (filename, width, height, format, file_size_target_kb)
test_cases = [
    # Valid - Small files
    ("valid_tiny_50x50.jpg", 50, 50, "JPEG", None),
    ("valid_small_200x200.jpg", 200, 200, "JPEG", None),
    ("valid_small_200x200.png", 200, 200, "PNG", None),
    
    # Valid - Medium files
    ("valid_medium_500x500.jpg", 500, 500, "JPEG", None),
    ("valid_medium_500x500.png", 500, 500, "PNG", None),
    ("valid_profile_800x800.jpg", 800, 800, "JPEG", None),
    
    # Valid - Large files
    ("valid_large_1500x1500.jpg", 1500, 1500, "JPEG", None),
    ("valid_large_2000x2000.png", 2000, 2000, "PNG", None),
    
    # Edge case - Very small
    ("edge_tiny_10x10.jpg", 10, 10, "JPEG", None),
    ("edge_tiny_1x1.png", 1, 1, "PNG", None),
    
    # Edge case - Non-square
    ("edge_wide_1920x1080.jpg", 1920, 1080, "JPEG", None),
    ("edge_tall_1080x1920.jpg", 1080, 1920, "JPEG", None),
    ("edge_narrow_100x1000.png", 100, 1000, "PNG", None),
    
    # Edge case - Huge dimensions
    ("edge_huge_5000x5000.jpg", 5000, 5000, "JPEG", None),
    ("edge_huge_8000x8000.png", 8000, 8000, "PNG", None),
]

def create_test_image(filename, width, height, format_type):
    """Create a colored test image with text overlay"""
    # Create image with gradient background
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    # Create gradient
    for y in range(height):
        for x in range(width):
            r = int((x / width) * 255)
            g = int((y / height) * 255)
            b = 150
            pixels[x, y] = (r, g, b)
    
    # Save
    filepath = os.path.join("test_images_python_imaging_library", filename)
    if format_type == "JPEG":
        img.save(filepath, "JPEG", quality=85)
    else:
        img.save(filepath, "PNG")
    
    # Get file size
    size_bytes = os.path.getsize(filepath)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    
    if size_mb > 1:
        print(f"{filename}: {width}x{height} - {size_mb:.2f} MB")
    else:
        print(f"{filename}: {width}x{height} - {size_kb:.2f} KB")

# Generate all test images
print("Generating test images...\n")
for filename, width, height, format_type, _ in test_cases:
    create_test_image(filename, width, height, format_type)

print(f"\nGenerated {len(test_cases)} test images in ./test_images_python_imaging_library/")