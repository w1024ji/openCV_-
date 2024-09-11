import cv2
import numpy as np

# 바탕이 하얀 이미지 255
img = np.ones((600,300,3), np.uint8) * 255 	# 600*300*3*8bits 행렬, 흰색으로 초기화

# 시작점 pt1과 끝점 pt2와, 그 라인의 색상과 두께
cv2.line(img, (50,50), (150,150), (255,0,0), 3)

# 첫 번째 인자는 그릴 대상이다. 여기선 img
cv2.rectangle(img, (50,50), (150,150), (0,255,0), 2)
cv2.rectangle(img, (50,200), (150,300), (0,255,0), cv2.FILLED)

# circle은 중심값이 있다. (220, 100)
cv2.circle(img, (220,100), 50, (0,0,255), 4)
# cv2.circle(img, (220,250), 30, (0,255,255), -1) 아래와 같은 코드이다. -1은 cv2.FILLED와 같은 의미
cv2.circle(img, (220,250), 30, (0,255,255), cv2.FILLED)

# 타원은 중심값이 2개이다. (100, 400), (75, 50)
# 타원이 얼마나 기울어져 있는가? 30, 0, 180 (시계 방향으로 30도 회전), (타원의 호 중 180 정도만 보여주자)
cv2.ellipse(img, (100, 400), (75, 50), 30, 0, 180, (0,255,0), 3)

# pts에 저장된 점들을 차례대로 연결해주는 polylines()
# isClosed=False 라면 첫번째 점에서 마지막 점까지만 연결. True라면 마지막 점과 첫번재 점을 연결해준다.(폐곡)
pts = np.array([[220,350], [180,500], [260,500]], dtype=np.int32)
cv2.polylines(img, [pts], True, (255,0,0), 10)

# org에서 시작해서 그린다.(왼쪽 아래임)
cv2.putText(img, "text1", (50,500), cv2.FONT_HERSHEY_DUPLEX, 1, (128, 128, 0), 2)
cv2.putText(img, "text2", (50,570), cv2.FONT_HERSHEY_TRIPLEX, 2, (221, 160, 221), 4)

cv2.imshow('OpenGL Graphics',img)

cv2.waitKey()
cv2.destroyAllWindows()