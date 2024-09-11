import cv2
import sys

# 비디오 캡처 객체 생성
# cap = cv2.VideoCapture('slow_traffic_small.mp4')    # 비디오 파일
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)    # 웹캠 비디오

if not cap.isOpened():
    sys.exit('동영상 연결 실패')

while True:
    # read()는 들어오는 동영상에 대해서 프레임을 캡쳐한다. 실제 프레임은 두번째 리턴값인 frame에 들어간다.
    ret, frame = cap.read()  # 비디오를 구성하는 프레임 획득

    if not ret: # ret는 프레임을 성공적으로 가져오면 true, 그렇지 않으면(동영상 종료) false
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    cv2.imshow('Video display', frame) # 하나의 창에 프레임이 촤르륵 바뀐다.

    key = cv2.waitKey(1)  # 1밀리초 동안 키보드 입력 기다림(정수)
    if key == ord('q'):  # 'q' 키가 들어오면 루프를 빠져나감, ord()는 문자를 아스키 값으로 변환하는 함수
        # imwrite() 이미지에 대한 함수이다. 특정한 이미지를 저장할 수 있다.
        cv2.imwrite('./captured.png', frame)  # 이미지 캡처 및 저장
        break

cap.release()  # 카메라와 연결을 끊음
cv2.destroyAllWindows()
