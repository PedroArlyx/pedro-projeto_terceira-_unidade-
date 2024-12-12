import cv2

webcam= cv2.VideoCapture(0)

if webcam.isOpened():
        validacao,frame =webcam.read()
        cv2.imshow('foto da webcam', frame)
        key = cv2.waitKey(5)
        cv2.imwrite(f'foto.png',frame)
webcam.release()
cv2.destroyAllWindows()