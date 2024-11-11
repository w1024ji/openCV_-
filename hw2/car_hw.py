import cv2
import numpy as np

## 자동차 번호판 후보 검출하기 과제 ##

# 이미지를 가져옵니다
gray = cv2.imread('05.jpg', cv2.IMREAD_GRAYSCALE)

# 1. 전처리(잡음 제거): 저는 medianBlur을 사용했습니다.
median = cv2.medianBlur(gray, 7)
cv2.imshow('median', median)

# 2. 숫자 부분의 주요 특징이 세로 에지 검출 - Sobel을 사용했습니다 -
sobel = cv2.Sobel(median, cv2.CV_64F, 1, 0, ksize=3)
sobel_abs = cv2.convertScaleAbs(sobel)
cv2.imshow('Sobel',sobel_abs)


# 3. Canny를 사용해 임계값 600, 700을 둬서 검은 배경과 흰 에지를 분리했습니다
canny=cv2.Canny(sobel_abs,600,700)	# Tlow=600, Thigh=700으로 설정
cv2.imshow('Canny',canny)


# 4. 가로로 긴 구조요소 se1를 이용하여 dilate을 k번 한 다음에 erode를 k번 하는 close를 만들었습니다.
k=16
se1=np.uint8([[0,0,0],			# 구조 요소
              [1,1,1],
              [0,0,0]])

# se2=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
b_closing=cv2.erode(cv2.dilate(canny,se1,iterations=k),se1,iterations=k)	# 닫기
cv2.imshow('Morphology',b_closing)


cv2.waitKey()
cv2.destroyAllWindows()