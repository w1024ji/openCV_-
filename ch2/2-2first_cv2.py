import cv2     # opencv 모듈 import
import sys

img=cv2.imread('soccer.jpg')	# 압축을 풀어서 ndarray 형태로 저장. Default는 cv2.IMREAD_COLOR 이다.
grayImg = cv2.imread('soccer.jpg',  cv2.IMREAD_GRAYSCALE)   # gray로 파일을 읽고 싶다면

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
print(type(img)) # <class 'numpy.ndarray'>
print(img.shape) # (948, 1434, 3) 행의 개수(세로), 열의 개수(가로), 컬러(3byte)

print(type(grayImg)) # <class 'numpy.ndarray'>
print(grayImg.shape) # (948, 1434) 세로, 가로

print(img[0,0]) # 컬러-3byte-이어서 [162 104 98]

print(grayImg[0,0]) # 흑백-1byte-이어서 109

print(img[0,0,0], img[0,0,1], img[0,0,2]) # 162 104 98 출력.

cv2.imshow('Image Display',img)	            # 이미지 보여주기. 문자열은 창의 타이틀을 의미함.
cv2.imshow('Gray Image Display',grayImg)

cv2.waitKey()               # 키보드 입력 대기. 바로 닫지 마!
cv2.destroyAllWindows()     # 모든 윈도우 제거 후 프로그램 종료