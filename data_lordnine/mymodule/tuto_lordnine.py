import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def tuto_start(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, imgs_set_
    from action_lordnine import skip_start, confirm_all, move_check

    try:

        print("tuto_start")

        result_move = move_check(cla)

        result_quest_ing = quest_ing_check(cla)

        if result_move == False and result_quest_ing == False:

            skip_start(cla)
            way_check(cla)

            # 퀘스트 클릭
            click_pos_2(870, 120, cla)
            time.sleep(0.3)
            confirm_all(cla)

            for i in range(5):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\near_aim_description.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 30, 600, 250, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("near_aim_description", imgs_)
                    click_pos_2(780, 130, cla)
                    time.sleep(0.3)
                    confirm_all(cla)
                    break
                time.sleep(0.2)


            quest_checking(cla)


    except Exception as e:
        print(e)

def quest_ing_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, int_put_, change_number
    from clean_screen_lordnine import clean_screen_start

    try:

        print("quest_ing_check")

        is_q = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\q_complete.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 110, 900, 200, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("q_complete", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\quest_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 820, 900, 900, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_btn", imgs_)
            is_q = True
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\q_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(640, 80, 720, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("q_1", imgs_)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\q_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(640, 80, 720, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("q_2", imgs_)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\off.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("off")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        clean_screen_start(cla)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("on")
            click_pos_2(480, 820, cla)

        return is_q

    except Exception as e:
        print(e)

def way_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, in_number_check, int_put_, change_number
    from action_lordnine import skip_start

    try:

        print("way_check")

        for i in range(5):

            is_way = False

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\up.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("up", imgs_)
                click_pos_reg(imgs_.x, imgs_.y - 30, cla)
                is_way = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\up_right.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("up_right", imgs_)
                click_pos_reg(imgs_.x + 100, imgs_.y - 30, cla)
                is_way = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\right.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("right", imgs_)
                click_pos_reg(imgs_.x + 23, imgs_.y, cla)
                is_way = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\left.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("left", imgs_)
                click_pos_reg(imgs_.x - 35, imgs_.y, cla)
                is_way = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\way\\down.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("down", imgs_)
                click_pos_reg(imgs_.x, imgs_.y + 35, cla)
                is_way = True

            if is_way == False:
                break
            else:
                time.sleep(0.5)

    except Exception as e:
        print(e)


def quest_checking(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from massenger import line_to_me

    from schedule import myQuest_play_add

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

        # new_maul
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\new_maul_talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 790, 550, 850, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("new_maul_talk", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # character_info_title
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\character_info_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(60, 90, 170, 130, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("character_info_title", imgs_)

            for i in range(5):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\character_info_status_plus_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 480, 500, 580, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("character_info_status_plus_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(450, 1005, cla)
                    break
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\character_info_status_add_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 590, 180, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("character_info_status_add_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

        # character_info_title
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ganghwa_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 670, 400, 730, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_btn : 1차 튜토 끝", imgs_)
            why = str(v_.this_game) + " 1차 튜토 끝"
            print(why)
            line_to_me(v_.now_cla, why)

            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
            file_path = dir_path + "\\start.txt"
            # cla.txt
            cla_data = str(v_.now_cla) + "cla"
            file_path2 = dir_path + "\\" + cla_data + ".txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = v_.now_cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)

    except Exception as e:
        print(e)

