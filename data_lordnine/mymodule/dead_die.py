import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from schedule import myQuest_play_add, myQuest_play_check
    from clean_screen_lordnine import clean_screen_start
    from potion_lordnine import potion_buy_start
    from action_lordnine import out_check, loading_check, juljun_off

    try:
        print("dead_check...")

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
                time.sleep(0.5)
            #
            # why = "죽었으니 당장 눈으로 확인하라. 10초 준다..."
            # line_to_me(cla, why)
            # time.sleep(10)

            dead = True

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_dead.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 630, 630, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("juljun_dead", imgs_)

                juljun_off(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\boohwal_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 400, 750, 900, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)

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

                dead = True

        if dead == True:
            result_schedule = myQuest_play_check(cla, "dead_check")
            print("result_schedule dead_check", result_schedule)
            result_schedule_ = result_schedule[0][2]

            dead = False
            print("dead???", dead)

            if result_schedule_ == "튜토육성":
                myQuest_play_add(cla, result_schedule_)
            elif "시련의탑" in result_schedule_:
                myQuest_play_add(cla, result_schedule_)

            potion_buy_start(cla)
            clean_screen_start(cla)
            dead_recorvery(cla)

            QTest.qWait(500)

        return dead
    except Exception as e:
        print(e)
        return 0


def dead_recorvery(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_lordnine import clean_screen_just_on_start
    from action_lordnine import out_check, juljun_off
    from massenger import line_to_me
    from schedule import myQuest_play_add, myQuest_play_check

    try:
        print("dead_recorvery")

        for i in range(7):
            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\boohwal_cross_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 50, 260, 120, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    break
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    juljun_off(cla)

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

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\recorvery_time.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 300, 400, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("recorvery_time", imgs_)
                        click_pos_2(110, 410, cla)

                        time.sleep(0.5)

                        click_pos_reg(imgs_.x + 50, imgs_.y + 10, cla)

                        time.sleep(0.5)

                        click_pos_2(110, 410, cla)

                        time.sleep(0.5)

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\recorver_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(90, 430, 260, 490, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)


                    else:

                        result_schedule = myQuest_play_check(cla, "dead_recorvery")
                        print("result_schedule dead_recorvery", result_schedule)
                        result_schedule_ = result_schedule[0][2]

                        if "5회" in result_schedule_:

                            v_.dead_count += 1

                            if v_.dead_count > 4:
                                # if v_.dead_count < 6:
                                v_.dead_count = 0

                                myQuest_play_add(cla, result_schedule_)

                                # dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                                # file_path = dir_path + "\\start.txt"
                                # # cla.txt
                                # cla_data = str(v_.now_cla) + "cla"
                                # file_path2 = dir_path + "\\" + cla_data + ".txt"
                                # with open(file_path, "w", encoding='utf-8-sig') as file:
                                #     data = 'no'
                                #     file.write(str(data))
                                #     time.sleep(0.2)
                                # with open(file_path2, "w", encoding='utf-8-sig') as file:
                                #     data = v_.now_cla
                                #     file.write(str(data))
                                #     time.sleep(0.2)
                                # os.execl(sys.executable, sys.executable, *sys.argv)
                        else:
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
            recorver_item = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\item.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:




                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\dead_zero_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    recorver_item = False
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\dead_zero_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        recorver_item = False

            if recorver_item == False:
                clean_screen_just_on_start(cla)
            else:
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\item.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:

                        end_fix = False
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\dead_zero_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            end_fix = True
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\dead_zero_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                end_fix = True


                        if end_fix == False:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\item.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(165, 90, 240, 130, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("item")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\dead_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(210, 130, 275, 185, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("dead_checked")

                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\recorver_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(90, 430, 260, 490, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)

                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dead_die\\dead_not_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(210, 130, 275, 185, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("dead_checked")
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)

                        else:
                            clean_screen_just_on_start(cla)
                            break
                    time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0

