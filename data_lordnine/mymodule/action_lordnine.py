import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def confirm_all(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        is_confirm = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\confirm_btn_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 570, 640, 640, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("confirm_btn_1 : 무엇", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\confirm_btn_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 980, 960, 1040, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("confirm_btn_2 : 소환 확인", imgs_)
            x_reg = imgs_.x
            y_reg = imgs_.y

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\sohwan_not_checked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 980, 40, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.3)

            click_pos_reg(x_reg, y_reg, cla)
            is_confirm = True

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\move_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 570, 960, 1040, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("move_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        return is_confirm

    except Exception as e:
        print(e)



def out_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("out_check")

        is_out = False

        result_menu_open = menu_open_check(cla)
        if result_menu_open == False:

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\out\\talk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 940, 60, 990, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_out = True

        return is_out

    except Exception as e:
        print(e)




def menu_open_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("menu_open_check")

        is_menu = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("character_change_btn", imgs_)
            is_menu = True

        return is_menu

    except Exception as e:
        print(e)


def menu_open(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    from clean_screen_lordnine import clean_screen_start
    try:

        print("menu_open")

        result_menu_open = menu_open_check(cla)

        menu_open_count = 0
        while result_menu_open is False:
            menu_open_count += 1
            if menu_open_count > 5:
                result_menu_open = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("character_change_btn", imgs_)
                result_menu_open = True
            else:
                clean_screen_start(cla)
                click_pos_2(915, 50, cla)
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)
            time.sleep(0.5)


    except Exception as e:
        print(e)

def skip_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg

    from clean_screen_lordnine import clean_screen_just_on_start

    try:

        print("skip_start")

        is_skip = False

        # top
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_skip = True
        else:
            # bottom
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 940, 960, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_skip = True
            else:
                # screen_click
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\screen_click_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 600, 700, 1040, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_skip = True

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("off")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
        else:
            clean_screen_just_on_start(cla)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("on")
            is_skip = True

        if is_skip == True:
            time.sleep(0.5)

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\next_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 940, 960, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\exit_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)


        return is_skip

    except Exception as e:
        print(e)



def move_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("move_check")

        is_move = False

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 570, 550, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("move_check : ok")
                is_move = True
                break
            time.sleep(0.2)

        is_move_count = 0
        is_move_second = 0
        while is_move is True:
            is_move_second += 1

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 570, 550, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("이동중", is_move_second, "초")
                is_move_count = 0

            else:
                is_move_count += 1
                if is_move_count > 3:
                    is_move = False

            time.sleep(1)


        return is_move

    except Exception as e:
        print(e)