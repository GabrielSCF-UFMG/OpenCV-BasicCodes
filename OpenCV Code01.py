import cv2

import cv2
print(cv2.__version__)


# Read the image file
image = cv2.imread("casa.png")

# Display the image
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Converting image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the gray image
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Applying Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the Gaussian image
cv2.imshow("Gaussian Image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Applying Edge Detection
edges = cv2.Canny(image, 100, 200)

# Display the Gaussian image
cv2.imshow("Edge Detectin Image", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying multiple image processing steps
gray_blurred_edges = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY), (5,5), 0), 100,200)

# Display the multiple iamge processiong steps image
cv2.imshow("Multiple processing Edge Detectin Image", gray_blurred_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create windows to display the images

width = 996
higth = 664

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)#| cv2.WINDOW_KEEPRATIO , (width,higth))
cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)#| cv2.WINDOW_KEEPRATIO , (width,higth))
cv2.namedWindow("Gaussian Image", cv2.WINDOW_NORMAL)#| cv2.WINDOW_KEEPRATIO , (width,higth))
cv2.namedWindow("Edge Detectin Image", cv2.WINDOW_NORMAL)#| cv2.WINDOW_KEEPRATIO , (width,higth))
cv2.namedWindow("Multiple processing Edge Detectin Image", cv2.WINDOW_NORMAL)#| cv2.WINDOW_KEEPRATIO , (width,higth))

# Show the images in the windows
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Gaussian Image", blurred_image)
cv2.imshow("Edge Detectin Image", edges)
cv2.imshow("Multiple processing Edge Detectin Image", gray_blurred_edges)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
