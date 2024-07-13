import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random
    import pydirectinput

    from function_game import text_check_get, int_put_, imgs_set_, imgs_set_for, click_pos_reg, click_pos_2
    from tuto_lordnine import way_check
    from action_lordnine import skip_start
    from clean_screen_lordnine import clean_screen_just_on_start


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5


    try:
        # result = text_check_get(490, 510, 560, 550, cla)
        # result_num = int_put_(result)
        # print("result", result_num)

        # 어빌리티
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\ability.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 150, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("ability", imgs_)

            # 2_1
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\2_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(270, 100, 360, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ability : 2_1", imgs_)

                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\ability_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 60, 420, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("ability_clicked ", imgs_)
                        click_pos_2(320, 150, cla)
                        break
                    else:
                        click_pos_2(305, 285, cla)
                    time.sleep(0.5)
            # 2_2
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\2_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 100, 430, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ability : 2_2", imgs_)

                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\ability_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 60, 420, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("ability_clicked ", imgs_)
                        click_pos_2(380, 150, cla)
                        break
                    else:
                        click_pos_2(400, 285, cla)
                    time.sleep(0.5)

            # 3_1
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\3_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 100, 550, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ability : 3_1", imgs_)

                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\ability_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 60, 420, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("ability_clicked ", imgs_)
                        click_pos_2(505, 150, cla)
                        break
                    else:
                        click_pos_2(490, 285, cla)
                    time.sleep(0.5)
            # 3_2
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\3_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(520, 100, 610, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("ability : 3_2", imgs_)

                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ability\\ability_clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 60, 420, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("ability_clicked ", imgs_)
                        click_pos_2(565, 150, cla)
                        clean_screen_just_on_start(cla)
                        break
                    else:
                        click_pos_2(585, 285, cla)
                    time.sleep(0.5)


        # skip_start(cla)
        #
        # for i in range(4):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("i", i)
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(1)

    except Exception as e:
        print(e)
