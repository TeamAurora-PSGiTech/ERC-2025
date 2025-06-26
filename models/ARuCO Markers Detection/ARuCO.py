import cv2
import cv2.aruco as aruco


image = cv2.imread('marker_images/0.jpeg') 
if image is None:
    raise FileNotFoundError("Image not found.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray = cv2.GaussianBlur(gray, (5, 5), 0)


aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(aruco_dict, parameters)


corners, ids, _ = detector.detectMarkers(gray)


if ids is not None:
    aruco.drawDetectedMarkers(image, corners, ids)
    for i, marker_id in enumerate(ids):
        print(f"Detected ArUco ID: {marker_id[0]}")
else:
    print("No markers detected.")


cv2.imshow("Detected ArUco Markers", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

