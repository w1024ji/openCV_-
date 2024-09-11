import numpy as np

arr1 =np.arange(10).reshape(2,5)	# 연속적인 숫자 배열 0~9를 사용해서 2행 5열 만드시오
print(arr1)

arr2 = np.arange(8)
print(arr2) # [0 1 2 3 4 5 6 7]
arr2.reshape(2,4)
print(arr2) # [0 1 2 3 4 5 6 7] reshape()는 원본을 건들지 않고 복사본을 리턴하는 듯
# 그래서 복사본을 출력하려면
arr3 = arr2.reshape(2,4)
print(arr3) # [[0 1 2 3]
             # [4 5 6 7]]

print(arr1[0,2]) 	# 원소 0,2를 추출
print(arr1[0][2])   # 행0과 열2의 원소 추출

print(arr1[[0,1],[1,3]]) # [0,1] [1,3] 색인 -> [1 8]

print(arr1[0])  	# 행0
print(arr1[0,])     # 행0
print(arr1[0,:])    # 행0

print(arr1[:,0])    	# 열0

print(arr1[:,0:3])  	# 슬라이싱. 모든 행과 0~2열의 교집합에 해당하는 건?

print(arr1[:2,3:])  	# 0~1행과 3~끝열의 교집합에 해당하는 건?
