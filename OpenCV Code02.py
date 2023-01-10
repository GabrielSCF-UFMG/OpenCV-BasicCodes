import cv2

# Read the image and the template
image = cv2.imread("moedorCilindrico.png")

template = cv2.imread("valvula.png")

# Check if the image is already grayscale
if len(template.shape) == 2:
    # The image is already grayscale, no need to convert
    gray = template
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Show the grayscale image
cv2.imshow("Grayscale image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image to a file
cv2.imwrite("gray_template_valvula.png", gray)

w, h = gray.shape[::-1]

# Perform template matching
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Locate the template in the image
loc = cv2.minMaxLoc(result)[2]

# Draw a rectangle around the matched region
cv2.rectangle(image, loc, (loc[0] + w, loc[1] + h), (0, 0, 255), 2)

# Show the image
cv2.imshow("Detected object", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
