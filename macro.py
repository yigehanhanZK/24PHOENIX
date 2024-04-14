# camera
CACHE_CONFIG_SAVE_DIR = 'save_stuff'
preview_location = [(100, 100)]
CAMERA_CONFIG_DIR = 'Camera_config'

# detect
CONF_THRESH_CAR = 0.5
CONF_THRESH_ARMOR = 0.01
IOU_THRESHOLD = 0.4
armor_locations = []
categories = ["B1", "B2", "B3", "B4", "B5", "B7", "R1", "R2", "R3", "R4", "R5", "R7"]

# lidar
LIDAR_TOPIC_NAME = '/livox/lidar'
PC_STORE_DIR = 'save_stuff/points'

# location
LOCATION_SAVE_DIR = 'save_stuff/position'
location_targets = {
    # enemy:red
    # red_base -> blue_outpost -> b_rt -> b_lt
    # enemy:blue
    # blue_base -> red_outpost -> r_rt -> r_lt
    'home_test':  # 家里测试，填自定义类似于赛场目标的空间位置
        {
            'red_base': [],
            'blue_outpost': [],
            'red_outpost': [],
            'blue_base': [],
            'r_rt': [],
            'r_lt': [],
            'b_rt': [],
            'b_lt': []
        },
    'game':  # 按照官方手册填入
        {
            # 24赛季相机位姿估计标记点
            'red_base': [1.760, 7.539, 0.200 + 0.920],  # red base
            'blue_outpost': [16.776, 12.565, 1.760],  # blue outpost
            'red_outpost': [11.176, 2.435, 1.760],  # red outpost
            'blue_base': [26.162, 7.539, 0.200 + 0.920],  # blue base
            'r_rt': [8.670, -5.715 - 0.400 + 15., 0.420],  # r0 right_top
            'r_lt': [8.670, -5.715 + 15., 0.420],  # r0 left_top
            'b_rt': [19.330, -9.285 + 0.400 + 15., 0.420],  # b0 right_top
            'b_lt': [19.330, -9.285 + 15., 0.420]  # b0 left_top
        }
}
