import cv2
import numpy as np

# 자동차 이미지 입력받기
car_no = str(input("자동차 영상 번호 (00~05): "))
img = cv2.imread('cars/' + car_no + '.jpg')

def hw2(img):
    # grayscale로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1. 전처리(잡음 제거): 저는 medianBlur을 사용했습니다.
    median = cv2.medianBlur(gray, 7)

    # 2. 숫자 부분의 주요 특징이 세로 에지 검출 - Sobel을 사용했습니다 -
    sobel = cv2.Sobel(median, cv2.CV_64F, 1, 0, ksize=3)
    sobel_abs = cv2.convertScaleAbs(sobel)

    # 3. Canny를 사용해 임계값 600, 700을 둬서 검은 배경과 흰 에지를 분리했습니다
    canny = cv2.Canny(sobel_abs, 600, 700)

    # 4. 가로로 긴 구조요소 se1를 이용하여 dilate을 k번 한 다음에 erode를 k번 하는 close를 만들었습니다.
    k = 16
    se1 = np.uint8([[0, 0, 0],
                    [1, 1, 1],
                    [0, 0, 0]])
    b_closing = cv2.erode(cv2.dilate(canny, se1, iterations=k), se1, iterations=k)

    return b_closing

# 전처리 처리 리턴
hw2_img = hw2(img)

# contour를 찾아 최소 최소면적 사각형을 찾는다
contours, _ = cv2.findContours(hw2_img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)

# 비율로 자동차 번호판 후보를 찾기
def verify_aspect_size(size):
    w, h = size
    if h == 0 or w == 0:
        return False
    aspect = h / w if h > w else w / h  # 종횡비 계산
    chk1 = 3000 < (h * w) < 12000  # 번호판 넓이 조건
    chk2 = 2.0 < aspect < 6.5  # 번호판 종횡비 조건
    return chk1 and chk2 # True 아니면 False를 리턴하겠군


for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, peri*0.05, True) # 그 도형을 구성하고 있는 근사한 도형. epsilon이 클수록 더 큰 도형이 나온다
    if len(approx) == 4: # 사각형인가?
        print('approx가 4인가? yes')
        (x, y, w, h) = cv2.boundingRect(approx)
        print('(w,h)', (w,h))

        if verify_aspect_size((w,h)): # 넓이와 종횡비 조건을 통과하면 그려주자
            print('통과한 contour: ', contour)
            cv2.drawContours(img, contour, -1, (0, 255, 0), 2)

cv2.imshow("first", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
