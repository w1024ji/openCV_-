import cv2
import numpy as np

# 전역 변수 설정
drawing = False
mode = None
ix, iy = -1, -1


# 마우스 콜백 함수
def draw_shape(event, x, y, flags, param):
    global ix, iy, drawing, mode, img

    # 마우스 왼쪽 버튼을 누른 경우
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        drawing = True

    # 마우스 오른쪽 버튼을 누른 경우
    elif event == cv2.EVENT_RBUTTONDOWN:
        ix, iy = x, y
        drawing = True

    # 마우스 움직임 처리
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if flags & cv2.EVENT_FLAG_LBUTTON:  # 왼쪽 버튼을 누르고 움직일 때
                if flags & cv2.EVENT_FLAG_SHIFTKEY:  # Shift 키와 함께
                    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # 초록색 원
                elif not (flags & cv2.EVENT_FLAG_ALTKEY or flags & cv2.EVENT_FLAG_CTRLKEY):  # ALT와 CTRL이 없는 상태
                    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)  # 파란색 원

            elif flags & cv2.EVENT_FLAG_RBUTTON:  # 오른쪽 버튼을 누르고 움직일 때
                if flags & cv2.EVENT_FLAG_SHIFTKEY:  # Shift 키와 함께
                    cv2.circle(img, (x, y), 5, (0, 255, 255), -1)  # 노란색 원
                elif not (flags & cv2.EVENT_FLAG_ALTKEY or flags & cv2.EVENT_FLAG_CTRLKEY):  # ALT와 CTRL이 없는 상태
                    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)  # 빨간색 원

    # 마우스 버튼을 뗀 경우
    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        drawing = False
        if flags & cv2.EVENT_FLAG_ALTKEY:  # ALT와 함께 그릴 때
            if event == cv2.EVENT_LBUTTONUP:  # 직사각형 테두리
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
            elif event == cv2.EVENT_RBUTTONUP:  # 직사각형 내부 칠하기
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        elif flags & cv2.EVENT_FLAG_CTRLKEY:  # CTRL과 함께 그릴 때
            radius = int(np.sqrt((x - ix) ** 2 + (y - iy) ** 2))
            if event == cv2.EVENT_LBUTTONUP:  # 원 테두리
                cv2.circle(img, (ix, iy), radius, (255, 0, 0), 2)
            elif event == cv2.EVENT_RBUTTONUP:  # 원 내부 칠하기
                cv2.circle(img, (ix, iy), radius, (255, 0, 0), -1)


# 600*900 크기의 흰색 이미지 생성
img = np.ones((600, 900, 3), np.uint8) * 255
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_shape)

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF

    # 's' 키를 눌러 이미지 저장
    if key == ord('s'):
        cv2.imwrite('output_image.png', img)

    # 'q' 키를 눌러 종료
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
