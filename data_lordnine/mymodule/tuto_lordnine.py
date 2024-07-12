import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def tuto_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    from action_lordnine import skip_start

    try:

        print("tuto_start")

        skip_start(cla)

    except Exception as e:
        print(e)


def way_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    from action_lordnine import skip_start

    try:

        print("way_check")

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\up_right.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("top_right", imgs_)
            # click_pos_reg(imgs_.x + 100, imgs_.y - 30, cla)
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\right.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("right", imgs_)
                # click_pos_reg(imgs_.x + 23, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\left.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("left", imgs_)
                    # click_pos_reg(imgs_.x -35, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\down.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("down", imgs_)
                        # click_pos_reg(imgs_.x, imgs_.y + 35, cla)


    except Exception as e:
        print(e)


def quest_checking(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    from action_lordnine import skip_start

    try:

        print("quest_checking")

        # hwal
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\hwal_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("hwal_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\hwal_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hwal_2", imgs_)
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\hwal_sayong_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 690, 880, 780, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)

