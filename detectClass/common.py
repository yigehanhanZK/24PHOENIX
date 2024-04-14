import numpy as np


def armor_post_process(armor_location, car_box):
    armor_location[:, 0] += car_box[0]
    armor_location[:, 1] += car_box[1]
    armor_location[:, 2] += car_box[0]
    armor_location[:, 3] += car_box[1]
    armor_location[:, 4] += car_box[0]
    armor_location[:, 5] += car_box[1]
    armor_location[:, 6] += car_box[0]
    armor_location[:, 7] += car_box[1]
    # armor_location[:, 8] = scores
    # armor_location[:, 9] = classID
    armor_location[:, 10] += car_box[0]
    armor_location[:, 11] += car_box[1]
    armor_location[:, 12] += car_box[0]
    armor_location[:, 13] += car_box[1]


def convert_detection_results(car_boxes, car_scores):
    """
    将目标检测网络的输出转换成SORT算法需要的格式
    """
    detections = []
    for bbox, score in zip(car_boxes, car_scores):
        x1, y1, x2, y2 = bbox
        detections.append([x1, y1, x2, y2, score])
    return np.array(detections)
