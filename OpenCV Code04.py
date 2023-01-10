import cv2

# Create an ORB descriptor
orb = cv2.ORB_create()


# Read the image

arquivo1 = "moedorCilindrico.png"
arquivo2 = "parafusoMaior.png"

img1 = cv2.imread(arquivo1, 0)
img2 = cv2.imread(arquivo2, 0)

# Check if the image is already grayscale
if len(img2.shape) == 2:
    # The image is already grayscale, no need to convert
    gray = img2
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Show the grayscale image
cv2.imshow("Grayscale image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image to a file
cv2.imwrite("gray_template_"+arquivo2, gray)

img2 = gray

print(img1.shape)
print(img2.shape)

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

print(kp1)
print(des1)
print(kp2)
print(des2)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)

# Show the image
cv2.imshow("Detected object", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
