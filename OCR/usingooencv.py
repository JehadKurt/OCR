import cv2

# Load image and convert to grayscale
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold image to black and white
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform morphological operations to remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

# Find contours and filter for text regions
contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    if area < 100:
        continue
    x,y,w,h = cv2.boundingRect(contour)
    roi = img[y:y+h, x:x+w]

    # Draw bounding box around each word
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Show image with bounding boxes
cv2.imshow("Image with bounding boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()