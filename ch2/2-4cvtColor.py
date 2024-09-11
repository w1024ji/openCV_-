import cv2
import sys

img=cv2.imread('soccer.jpg') # 컬러로 읽어서
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv2.imshow('Original Image', img) # 컬러로 출력

# 1 그레이 이미지
#grayImg = cv2.imread('soccer.jpg',  cv2.IMREAD_GRAYSCALE) # 그레이 이미지로
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 그레이 이미지로 색상 변환 BGR2GRAY
# cv2.imshow('GrayImage', grayImg)

# 2 컬러 모델 변환
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
ycrcbImg = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 왜 변환해?
# 이미지를 처리하는데에 있어서 용이함.

cv2.imshow('HSVImage', hsvImg)
cv2.imshow('YCrCbImage', ycrcbImg)
cv2.imshow('RGBImage', rgbImg)

cv2.waitKey()
cv2.destroyAllWindows()
