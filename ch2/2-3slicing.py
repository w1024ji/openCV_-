import cv2
import sys
import numpy as np

img=cv2.imread('soccer.jpg') # 컬러로 읽어서
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

print(type(img)) # <class 'numpy.ndarray'>
print(img.shape) # (948, 1434, 3)

# 1 numpy의 슬라이싱slicing
# img.shape[0]은 '이미지의 세로'를 말한다
# img.shape[1]은 '이미지의 가로'를 말한다
#                                   행 중에서 '0~절반'을 쓸거고, 열 중에서 '0~절반'을 쓸거고, 컬러는 다 쓰겠다
cv2.imshow('Upper left half', img[0 : img.shape[0]//2, 0 : img.shape[1]//2, :])
#                      세로의 1/4 지점에서 시작 : 세로의 3/4 지점에서 끝, 가로의 1/4 지점에서 시작 : 가로의 3/4 지점에서 끝
cv2.imshow('Central half', img[img.shape[0]//4 : 3*img.shape[0]//4, img.shape[1]//4 : 3*img.shape[1]//4, :])

# 세로, 가로 다 쓰겠다. 하지만 컬러 중에서 n번째 해당하는 값만 쓰겠다.
# OpenCV는 BGR로 색상값 저장
# r, g, b가 순서대로 2, 1, 0번째임
cv2.imshow('Red channel', img[:,:,2])   # r만 쓰겠다. 값이 크면 하얘짐
cv2.imshow('Green channel', img[:,:,1]) # g만 쓰겠다
cv2.imshow('Blue channel', img[:,:,0])  # b만 쓰겠다

# 2 OpenCV의 split
b,g,r = cv2.split(img) # 특정한 색상을 분리하는 함수 split(). 리턴값 3개를 준다
black = np.zeros((img.shape[0],img.shape[1]), np.uint8)
# 빨간색이 나오는 이미지를 만드려면 3byte를 충족해야 함.
# 그래서 black이란 변수에 0을 초기값으로 갖는 같은 크기의 행렬을 만든 다음, merge()를 이용해 합쳐주면 된다
img_R = cv2.merge((black,black, r))     # b, g, r 순이다(매개변수)
img_B = cv2.merge((b, black, black))
cv2.imshow('Red in Color', img_R)
cv2.imshow('Blue in Color', img_B)


cv2.waitKey()
cv2.destroyAllWindows()