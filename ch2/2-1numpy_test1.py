import numpy as np          # numpy 모듈 import, np로 사용

a = np.zeros((2,5), np.int32)   # 초기값이 0인 배열. zeros는 행렬을 만드는 함수. 2행, 5열
b = np.ones((3,1), np.uint8)    # 초기값이 1인 배열 unsigned int. 3행 1열
c = np.empty((1,5), np.float64) # 초기값이 없는(임의의 값 저장) 배열. 1행, 5열
d = np.full(5, 15, np.float32)  # 특정 값(15)으로 채워진 배열
d2 = np.full((1,5), 15, np.float32)

print(type(a), type(a[0]), type(a[0][0]))       # 객체 자료형(type) 출력
print(type(b), type(b[0]), type(b[0][0]))           
print(type(c), type(c[0]), type(c[0][0]))
print(type(d), type(d[0])) # <class 'numpy.ndarray'> <class 'numpy.float32'>


print('c 형태:', c.shape, '   d 형태:', d.shape) # 객체 형태(shape) 출력. 행열을 보여준다

print('a: ', a)    # 객체 원소 출력
print('b: ', b)
print('c: ', c)
print('d: ', d) # [15. 15. 15. 15. 15.]
print('d2: ', d2) # [[15. 15. 15. 15. 15.]]
# d와 d2의 차이는 d는 1차원 배열이라는 거고 d2는 2차원 배열이라는 것.
# shape을 5로 하느냐, (1,5)로 하느냐는 큰 차이가 있다.
print(type(d2), type(d2[0])) # <class 'numpy.ndarray'> <class 'numpy.ndarray'>

