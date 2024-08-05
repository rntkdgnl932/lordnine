import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, text_check_get
    from action_lordnine import juljun_check, out_check
    from tuto_lordnine import way_check

    try:
        print("potion_check", v_.potion_buy_count)

        # 우선 절전모드인지 아웃 모드인지 파악하기

        is_num = False

        result_juljun = juljun_check(cla)

        if result_juljun == True:

            x_1 = 870
            y_1 = 1010
            x_2 = 884
            y_2 = 1025

            # text_check_get(x_1, y_1, x_2, y_2, cla)

            for i in range(10):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_num\\small\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_1, y_1, x_2, y_2, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("i", i)
                    is_num = True

                    if v_.potion_buy_count > 0:
                        v_.potion_buy_count -= 1

            if is_num == False:

                for s in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 750, 870, 800, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_setting_title", imgs_)

                        for p in range(3):
                            if p == 0:
                                print("소형")
                            elif p == 1:
                                print("중형")
                            elif p == 2:
                                print("대형")
                            x_1 = 700 + (p * 70)
                            y_1 = 905
                            x_2 = 722 + (p * 70)
                            y_2 = 923

                            # text_check_get(x_1, y_1, x_2, y_2, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_num\\big\\" + str(
                                    i) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(x_1, y_1, x_2, y_2, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("절전 i", i)
                                    is_num = True

                                    if v_.potion_buy_count > 0:
                                        v_.potion_buy_count -= 1
                            if is_num == True:
                                break
                    else:
                        click_pos_2(880, 975, cla)
                        for g in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 750, 870, 800, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.1)
                    if is_num == True:
                        break
                    time.sleep(0.5)


                if is_num == False:

                    print("절전 : 숫자 안 보여", v_.potion_buy_count)




                    v_.potion_buy_count += 1
                    if v_.potion_buy_count > 4:
                        v_.potion_buy_count = 0
                        potion_buy_start(cla)

        else:

            result_out = out_check(cla)
            if result_out == True:

                x_1 = 270
                y_1 = 1006
                x_2 = 285
                y_2 = 1021

                # text_check_get(x_1, y_1, x_2, y_2, cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_num\\small\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_1, y_1, x_2, y_2, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("i", i)
                        is_num = True

                        if v_.potion_buy_count > 0:
                            v_.potion_buy_count -= 1


                if is_num == False:

                    for s in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(190, 750, 370, 800, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_setting_title", imgs_)

                            for p in range(3):
                                if p == 0:
                                    print("소형")
                                elif p == 1:
                                    print("중형")
                                elif p == 2:
                                    print("대형")

                                x_1 = 200 + (p * 70)
                                y_1 = 900
                                x_2 = 217 + (p * 70)
                                y_2 = 920

                                # text_check_get(x_1, y_1, x_2, y_2, cla)

                                for i in range(10):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_num\\big\\" + str(
                                        i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(x_1, y_1, x_2, y_2, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("아웃 i", i)
                                        is_num = True

                                        if v_.potion_buy_count > 0:
                                            v_.potion_buy_count -= 1
                                if is_num == True:
                                    break
                        else:
                            click_pos_2(280, 975, cla)
                            for g in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(190, 750, 370, 800, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.1)

                        if is_num == True:
                            break

                    if is_num == False:
                        print("아웃 : 숫자 안 보여", v_.potion_buy_count)

                        v_.potion_buy_count += 1
                        if v_.potion_buy_count > 4:
                            v_.potion_buy_count = 0
                            potion_buy_start(cla)

            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(190, 750, 370, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("potion_setting_title", imgs_)

                    for p in range(3):
                        if p == 0:
                            print("소형")
                        elif p == 1:
                            print("중형")
                        elif p == 2:
                            print("대형")

                        x_1 = 200 + (p * 70)
                        y_1 = 900
                        x_2 = 217 + (p * 70)
                        y_2 = 920

                        # text_check_get(x_1, y_1, x_2, y_2, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_num\\big\\" + str(
                                i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_1, y_1, x_2, y_2, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("아웃 i", i)
                                is_num = True

                                if v_.potion_buy_count > 0:
                                    v_.potion_buy_count -= 1
                        if is_num == True:
                            break
                else:
                    print("파악 안됨")
                    is_num = True

        return is_num

    except Exception as e:
        print(e)
        return 0


def potion_buy_start(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_lordnine import juljun_off, juljun_check, go_maul, move_check
    from boonhae_collection import col_boon_start
    from schedule import myQuest_play_check, myQuest_play_add
    from clean_screen_lordnine import clean_screen_start
    from massenger import line_to_me

    try:
        print("potion_buy_start")

        if v_.onCollection == True:

            result_schedule = myQuest_play_check(cla, "check")
            result_schedule_ = result_schedule[0][2]

            # if result_schedule_ == "튜토육성":
            #     myQuest_play_add(cla, result_schedule_)
            if "1회" in result_schedule_:
                myQuest_play_add(cla, result_schedule_)

        result_maul = go_maul(cla)
        if result_maul == True:
            col_boon_start(cla)



        buy_potion = False
        buy_potion_count = 0

        while buy_potion is False:
            buy_potion_count += 1
            if buy_potion_count > 7:
                buy_potion = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\title_jabhwa_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 150, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title_jabhwa_1", imgs_)

                buy_potion = True

                # 80% 설정하기
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 330, 540, 400, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(20, 1010, cla)
                    time.sleep(0.5)

                # 설정하기
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 330, 540, 400, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:

                    potion_setting(cla)


                # 구매하기

                anymore = False

                for i in range(7):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 330, 540, 400, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_setting", imgs_)
                        click_pos_2(530, 400, cla)
                        time.sleep(0.5)
                        click_pos_2(550, 700, cla)
                        time.sleep(0.5)

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\enough_item.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 100, 660, 150, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("enough_item", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\anymore_buy_item.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 100, 660, 150, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("anymore_buy_item", imgs_)
                                anymore = True
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_buy_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(460, 660, 600, 720, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("potion_buy_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    break
                                else:
                                    click_pos_2(150, 1005, cla)
                    time.sleep(0.5)

                if anymore == True:
                    why = "물약 살때 오류"
                    line_to_me(cla, why)

                # 나가기
                clean_screen_start(cla)

            else:

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\maul\\jabhwa.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(730, 770, 810, 850, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        move_check(cla)
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\title_jabhwa_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 150, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                    time.sleep(0.3)
            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0


def potion_setting(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_lordnine import juljun_off, juljun_check, go_maul, move_check
    from boonhae_collection import col_boon_start
    from schedule import myQuest_play_check, myQuest_play_add
    from clean_screen_lordnine import clean_screen_start
    from massenger import line_to_me

    try:
        print("potion_setting")

        is_potion = "low"

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\high_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(160, 370, 240, 550, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("high_potion", imgs_)
            is_potion = "high"
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\middle_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(160, 370, 240, 550, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("middle_potion", imgs_)
                is_potion = "middle"

        if is_potion == "high":
            y_cal = 110
        elif is_potion == "middle":
            y_cal = 55
        else:
            y_cal = 0


        click_pos_2(530, 400 + y_cal, cla)
        time.sleep(0.1)
        click_pos_2(530, 400 + y_cal, cla)
        time.sleep(0.5)

        # 드래그
        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\gamjung_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(215, 580, 320, 620, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("감정주문서(귀속)", imgs_)
            else:
                drag_pos(740, 600, 740, 400, cla)
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\100.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(715, 365, 760, 405, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("속도증가주문서", imgs_)
                break
            else:
                click_pos_2(525, 385, cla)
                time.sleep(0.5)
                click_pos_2(615, 385, cla)
                time.sleep(0.5)
            time.sleep(0.3)

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\100.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(715, 420, 760, 455, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("무게증가주문서", imgs_)
                break
            else:
                click_pos_2(525, 440, cla)
                time.sleep(0.5)
                click_pos_2(615, 440, cla)
                time.sleep(0.5)
            time.sleep(0.3)

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\100.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(715, 475, 760, 515, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("회복증가주문서", imgs_)
                break
            else:
                click_pos_2(525, 495, cla)
                time.sleep(0.5)
                click_pos_2(615, 495, cla)
                time.sleep(0.5)
            time.sleep(0.3)



        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\20.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(715, 525, 760, 565, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("순간이동주문서", imgs_)
                break
            else:
                click_pos_2(525, 550, cla)
                time.sleep(0.5)
                click_pos_2(615, 550, cla)
                time.sleep(0.5)
            time.sleep(0.3)



        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\100.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(715, 580, 760, 620, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("감정주문서", imgs_)
                break
            else:
                click_pos_2(525, 605, cla)
                time.sleep(0.5)
                click_pos_2(615, 605, cla)
                time.sleep(0.5)
            time.sleep(0.3)

        # 마무리
        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 330, 540, 400, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(550, 700, cla)
                time.sleep(0.5)
            else:
                break
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0