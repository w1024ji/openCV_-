import cv2
import numpy as np
import time

img1=cv2.imread('mot_color70.jpg')[190:350,440:560] # 버스를 크롭하여 모델 영상으로 사용
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2=cv2.imread('mot_color83.jpg')			     # 장면 영상
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

sift=cv2.SIFT_create()
kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)
print('특징점 개수:',len(kp1),len(kp2)) 

# 1 전수조사 + 가장 가까운 특징점
bf_matcher=cv2.BFMatcher()
bf_matches = bf_matcher.match(des1,des2)		# 가장 가까운 특징점을 받음
#print(len(bf_matches))

# 2 전수조사 + k개의 유사한 특징점
bf_knn_matches = bf_matcher.knnMatch(des1,des2, 2) 	# 가장 유사한 특징점 k(=2)개를 받음
#print(len(bf_knn_matches))

T=0.7
good_match=[]
for nearest1,nearest2 in bf_knn_matches:
    # if (nearest1.distance < T) : # 1) 고정 임계값, 2) 최근접 이웃 거리 비율 전략
    if (nearest1.distance/nearest2.distance) < T : # 3) 최근접 이웃 거리 비율 전략
        good_match.append(nearest1)

# 3 빠른 매칭 + + k개의 유사한 특징점
flann_matcher=cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_FLANNBASED)
flann_knn_matches=flann_matcher.knnMatch(des1,des2,2)   # 가장 유사한 특징점 k(=2)개를 받음
print(len(flann_knn_matches))
print(bf_matches[0].queryIdx, bf_matches[0].trainIdx)

# 매칭 전략을 만족하는 매칭쌍(good_match)을 찾음
T=0.7
good_match=[]
for nearest1,nearest2 in flann_knn_matches:
    if (nearest1.distance/nearest2.distance)<T: # 최근접 이웃 거리 비율 전략
        good_match.append(nearest1)
# T=0.7
# good_match=[]
# for nearest in flann_knn_matches:
#     if nearest.distance < T: # 1) 고정 임계값
#         good_match.append(nearest)

#print(len(good_match))
#print(good_match[0].queryIdx,' -- ', good_match[0].trainIdx, ' : ', good_match[0].distance)

img_match=np.empty((max(img1.shape[0],img2.shape[0]),img1.shape[1]+img2.shape[1],3),dtype=np.uint8)
cv2.drawMatches(img1,kp1,img2,kp2,good_match,img_match,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)  # good_match만 그림
# cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS, cv2.DrawMatchesFlags_DEFAULT, cv2.DrawMatchesFlags_DRAW_OVER_OUTIMG, cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS, cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS
cv2.imshow('Good Matches', img_match)

cv2.waitKey()
cv2.destroyAllWindows()