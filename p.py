import numpy as np
import cv2 as cv
import glob

chessboardSize = (10, 14)
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboardSize[0], 0:chessboardSize[1]]
prev_img_shape = None

objpoints = []
imgpoints = []
images = glob.glob('*.jpg')
for image in images:
    print(image)
    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, chessboardSize)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        cv.drawChessboardCorners(img, chessboardSize, corners2, ret)

    cv.imshow('img', img)
    cv.imwrite('caliResult.png', img)
    cv.waitKey(100)
cv.destroyAllWindows()
