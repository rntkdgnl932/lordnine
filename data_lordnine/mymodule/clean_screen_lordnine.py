import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for

    try:
        print("clean_screen_start")
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("close_1 : top_right")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\close_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_for(0, 30, 960, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_2 : ", imgs_)
            if len(imgs_) > 0:
                for i in range(len(imgs_)):
                    click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                    time.sleep(0.5)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\title_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("title_exit : top_right")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\arim_close.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 400, 650, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("arim_close : middle")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def clean_screen_just_on_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for

    try:
        print("clean_screen_just_on_start")
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("close_1 : top_right")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\close_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_for(0, 80, 960, 140, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("close_2 : ", imgs_)
            if len(imgs_) > 0:
                for i in range(len(imgs_)):
                    click_pos_reg(imgs_[i][0], imgs_[i][1], cla)
                    time.sleep(0.5)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\title_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(880, 30, 960, 100, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("title_exit : top_right")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\arim_close.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(550, 400, 650, 480, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("arim_close : middle")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

