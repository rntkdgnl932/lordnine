import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, where):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import juljun_check, juljun_attack_check, attack_on, juljun_time_check
    from potion_lordnine import potion_check
    from dead_die import dead_check, dead_recorvery
    from schedule import myQuest_play_add

    try:
        print("dungeon_start")



        # 던전_어둠의숲_3

        result_spot = where.split("_")

        # 검은실험실
        # if result_spot[1] == "검은실험실":
        #     myQuest_play_add(cla, where)
        # else:
        # result_spot[1] => 던전종류
        # resut_spot[2] => 층수
        if result_spot[1] == "검은실험실":
            dun_name = "black"
        elif result_spot[1] == "어둠의숲":
            dun_name = "adoom"
        elif result_spot[1] == "조각의숲": # 던전 없어짐...
            dun_name = "jogag"
        elif result_spot[1] == "타락한미궁":
            dun_name = "talag"
        elif result_spot[1] == "가르바나지하수로":
            dun_name = "garbana"
        elif result_spot[1] == "이벤트": # 눈꽃정원
            dun_name = "event"
        elif result_spot[1] == "수련의전당":
            dun_name = "soolyun"

        if result_spot[1] == "조각의숲":
            myQuest_play_add(cla, where)
        else:
            result_juljun = juljun_check(cla)

            if result_juljun == True:

                juljun_time_check(cla)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\juljun_map\\" + str(dun_name) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 850, 300, 950, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    result_juljun_attack = juljun_attack_check(cla)
                    if result_juljun_attack == True:
                        potion_check(cla)
                    else:
                        if str(dun_name) == "soolyun":
                            potion_check(cla)
                        else:
                            if dun_name == "garbana":
                                garbana_move(cla)
                            attack_on(cla)
                else:
                    dun_in(cla, where)
            else:
                result_dead = dead_check(cla)
                if result_dead == True:
                    dead_recorvery(cla)
                dun_in(cla, where)

    except Exception as e:
        print(e)
        return 0


