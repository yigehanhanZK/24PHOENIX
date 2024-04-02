import yaml
import cv2
import numpy as np

import sys
sys.path.append('..')
from macro import CAMERA_CONFIG_DIR
from cameraClass.camera import HTCamera


def read_yaml(camera_type):
    """
    读取相机标定参数,包含外参，内参，以及关于雷达的外参
    :param camera_type: 相机编号
    :return: 读取成功失败标志位，相机内参，畸变系数，和雷达外参，相机图像大小
    """
    yaml_path = "../{0}/camera{1}.yaml".format(CAMERA_CONFIG_DIR, camera_type)
    try:
        with open(yaml_path, 'rb') as f:
            res = yaml.load(f, Loader=yaml.FullLoader)
            K_0 = np.float32(res["K_0"]).reshape(3, 3)
            C_0 = np.float32(res["C_0"])
            E_0 = np.float32(res["E_0"]).reshape(4, 4)
            imgsize = tuple(res['ImageSize'])

        return True, K_0, C_0, E_0, imgsize
    except Exception as e:
        print("[ERROR] {0}".format(e))
        return False, None, None, None, None


def tune_exposure(cap: HTCamera, date, high_reso=False):
    """
    :param cap: camera target
    :param high_reso: 采用微秒/毫秒为单位调整曝光时间
    """
    cv2.namedWindow("exposure press q to exit", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("exposure press q to exit", 1280, 960)
    cv2.moveWindow("exposure press q to exit", 300, 300)
    cv2.setWindowProperty("exposure press q to exit", cv2.WND_PROP_TOPMOST, 1)
    if high_reso:
        cv2.createTrackbar("ex", "exposure press q to exit", 0, 1,
                           lambda x: None)
        cv2.setTrackbarMax("ex", "exposure press q to exit", 30000)
        cv2.setTrackbarMin("ex", "exposure press q to exit", 0)
        cv2.setTrackbarPos("ex", "exposure press q to exit",
                           int(cap.getExposureTime() * 1000))
        # 模拟增益区间为0到256
        cv2.createTrackbar("g1", "exposure press q to exit", 0, 1,
                           lambda x: None)
        cv2.setTrackbarMax("g1", "exposure press q to exit", 256)
        cv2.setTrackbarMin("g1", "exposure press q to exit", 0)
        cv2.setTrackbarPos("g1", "exposure press q to exit",
                           int(cap.getAnalogGain()))
    else:
        cv2.createTrackbar("ex", "exposure press q to exit", 0, 1,
                           lambda x: None)
        cv2.setTrackbarMax("ex", "exposure press q to exit", 120)
        cv2.setTrackbarMin("ex", "exposure press q to exit", 0)
        cv2.setTrackbarPos("ex", "exposure press q to exit",
                           int(cap.getExposureTime()))
        cv2.createTrackbar("g1", "exposure press q to exit", 0, 1,
                           lambda x: None)
        cv2.setTrackbarMax("g1", "exposure press q to exit", 256)
        cv2.setTrackbarMin("g1", "exposure press q to exit", 0)
        cv2.setTrackbarPos("g1", "exposure press q to exit",
                           int(cap.getAnalogGain()))

    flag, frame = cap.read()

    while (flag):
        if high_reso:
            cap.setExposureTime(
                cv2.getTrackbarPos("ex", "exposure press q to exit"))
        else:
            cap.setExposureTime(
                cv2.getTrackbarPos("ex", "exposure press q to exit") * 1000)
        cap.setGain(cv2.getTrackbarPos("g1", "exposure press q to exit"))

        cv2.imshow("exposure press q to exit", frame)
        flag, frame = cap.read()
        key = cv2.waitKey(1)
        if key == ord('q') & 0xFF:
            break
        if key == ord('s') & 0xFF:
            cap.saveParam(date)
            break

    ex = cv2.getTrackbarPos("ex", "exposure press q to exit")
    g1 = cv2.getTrackbarPos("g1", "exposure press q to exit")
    if high_reso:
        ex = ex / 1000
    print(f"finish set exposure time {ex:.03f}ms")
    print(f"finish set analog gain {g1}")
    cv2.destroyWindow("exposure press q to exit")
