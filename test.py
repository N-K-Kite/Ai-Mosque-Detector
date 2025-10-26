# Create a simple function for your project demo
def detect_mosque_for_drone(image_path, confidence_threshold=0.5):
    """
    Mosque detection system for humanitarian drone protection.
    
    Args:
        image_path: Path to drone camera image
        confidence_threshold: Minimum confidence (0-1)
    
    Returns:
        bool: True if mosque detected (DO NOT ENGAGE), False if safe
    """
    results = final_model(image_path, conf=confidence_threshold, verbose=False)
    
    num_mosques = len(results[0].boxes)
    
    if num_mosques > 0:
        print("⚠️  PROTECTED ZONE DETECTED!")
        print(f"   {num_mosques} mosque(s) found")
        print("   🚫 DO NOT ENGAGE - Safe zone")
        for i, box in enumerate(results[0].boxes):
            conf = float(box.conf[0])
            print(f"   Detection {i+1}: {conf:.1%} confidence")
        return True
    else:
        print("✅ No protected structures detected")
        print("   Area clear for operations")
        return False

# Test the function
print("🎯 Testing Humanitarian Drone Protection System:\n")
test_img = f'{dataset.location}/test/images/{test_images[0]}'
is_protected = detect_mosque_for_drone(test_img)