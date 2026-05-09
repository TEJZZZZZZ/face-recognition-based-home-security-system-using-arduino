import cv2

import serial

arduino = serial.Serial('COM3', 9600)
# Function to resize an image
def resize_image(image, width=500, height=300):
    return cv2.resize(image, (450, 250))


# Load pre-stored face templates
template1 = cv2.imread('C:\\Users\\JANKI\\PycharmProjects\\pythonProject4\\IMG20230309135747.jpg', cv2.IMREAD_GRAYSCALE)
template2 = cv2.imread('C:\\Users\\JANKI\\PycharmProjects\\pythonProject4\\IMG_20240208_142924_819.jpg',
                       cv2.IMREAD_GRAYSCALE)
template3 = cv2.imread('C:\\Users\\JANKI\\PycharmProjects\\pythonProject4\\Snapchat-1924841239.jpg',
                       cv2.IMREAD_GRAYSCALE)
template4 = cv2.imread('C:\\Users\\JANKI\\PycharmProjects\\pythonProject4\\1707382816453.jpg', cv2.IMREAD_GRAYSCALE)
# Resize the templates
template1 = resize_image(template1)
template2 = resize_image(template2)
template3 = resize_image(template3)
template4 = resize_image(template4)

# Create a list of templates and corresponding labels
templates = [template1, template2, template3, template4]
labels = ["Shlok", "Tejaswini", "Shravani", "Neha"]

# Open the webcam
cap = cv2.VideoCapture(0)

# Password for LCD
password = "1609"

while True:
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    name = "Unknown Person"  # Initialize name as "Unknown Person"

    # Iterate through templates and perform template matching
    for template, label in zip(templates, labels):
        result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        # Set a threshold for matching
        threshold = 0.8

        # If a match is found, consider it a known face
        if max_val > threshold:
            name = label
            break

    # If an unknown face is detected, ask for a password
    if name == "Unknown Person":
        entered_password = input("Enter the password: ")

        # Check if the entered password is correct
        if entered_password == password:
            arduino.write(b'0')  # Send '0' to Arduino for no alert
        else:
            arduino.write(b'1')  # Send '1' to Arduino for alert



        # Draw rectangle and label on the face
        cv2.putText(frame, "Face Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    else:
        # Known face detected, send '0' to Arduino for no alert
        arduino.write(b'0')

        # Draw rectangle and label on the face
        cv2.putText(frame, name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()