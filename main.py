import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('test.jpg')
cv2.imshow('Original', img)
# Change to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5,5),0)
cv2.imshow('Blur', blur)
# Apply canny filter
canny = cv2.Canny(blur, 0,200)
# Remove titles 
canny[190:238,:] = 0
canny[388:,:] = 0
# plt.imshow(canny)
cv2.imshow('Canny', canny)
# Get contours
contours, hier = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Print len of contours
print(f'Contours found: {len(contours)}')
# Draw contours on original image
cv2.drawContours(img, contours, -1, (0,255,0),3)
cv2.imshow("With contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()