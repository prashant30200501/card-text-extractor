import cv2

camera = cv2.VideoCapture(0)

image_count = 1

while True:
    success, frame = camera.read()

    if not success:
        print("Could not access camera")
        break

    cv2.imshow("Card Extractor Camera", frame)

    

    key = cv2.waitKey(1)

    if key ==ord('s'):
        filename = f"images/card_{image_count}.jpg"
        cv2.imwrite(filename,frame)
        print(f"saved: {filename}")
        image_count += 1
      
    
    

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()