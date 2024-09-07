import random
import time
# import os
import sys
from PyQt5.QtTest import *


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def mission_get(cla, data):
    import numpy as np
    import cv2
    from datetime import datetime

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from potion_lordnine import potion_check
    from action_lordnine import juljun_check, out_check, zero_check_minute, juljun_attack_check
    from dead_die import dead_check
    from tuto_lordnine import way_check
    from boonhae_collection import col_boon_start

    try:
        print("mission_get", data)

        dead_check(cla)


        if v_.daily_mission_ready == True:

            print("v_.daily_mission_ready", v_.daily_mission_ready)

            mission_get_week(cla)
            v_.daily_mission_ready = False
        else:
            result_juljun = juljun_check(cla)
            if result_juljun == True:

                zero = zero_check_minute(cla)

                if zero == True:
                    # 가방 체크...10분 마다
                    mission_get_daily(cla, data)

                else:
                    nowMinute = int(datetime.today().strftime("%M"))
                    print("nowMinute", nowMinute)
                    result_m = nowMinute % 10
                    print("result_m", result_m)

                    if result_m == 0:
                        # 가방 체크...10분 마다
                        mission_get_daily(cla, data)
                    else:
                        result_attack_check = juljun_attack_check(cla)
                        if result_attack_check == False:

                            is_action = False

                            for i in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_attack_on.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    is_action = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_move_on.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        is_action = True
                                        break
                                time.sleep(1)

                            if is_action == False:
                                mission_get_daily(cla, data)
                            else:
                                potion_check(cla)
                        else:
                            potion_check(cla)

            else:

                result_out = out_check(cla)

                if result_out == True:

                    for i in range(3):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\out_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(840, 100, 900, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_complete", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                way_check(cla)


                # 미션 얻고 공격까지하고, 미션 얻다가 더이상 실행할 수 있는 것이 없으면 add
                mission_get_daily(cla, data)


    except Exception as e:
        print(e)
        return 0


def mission_get_daily(cla, data):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import menu_open, confirm_all, loading_check, move_check, juljun_on
    from clean_screen_lordnine import clean_screen_start
    from schedule import myQuest_play_add

    try:
        print("mission_get_daily")
        # 일일임무_2_모험



        result_spot = data.split("_")
        y_num = int(result_spot[1])
        # 시간 time_jogag 모험 adventure 우호 friendship
        selected = result_spot[2]
        if result_spot[2] == "시간":
            selected = "time_jogag"
        elif result_spot[2] == "모험":
            selected = "adventure"
        elif result_spot[2] == "우호":
            selected = "friendship"

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("mission", imgs_)

                is_in = False

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\mission_refresh_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 980, 100, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_in = True
                else:
                    for a in range(6):
                        is_ = a + 1
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\list\\" + str(is_) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 100, 750, 140, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("click ok", is_)
                            is_in = True
                            break

                if is_in == True:

                    get = True

                    # 일일 임무를 클릭하기 전 준비
                    for a in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("아직 수락할 수 없다는 글이 보인다.")
                        else:
                            break
                        time.sleep(1)

                    # 일일 임무 해당 장소를 클릭하자
                    # 125, 160, 195...

                    y_click = 90 + (y_num * 35)

                    for a in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\list\\" + str(y_num) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 100, 750, 140, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("click ok")
                            break
                        else:
                            click_pos_2(50, y_click, cla)
                        time.sleep(1)

                    # 일일 임무 완료 보상을 받자

                    for a in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("complete")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 980, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("complete_btn")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for g in range(10):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 390, 550, 450, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:

                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_get.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(540, 560, 650, 650, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            time.sleep(0.5)
                                            result_ran = random.randint(1, 5)
                                            x_get = 315 + (result_ran * 55)
                                            y_get = imgs_.y
                                            # 370, 425, 480, 535, 590
                                            for com in range(5):
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(390, 390, 550, 450, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_2(x_get, y_get, cla)
                                                else:
                                                    break
                                                time.sleep(0.5)
                                            break
                                    time.sleep(0.5)
                        else:
                            break
                        time.sleep(1)

                    # 임무를 더 받을지...
                    again = False

                    # 일일 임무를 얻쟈
                    for i in range(40):

                        anymore = False

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 100, 620, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            y_reg = imgs_.y
                        else:
                            y_reg = 800

                        is_selected = False

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\time_jogag.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(180, 100, 350, y_reg, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            is_selected = True
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\adventure.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(180, 100, 350, y_reg, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                is_selected = True
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\friendship.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(180, 100, 350, y_reg, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    is_selected = True

                        if is_selected == True:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_soolock_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(810, 980, 950, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for a in range(5):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        anymore = True
                                        break
                                    time.sleep(0.1)
                        else:
                            for c in range(10):
                                result_confirm = confirm_all(cla)
                                if result_confirm == True:
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\mission_refresh_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 980, 100, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        # 갱신이 끝났으면 바로 전 단계에서 하기
                                        # 바로 전단계가 없으면 시간증서 또는 우호증서 받아서 하기
                                        # 이 마저도 없으면 아무거나 받기
                                        print("모두 끝...")
                                        again = True
                                        anymore = True
                                        break
                                time.sleep(0.5)

                        if anymore == True:
                            break

                        time.sleep(0.2)
                    if again == True:
                        print("아무거나 받기")

                        for a in range(20):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_soolock_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(810, 980, 950, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.3)

                    # 진행중이 있으면 임무 수행...없으면 add

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\ing.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        for att in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:


                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\soongan_move_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(710, 980, 810, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                    for con in range(5):
                                        result_move_confirm = confirm_all(cla)
                                        if result_move_confirm == True:
                                            break
                                        time.sleep(0.1)


                                    for load in range(5):
                                        loading_check(cla)
                                        time.sleep(0.2)

                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\ing.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.2)
                                    else:
                                        loading_check(cla)
                            else:
                                break
                            time.sleep(0.5)
                        # 나간 후
                        attacked = False
                        attacked_count = 0

                        while attacked is False:
                            attacked_count += 1
                            if attacked_count > 12:
                                attacked = True
                                click_pos_2(870, 850, cla)
                                time.sleep(0.5)
                                juljun_on(cla)

                            result_move = move_check(cla)
                            if result_move == False:
                                attacked_count += 1
                                result_loading = loading_check(cla)
                                if result_loading == False:
                                    attacked_count += 1
                            time.sleep(0.5)

                    else:
                        print("?????????????????????????????????")
                        myQuest_play_add(cla, data)
                        clean_screen_start(cla)

                else:
                    click_pos_2(48, 88, cla)

            else:

                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\menu_mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 140, 870, 220, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



def mission_get_week(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import menu_open, confirm_all

    try:
        print("mission_get_week")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("mission", imgs_)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\week_mission.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 100, 50, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("week_mission", imgs_)
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\week_mission2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 950, 920, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("week_mission2", imgs_)

                        get = True


                        # 주간 임무를 클릭하기 전 준비
                        for a in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("아직 수락할 수 없다는 글이 보인다.")
                            else:
                                break
                            time.sleep(1)

                        # 주간 임무 완료 보상을 받자

                        for a in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("complete")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 980, 960, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("complete_btn")
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    for g in range(10):
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(390, 390, 550, 450, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:

                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_get.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(540, 560, 650, 650, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                time.sleep(0.5)
                                                result_ran = random.randint(1, 5)
                                                x_get = 315 + (result_ran * 55)
                                                y_get = imgs_.y
                                                # 370, 425, 480, 535, 590
                                                for com in range(5):
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\complete_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(390, 390, 550, 450, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_2(x_get, y_get, cla)
                                                    else:
                                                        break
                                                    time.sleep(0.5)
                                                break
                                        time.sleep(0.5)
                            else:
                                break
                            time.sleep(1)

                        # 주간 임무를 얻자
                        for w in range(6):

                            anymore = False

                            clicked = False

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\ing.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("ing", imgs_)
                                y_reg = imgs_.y - 20
                            else:
                                y_reg = 700

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\gamjung_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_for = imgs_set_for(170, 100, 400, y_reg - 20, cla, img, 0.9)
                            if imgs_for is not None and imgs_for != False:
                                print("gamjung_1", imgs_for)
                                if len(imgs_for) > 0:
                                    for i in range(len(imgs_for)):
                                        click_pos_reg(imgs_for[i][0], imgs_for[i][1], cla)
                                        time.sleep(0.5)
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\gamjung_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(600, 60, 700, 110, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("gamjung_2", imgs_)
                                            clicked = True
                                            break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_misson.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(170, 100, 400, y_reg, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("daily_misson", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        clicked = True
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\guild_donation.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(170, 100, 400, y_reg, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("guild_donation", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            clicked = True
                            if clicked == True:
                                time.sleep(0.5)
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_soolock_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(810, 980, 950, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for a in range(5):
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            anymore = True
                                            break
                                        time.sleep(0.1)

                            if anymore == True:
                                break
                            QTest.qWait(500)

                        # 나가자
                        # clean_screen_start(cla)
                    else:
                        click_pos_2(148, 88, cla)

                else:
                    click_pos_2(148, 88, cla)

            else:

                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\menu_mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 140, 870, 220, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0