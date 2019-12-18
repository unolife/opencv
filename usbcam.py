import cv2

count = 0
max_frame = 5

resolution = (4096,2160)

save_dir = '/Users/test/Desktop/opencv/sample_data/'
capture = cv2.VideoCapture(1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

while True:
    ret, frame = capture.read()
    # ret => True or False (If cv read frame properly, ret returns true)
    try:
        if count < max_frame and ret:
            cv2.imwrite('{}/{}.jpg'.format(save_dir,count), frame)
            count += 1
            print(count)
    except:
        pass
    # cv2.imshow("VideoFrame", frame)
    # if cv2.waitKey(1) > 0: break

capture.release()
cv2.destroyAllWindows()

# https://076923.github.io/posts/Python-opencv-2/
