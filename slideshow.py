import glob
import os
import cv2

# 특정 폴더에 있는 이미지 파일(*.jpg) 목록 읽기
"""# os.listdir()
file_list = os.listdir('ch01/images')
img_files = [file for file in file_list if file.endswith('.jpg')]
"""
# glob.glob()
img_files = glob.glob('ch01/images/*.jpg')
img = cv2.imread(img_files[0])
cv2.imshow('image', img)
cv2.waitKey()
#for f in img_files:
#    print(f)

# 전체 화면 영상 출력 창 만들기
# 먼저 cv2.WINDOW_NORMAL 속성의 창을 만든 후, cv2.setWindowProperty() 함수를 사용하여 전체 화면 속성으로 변경
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 불러온 영상을 반복적으로 출력하기
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img)

    if cv2.waitKey(1000) >= 0:  # 1초 기다렸는데 아무 키도 안누르면 -1 return // 아무키나 누르면 0 이상 값을 return(루프 종료)
        # == 27     # ESC
        break

    idx += 1
    if idx >= cnt:
        idx = 0

# 맥에서는 전체화면 부분이 이상하다..
