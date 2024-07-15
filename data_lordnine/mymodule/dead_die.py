import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add, myQuest_play_check
    from massenger import line_to_me
    from potion_lordnine import potion_buy_start
    from action_lordnine import out_check, loading_check

    try:
        print("dead_check")

        dead = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(250, 400, 750, 900, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            for i in range(5):
                result_loading = loading_check(cla)
                if result_loading == True:
                    break
                time.sleep(0.2)

            for i in range(5):
                result_out = out_check(cla)
                if result_out == True:
                    break
                time.sleep(0.2)

            why = "죽었으니 당장 눈으로 확인하라. 10초 준다..."
            line_to_me(cla, why)
            time.sleep(10)

            dead = True

        if dead == True:
            result_schedule = myQuest_play_check(cla, "check")
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성":
                myQuest_play_add(cla, result_schedule_)

            potion_buy_start(cla)
            dead_recorvery(cla)

        return dead
    except Exception as e:
        print(e)
        return 0


def dead_recorvery(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_lordnine import clean_screen_start

    try:
        print("dead_recorvery")

        for i in range(5):
            result_out = out_check(cla)
            if result_out == True:
                break
            time.sleep(0.5)

        is_cross = False
        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\boohwal_cross_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(200, 50, 260, 120, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                is_cross = True
                break
            time.sleep(0.2)

        if is_cross == True:

            for i in range(10):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\recorver_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(90, 430, 260, 490, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("boohwal_cross_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    break
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\boohwal_cross_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 50, 260, 120, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("boohwal_cross_btn")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
            # 아이템 복구
            for i in range(10):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\item.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("item")
                    clean_screen_start(cla)
                    break
                else:
                    click_pos_2(220, 110, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\recorver_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 430, 260, 490, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("boohwal_cross_btn")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

