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

    from function_game import text_check_get, int_put_, imgs_set_, click_pos_reg, click_pos_2
    from tuto_lordnine import way_check
    from action_lordnine import skip_start


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

    # result = text_check_get(490, 510, 560, 550, cla)
    # result_num = int_put_(result)
    # print("result", result_num)

    time.sleep(1)

    click_pos_2(925, 50, cla)

    time.sleep(0.5)
    pydirectinput.click()

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
