import cv2 as cv
import numpy as np

def main():
    calib_data_path = 'calib_data/MultiMatrix2.npz'
    calib_data = np.load(calib_data_path)

    cam_mat = calib_data['camMatrix']
    dist_coef = calib_data['distCoef']
    r_vectors = calib_data['rVector']
    t_vectors = calib_data['tVector']

    cap = cv.VideoCapture(0, cv.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        frame_undist = frame
        if ret:
            cv.imshow('Camara con distorcion', frame_undist)
            h, w = frame.shape[:2]

            newcameramtx, roi = cv.getOptimalNewCameraMatrix(cam_mat, dist_coef, (w,h), 1, (w,h))

            # corregir distorcion
            dst = cv.undistort(frame, cam_mat, dist_coef, None, newcameramtx)

            # recortar la imagen
            x, y, w, h = roi
            dst = dst[y:y+h, x:x+w]

            cv.imshow('Camara con correccion', dst)

            key = cv.waitKey(10)

            if key == ord('q'): break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
