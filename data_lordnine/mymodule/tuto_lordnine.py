import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def tuto_start(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, imgs_set_, click_pos_reg
    from action_lordnine import skip_start, confirm_all, move_check, juljun_off, loading_check
    from dead_die import dead_check
    from potion_lordnine import potion_check

    try:

        print("tuto_start")

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            juljun_off(cla)

        result_dead = dead_check(cla)

        if result_dead == False:

            # v_.onTutoPotion은 여기서 튜토시 물약체크 용으로 쓴다. 죽으면 아깝기 때문에
            if v_.onTutoPotion == True:
                potion_check(cla)

            result_move = move_check(cla)

            result_quest_ing = quest_ing_check(cla)

            if result_move == False and result_quest_ing == False:

                skip_start(cla)
                way_check(cla)


                y_sub = 0
                if v_.sub_mission == True:
                    v_.sub_mission_count += 1
                    if v_.sub_mission_count > 4:
                        v_.sub_mission = False
                        v_.sub_mission_count = 0
                    else:
                        y_sub = 45

                print("서브", v_.sub_mission, v_.sub_mission_count)

                # 퀘스트 클릭
                click_pos_2(870, 120 + y_sub, cla)
                time.sleep(0.5)
                result_confirm = confirm_all(cla)
                if result_confirm == True:
                    for i in range(25):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\near_aim_description.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 30, 600, 250, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("near_aim_description", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\loading\\tip.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 900, 150, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("tip : loading...")
                                loading_check(cla)
                                break
                        time.sleep(0.2)

                click_pos_2(780, 130 + y_sub, cla)
                time.sleep(0.3)
                result_confirm = confirm_all(cla)
                if result_confirm == True:
                    time.sleep(5)


                is_sub = False

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\quest_click_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("quest_click_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_sub = True
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\quest_click_btn2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_click_btn2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_sub = True

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\question_mark.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("question_mark", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            is_sub = True

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\question_mark2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("question_mark2", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                is_sub = True

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\question_mark3.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("question_mark3", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_sub = True

                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\quest_click_btn3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("quest_click_btn3", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        is_sub = True

                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\quest_click_btn4.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("quest_click_btn4", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            is_sub = True
                                            time.sleep(1)

                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\quest_click_btn3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(200, 150, 850, 850, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("quest_click_btn3", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            is_sub = True
                                        else:
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\sub_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(680, 520, 730, 570, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\sub_ing_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(860, 520, 950, 570, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\exit_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                else:
                                                    is_sub = True

                if is_sub == True:

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\sub_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 520, 730, 570, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("sub_btn", imgs_)
                            v_.sub_mission = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            skip_start(cla)


                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\sub_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 650, 570, 690, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("sub_confirm", imgs_)
                                break
                        time.sleep(0.2)
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\sub_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 650, 570, 690, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("sub_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            skip_start(cla)
                            break
                        time.sleep(0.2)


                quest_checking(cla)




    except Exception as e:
        print(e)

def quest_ing_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, int_put_, change_number
    from clean_screen_lordnine import clean_screen_just_on_start
    from action_lordnine import skip_start

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
                        clean_screen_just_on_start(cla)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("on")
            click_pos_2(480, 820, cla)
            time.sleep(0.2)
            skip_start(cla)


        return is_q

    except Exception as e:
        print(e)

def way_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg

    try:

        print("way_check")

        for i in range(10):

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
    from massenger import line_to_me
    from clean_screen_lordnine import clean_screen_just_on_start

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
        imgs_ = imgs_set_(60, 90, 170, 130, cla, img, 0.85)
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

        # 어빌리티
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\ability.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 150, cla, img, 0.85)
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

        # 제작
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\jejak.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 170, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jejak", imgs_)

            for i in range(5):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\jejak_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(140, 60, 220, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jejak_1", imgs_)
                    click_pos_2(865, 1005, cla)
                    break
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\jejak_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 60, 220, 140, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jejak_2", imgs_)
                        click_pos_2(865, 1005, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\jejak_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(140, 60, 220, 140, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jejak_3", imgs_)
                            click_pos_2(865, 1005, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\jejak_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(140, 60, 220, 140, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("jejak_4", imgs_)
                                click_pos_2(865, 1005, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\jejak_5.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(140, 60, 220, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("jejak_5", imgs_)
                                    click_pos_2(865, 1005, cla)
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_checking\\jejak_6.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(140, 60, 220, 140, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jejak_5", imgs_)
                                        click_pos_2(865, 1005, cla)
                                        break


                time.sleep(0.5)
            for i in range(5):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\touch_me.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("touch_me", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    clean_screen_just_on_start(cla)
                    break

                time.sleep(0.2)


        # tuto 임시 정지

        # character_info_title

        pause = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\ganghwa_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 670, 400, 730, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("ganghwa_btn : 1차 튜토 끝", imgs_)
            why = str(v_.this_game) + " 강화로 인한 튜토 잠시 정지"
            pause = True
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\ability.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 150, 30, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("ability : 1차 튜토 끝", imgs_)
                # why = str(v_.this_game) + " 직업 고르기 위한..."
                # pause = True

        if pause == True:
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

