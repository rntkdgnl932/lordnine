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
        print("potion_check")

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
                print("절전 : 숫자 안 보여")

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
                    print("아웃 : 숫자 안 보여")

                    v_.potion_buy_count += 1
                    if v_.potion_buy_count > 4:
                        v_.potion_buy_count = 0
                        potion_buy_start(cla)

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

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import juljun_off, juljun_check, go_maul, move_check
    from boonhae_collection import col_boon_start
    from schedule import myQuest_play_check, myQuest_play_add

    try:
        print("potion_buy_start")

        if v_.onCollection == True:

            result_schedule = myQuest_play_check(cla, "check")
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성":
                myQuest_play_add(cla, result_schedule_)

        go_maul(cla)

        buy_potion = False
        buy_potion_count = 0

        while buy_potion is False:
            buy_potion_count += 1
            if buy_potion_count > 7:
                buy_potion = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\title_jabhwa_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 150, 80, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("title_jabhwa_1", imgs_)

                buy_potion = True

                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\enough_item.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 100, 660, 150, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("enough_item", imgs_)
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

                col_boon_start(cla)

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
                        imgs_ = imgs_set_(0, 30, 150, 80, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            break
                    time.sleep(0.3)
            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0
