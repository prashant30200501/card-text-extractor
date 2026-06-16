import cv2

camera = cv2.VideoCapture(0)

while True:
    success, frame = camera.read()

    if not success:
        print("Could not access camera")
        break

    cv2.imshow("Card Extractor Camera", frame)

    

    key = cv2.waitKey(1)

    if key ==ord('s'):
        cv2.imwrite("card.jpg",frame)
        print("image saved")
    
    

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()