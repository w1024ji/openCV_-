import cv2
import numpy as np

# rock4.mp4를 준비합니다
input_video_path = 'rock4.mp4'
output_video_path = 'rock4_result.mp4'

# 비디오 캐벼를 준비합니다
cap = cv2.VideoCapture(input_video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

# 살구색을 위한 YCrCb를 준비해줍니다
lower_skin = np.array([0, 133, 77], dtype=np.uint8)
upper_skin = np.array([255, 173, 127], dtype=np.uint8)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임을 YCrCb와 threshold로 변환해줍니다
    ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    mask = cv2.inRange(ycrcb, lower_skin, upper_skin)

    # 마스크를 정리해주기 위해 모폴로지를 사용합니다
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=2)

    # 컨투어를 찾아봅니다
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # 가장 큰 컨투어가 손이라고 가정합니다
        contour = max(contours, key=cv2.contourArea)

        # convexHull이랑 convexityDefects를 찾아줍니다
        hull = cv2.convexHull(contour, returnPoints=False)
        defects = cv2.convexityDefects(contour, hull)

        # convexity 결함을 기준으로 fingertips를 계산합니다
        fingertip_count = 0
        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])

                # 각도를 계산합니다
                a = np.linalg.norm(np.array(start) - np.array(far))
                b = np.linalg.norm(np.array(end) - np.array(far))
                c = np.linalg.norm(np.array(start) - np.array(end))
                angle = np.arccos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * 57.2958

                # 깊은 결함만 계산합니다. 각도 < 90이며 거리를 높여 헷갈리지 않도록 해줍니다. 1200를 d의 threshold로 해줍니다.
                if angle <= 90 and d > 12000:
                    fingertip_count += 1
                    cv2.circle(frame, far, 5, [0, 0, 255],
                               -1)

        # 개수로 가위, 바위, 보를 정해줍니다
        if fingertip_count == 0:
            gesture = "Rock"
        elif fingertip_count == 1:
            gesture = "Scissors"
        elif fingertip_count > 1:
            gesture = "Paper"
        else:
            gesture = "Unknown"

        # 해당 가위, 바위, 보를 상단에 적어줍니다
        cv2.putText(frame, gesture, (frame.shape[1] - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_AA)

        # 파란색으로 컨투어를 그려줍니다
        cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)  # Blue contour only

    # 결과 비디오에 써줍니다.
    out.write(frame)

    cv2.imshow('Rock Paper Scissors', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):  # 1분짜리 비디오를 만드려고 waitKey(30) 했습니다
        break

cap.release()
out.release()
cv2.destroyAllWindows()
