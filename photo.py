import cv2
import os

def capture_and_save_image(image_path='captured_image.png'):
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return False

    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        return False

    # Display the captured frame (optional, for debugging purposes)
    cv2.imshow('Captured Image', frame)
    cv2.waitKey(1)  # Wait for a brief moment

    # Save the captured frame as an image file
    cv2.imwrite(image_path, frame)

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

    # Check if the image is saved
    if os.path.exists(image_path):
        print(f"Image saved successfully as {image_path}")
        return True
    else:
        print("Error: Image was not saved.")
        return False

# Call the function
if capture_and_save_image():
    print("Image capture and save successful.")
else:
    print("Image capture and save failed.")
