import easyocr
import cv2

# Load image and set background and text color
image_path = "test_bank_1.jpg"
background_color = [255, 255, 255]  # white background
text_color = [0, 0, 0]  # black text
img = cv2.imread(image_path)
img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=background_color)

# Initialize EasyOCR reader and set language
reader = easyocr.Reader(['en'])

# Get bounding boxes for text
results = reader.readtext(img, detail=0, paragraph=False, min_size=10, text_threshold=0.8, low_text=0.3, contrast_ths=0.1)

# Draw bounding boxes on image
for bbox in results:
    x1, y1, x2, y2 = bbox[0][0], bbox[0][1], bbox[0][2], bbox[0][3]
    img = cv2.rectangle(img, (x1, y1), (x2, y2), text_color, 2)

# Show image with bounding boxes
cv2.imshow("Image with bounding boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
