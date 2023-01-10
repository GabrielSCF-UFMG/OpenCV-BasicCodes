import cv2

# Create a SIFT descriptor
sift = cv2.xfeatures2d.SIFT_create()

# Read the image
img1 = cv2.imread("moedorCilindrico.png", 0)
img2 = cv2.imread("valvula.png", 0)

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.det

# create BFMatcher object
bf = cv2.BFMatcher()

# Match descriptors.
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None, flags=2)

# Show the image
cv2.imshow("Detected object", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