def dun_in(cla, where):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, out_check, loading_check, attack_on, juljun_on
    from potion_lordnine import potion_buy_start

    from schedule import myQuest_play_add

    try:
        print("dun_in", where)

        # 이벤트 던전 여부
        event_dungeon = False

        y_e_plus = 0
        if event_dungeon == True:
            y_e_plus = 120


        # 검은 실험실 이벤트 여부
        black_laboratory = True

        # 던전_어둠의숲_3

        result_spot = where.split("_")

        # result_spot[1] => 던전종류
        # resut_spot[2] => 층수
        if result_spot[1] == "검은실험실":
            if black_laboratory == True:
                y_1 = 160 + y_e_plus
            else:
                y_1 = 590 + y_e_plus
            dun_name = "black"
        elif result_spot[1] == "어둠의숲":
            if black_laboratory == True:
                y_1 = 390 + y_e_plus
            else:
                y_1 = 280 + y_e_plus
            dun_name = "adoom"

        elif result_spot[1] == "타락한미궁":
            if black_laboratory == True:
                y_1 = 510 + y_e_plus
            else:
                y_1 = 400 + y_e_plus
            dun_name = "talag"
        elif result_spot[1] == "가르바나지하수로":
            if black_laboratory == True:
                y_1 = 280 + y_e_plus
            else:
                y_1 = 170 + y_e_plus
            dun_name = "garbana"

        elif result_spot[1] == "이벤트":
            y_1 = 170
            dun_name = "event"

        elif result_spot[1] == "수련의전당":
            if black_laboratory == True:
                y_1 = 620 + y_e_plus
            else:
                y_1 = 520

            dun_name = "soolyun"

        # 던전 가기전 물약 사자
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("던전 고르는 중")
        else:
            potion_buy_start(cla)


        QTest.qWait(500)

        dun = False
        dun_count = 0
        print("dun True??? False???", dun)

        while dun is False:
            dun_count += 1
            if dun_count > 7:
                dun = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("dungeon", imgs_)

                dun = True

                complete = False

                y_plus = 0

                if event_dungeon == True:
                    y_plus = 115

                # 만료여부
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_complete_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                if str(dun_name) == "black":
                    if black_laboratory == True:
                        imgs_ = imgs_set_(205, 175 + y_plus, 255, 200 + y_plus, cla, img, 0.8)
                    else:
                        if event_dungeon == True:
                            imgs_ = imgs_set_(205, 715 + y_plus, 255, 745 + y_plus, cla, img, 0.8)
                        else:
                            imgs_ = imgs_set_(205, 600 + y_plus, 255, 630 + y_plus, cla, img, 0.8)

                elif str(dun_name) == "garbana":
                    if black_laboratory == True:
                        imgs_ = imgs_set_(205, 290 + y_plus, 255, 315 + y_plus, cla, img, 0.8)
                    else:
                        if event_dungeon == True:
                            imgs_ = imgs_set_(205, 175 + y_plus, 255, 200 + y_plus, cla, img, 0.8)
                        else:
                            imgs_ = imgs_set_(205, 175, 255, 200, cla, img, 0.8)

                elif str(dun_name) == "adoom":
                    if black_laboratory == True:
                        imgs_ = imgs_set_(205, 405 + y_plus, 255, 430 + y_plus, cla, img, 0.8)
                    else:
                        if event_dungeon == True:
                            imgs_ = imgs_set_(205, 290 + y_plus, 255, 315 + y_plus, cla, img, 0.8)
                        else:
                            imgs_ = imgs_set_(205, 290, 255, 315, cla, img, 0.8)

                elif str(dun_name) == "talag":
                    if black_laboratory == True:
                        imgs_ = imgs_set_(205, 520 + y_plus, 255, 545 + y_plus, cla, img, 0.8)
                    else:
                        if event_dungeon == True:
                            imgs_ = imgs_set_(205, 405 + y_plus, 255, 430 + y_plus, cla, img, 0.8)
                        else:
                            imgs_ = imgs_set_(205, 405, 255, 430, cla, img, 0.8)

                elif str(dun_name) == "soolyun":
                    if black_laboratory == True:
                        imgs_ = imgs_set_(205, 635, 255, 660, cla, img, 0.8)
                    else:
                        if event_dungeon == True:
                            imgs_ = imgs_set_(205, 520 + y_plus, 255, 545 + y_plus, cla, img, 0.8)
                        else:
                            imgs_ = imgs_set_(205, 520, 255, 545, cla, img, 0.8)



                elif str(dun_name) == "event":
                    imgs_ = imgs_set_(205, 175, 255, 205, cla, img, 0.8)



                if imgs_ is not None and imgs_ != False:
                    print("dun_complete_1", imgs_)

                    if str(dun_name) == "event":
                        complete = True

                    else:

                        # 만료여부
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_complete_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        if str(dun_name) == "black":
                            if black_laboratory == True:
                                imgs_ = imgs_set_(205, 195 + y_plus, 255, 225 + y_plus, cla, img, 0.8)
                            else:
                                if event_dungeon == True:
                                    imgs_ = imgs_set_(205, 620 + y_plus, 255, 650 + y_plus, cla, img, 0.8)
                                else:
                                    imgs_ = imgs_set_(205, 620, 255, 650, cla, img, 0.8)

                        elif str(dun_name) == "garbana":
                            if black_laboratory == True:
                                imgs_ = imgs_set_(205, 310 + y_plus, 255, 335 + y_plus, cla, img, 0.8)
                            else:
                                if event_dungeon == True:
                                    imgs_ = imgs_set_(205, 195 + y_plus, 255, 225 + y_plus, cla, img, 0.8)
                                else:
                                    imgs_ = imgs_set_(205, 195, 255, 220, cla, img, 0.8)

                        elif str(dun_name) == "adoom":
                            if black_laboratory == True:
                                imgs_ = imgs_set_(205, 425 + y_plus, 255, 450 + y_plus, cla, img, 0.8)
                            else:
                                if event_dungeon == True:
                                    imgs_ = imgs_set_(205, 310 + y_plus, 255, 335 + y_plus, cla, img, 0.8)
                                else:
                                    imgs_ = imgs_set_(205, 310, 255, 335, cla, img, 0.8)

                        elif str(dun_name) == "talag":
                            if black_laboratory == True:
                                imgs_ = imgs_set_(205, 540 + y_plus, 255, 570 + y_plus, cla, img, 0.8)
                            else:
                                if event_dungeon == True:
                                    imgs_ = imgs_set_(205, 425 + y_plus, 255, 450 + y_plus, cla, img, 0.8)
                                else:
                                    imgs_ = imgs_set_(205, 425, 255, 450, cla, img, 0.8)
                        elif str(dun_name) == "soolyun":
                            if black_laboratory == True:
                                imgs_ = imgs_set_(205, 655, 255, 685, cla, img, 0.8)
                            else:
                                if event_dungeon == True:
                                    imgs_ = imgs_set_(205, 540 + y_plus, 255, 565 + y_plus, cla, img, 0.8)
                                else:
                                    imgs_ = imgs_set_(205, 540, 255, 565, cla, img, 0.8)





                        if imgs_ is not None and imgs_ != False:
                            print("dun_complete_2", imgs_)

                            complete = True



                if complete == True:

                    myQuest_play_add(cla, where)

                else:


                    # 던전 클릭
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_ready_check\\" + str(dun_name) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 70, 800, 110, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            if result_spot[1] == "가르바나지하수로":
                                int_step = int(result_spot[2])
                                if int_step > 2:
                                    x_1 = 3
                                else:
                                    x_1 = int_step

                                step_select(cla, x_1)

                            elif result_spot[1] == "검은실험실":

                                if int_step > 5:
                                    x_1 = 6
                                else:
                                    x_1 = int_step

                                step_select(cla, x_1)

                            elif result_spot[1] == "수련의전당":

                                if int_step > 4:
                                    x_1 = 5
                                else:
                                    x_1 = int_step

                                step_select(cla, x_1)


                            else:
                                step_select(cla, result_spot[2])



                            break
                        else:
                            click_pos_2(150, y_1, cla)
                        time.sleep(0.5)

                    # 던전 입장
                    is_out = False
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("dungeon", imgs_)
                            click_pos_2(805, 1005, cla)
                        else:
                            for o in range(10):
                                result_out = out_check(cla)
                                if result_out == True:
                                    is_out = True

                                    break
                                else:
                                    loading_check(cla)
                                time.sleep(0.5)
                        if is_out == True:
                            for o in range(3):
                                result_loading = loading_check(cla)
                                if result_loading == True:
                                    break
                                time.sleep(0.2)
                            break
                        time.sleep(0.5)
                    # 던전 입장 후

                    # 가르바나 지하수로 일 경우 지도 체크 후 공격
                    if str(dun_name) == "garbana":
                        garbana_move(cla)
                    attack_on(cla)
                    time.sleep(0.2)
                    juljun_on(cla)


                    # for i in range(5):
                    #     result_out = out_check(cla)
                    #     if result_out == True:
                    #         # 공격하고 절전모드 ㄱㄱ
                    #         attack_on(cla)
                    #         time.sleep(0.2)
                    #         juljun_on(cla)
                    #
                    #         break
                    #     else:
                    #         loading_check(cla)
                    #     time.sleep(0.5)

            else:
                menu_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\menu_dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 190, 750, 290, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_dungeon", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)
            QTest.qWait(500)
            # time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def step_select(cla, x_1):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, drag_pos

    try:
        print("step_select", x_1)

        x_click = False
        x_click_count = 0

        while x_click is False:
            x_click_count += 1
            if x_click_count > 2:
                x_click = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_step\\top\\" + str(x_1) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 70, 700, 110, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("오케이~~~~~~~~~~~", imgs_)
                x_click = True

            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_step\\bottom\\clicked\\" + str(
                    x_1) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(340, 740, 900, 850, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("clicked : x_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_step\\bottom\\not_clicked\\" + str(
                        x_1) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 740, 900, 850, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("not clicked : x_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    else:
                        if x_click_count > 0:
                            x_click_count -= 1
                        if int(x_1) > 3:
                            print("left drag")
                            drag_pos(630, 810, 300, 810, cla)
                            time.sleep(0.2)
                        else:
                            print("right drag")
                            drag_pos(630, 810, 840, 810, cla)
                            time.sleep(0.2)
            time.sleep(0.3)




    except Exception as e:
        print(e)
        return 0


def garbana_move(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, move_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("garbana_move")

        x_click = False
        x_click_count = 0

        while x_click is False:
            x_click_count += 1
            if x_click_count > 10:
                x_click = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 570, 550, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("move_check : ok")
                x_click = True
            else:

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap", imgs_)
                    click_pos_2(380, 555, cla)
                    time.sleep(0.5)
                    click_pos_2(400, 560, cla)
                    time.sleep(0.5)
                    click_pos_2(390, 565, cla)
                    time.sleep(0.5)
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("worldmap", imgs_)
                            click_pos_2(925, 50, cla)
                        else:
                            break
                        time.sleep(1)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\maul\\map.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(185, 100, 220, 130, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("map", imgs_)
                        click_pos_reg(imgs_.x - 50, imgs_.y + 50, cla)
                    else:

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\maul\\party_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 140, 160, 240, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("party_1", imgs_)
                            click_pos_2(35, 125, cla)
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\maul\\party_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 140, 160, 240, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("party_2", imgs_)
                                click_pos_2(35, 125, cla)
                            else:
                                clean_screen_start(cla)
                                click_pos_2(35, 125, cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0