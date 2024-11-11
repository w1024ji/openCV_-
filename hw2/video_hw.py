import cv2

# 동영상을 가져옵니다
video_path = 'face2.mp4'
cap = cv2.VideoCapture(video_path)

# 한 번 확인해주고
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

current_effect = 'n'  # 첫 시작은 오리지널로 합시다
effect_text = "Original"  # 왼쪽 상단에 띄울 글자입니다

# 루프를 돌려줍니다
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # 디폴트 프레임입니다
    output_frame = frame

    # 마지막으로 누른 키가 뭐냐에 따라 동영상 이펙트가 달라집니다
    if current_effect == 'n':
        output_frame = frame
        effect_text = "original"
        text_color = (255, 0, 255)  # 보라색입니다

    elif current_effect == 'b': # b를 누르면 bilateralFilter 이펙트가 적용되도록 해줍니다
        output_frame = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)
        effect_text = "bilateral"
        text_color = (255, 0, 255)

    elif current_effect == 's': # s를 누르면 stylization 이펙트가 적용되도록 해줍니다
        output_frame = cv2.stylization(frame, sigma_s=30, sigma_r=0.05)
        effect_text = "stylization"
        text_color = (255, 0, 255)

    elif current_effect == 'g': # g를 누르면 graypencil 적용되도록 해줍니다
        gray_sketch, _ = cv2.pencilSketch(frame, sigma_s=30, sigma_r=0.05, shade_factor=0.02)
        output_frame = gray_sketch
        effect_text = "graypencil"
        text_color = (150, 150, 150) # 흑백으로 해야해서 회색 색깔을 넣어줬습니다

    elif current_effect == 'c': # c를 누르면 colorpencil 이펙트가 적용되도록 해줍니다
        _, color_sketch = cv2.pencilSketch(frame, sigma_s=30, sigma_r=0.05, shade_factor=0.02)
        output_frame = color_sketch
        effect_text = "colorpencil"
        text_color = (255, 0, 255)

    elif current_effect == 'o': # o를 누르면 oilPainting 이펙트가 적용되도록 해줍니다
        output_frame = cv2.xphoto.oilPainting(frame, size=5, dynRatio=1)
        effect_text = "oilPainting"
        text_color = (255, 0, 255)

    # 글의 특성을 정해줍니다
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    position = (10, 30)

    # 글을 넣어줍니다
    cv2.putText(output_frame, effect_text, position, font, font_scale, text_color, thickness)

    # 프레임을 띄웁니다
    cv2.imshow('homework2_video_effect', output_frame)

    # 키 준비시키기!!
    key = cv2.waitKey(1) & 0xFF

    # 중간에 키가 바뀐다면 해당 키와 연결된 이펙트 적용 해줍니다
    if key == ord('n'):
        current_effect = 'n'

    elif key == ord('b'):
        current_effect = 'b'

    elif key == ord('s'):
        current_effect = 's'

    elif key == ord('g'):
        current_effect = 'g'

    elif key == ord('c'):
        current_effect = 'c'

    elif key == ord('o'):
        current_effect = 'o'

    # 이건 과제 요구사항에 없지만 q가 눌리면 꺼지게 설정했습니다.
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
