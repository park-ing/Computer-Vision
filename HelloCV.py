import sys
import cv2

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('ch01/cat.bmp')    # cat.bmp 파일을 불러와 img변수에 저장.

if img is None:                     # 영상 파일 불러오기가 실패하면 에러 메시지를 출력하고 종료.
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')            # "image"라는 이름의 새 창을 만들고, 이 창에 img영상을 출력하고, 키보드 입력이 있을 때까지 대기.
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()             # 생성된 모든 창을 닫음.



