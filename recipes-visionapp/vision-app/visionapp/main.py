import cv2
import sys
import glob

def get_camera_index():
    camIndex = [int(vi.split("/")[-1][5:]) for vi in glob.glob("/dev/video*")]
    for ci in camIndex:
        try:
            cap = cv2.VideoCapture(ci)
            ret, frame = cap.read()
            cap.release()
            if ret == True:
                return ci
        except:
            pass
    return None 


def main(argv=None):
    if argv is None:
        argv = sys.argv
    print("Searching for camera index")
    cindex = get_camera_index()
    if cindex is None:
        print("Camera not found")
        return 0

    print(f"Camera at {cindex}")

    cap = cv2.VideoCapture(cindex)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0

            
