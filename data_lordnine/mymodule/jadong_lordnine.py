import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla, where):
    import numpy as np
    import cv2
    from datetime import datetime

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import juljun_check, juljun_attack_check, attack_on, juljun_on, zero_check_hour, juljun_time_check
    from potion_lordnine import potion_check
    from dead_die import dead_check, dead_recorvery
    from boonhae_collection import col_boon_start

    try:
        print("jadong_start", where)



        result_where = spot_get(where)

        # 디엔북부/메마른호숫가_1_1_1
        # 특수/티리오사무덤/지하1층_3_3_0

        # 특수/티리오사무덤/지하1층_3_3_0

        # result_special = result_where.split("/")

        result_spot = result_where.split("_")

        result_special = result_spot[0].split("/")

        result_juljun = juljun_check(cla)

        if result_juljun == True:

            juljun_time_check(cla)


            zero = zero_check_hour(cla)


            if zero == True:
                # 가방 체크...한시간 마다
                col_boon_start(cla)
                juljun_on(cla)

            else:
                nowHour = int(datetime.today().strftime("%H"))
                nowMinute = int(datetime.today().strftime("%M"))
                print("nowMinute", nowMinute)

                if nowMinute == 0:
                    if nowHour % 2 == 1:
                        col_boon_start(cla)
                        juljun_on(cla)
                else:
                    if result_special[0] == "특수":
                        if result_special[1] == "비밀실험실":
                            spot_name = "secret"
                        if result_special[1] == "티리오사무덤":
                            spot_name = "tiriosa"
                        if "죽은자의대지" in result_special[1]:
                            spot_name = "landofdead"


                        print("특수던전", spot_name)

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\juljun_spot\\special\\" + str(spot_name) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 880, 200, 940, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun big_map", result_special[1], imgs_)
                            result_juljun_attack = juljun_attack_check(cla)

                            if result_juljun_attack == True:
                                potion_check(cla)
                            else:
                                attack_on(cla)
                        else:
                            spot_in(cla, result_where)
                    else:

                        # result_spot[1] => 큰 맵
                        # result_spot[2] => 중간 맵 // 200 235 270 ...
                        # result_spot[3] => 세부 맵

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\juljun_spot\\" + str(result_spot[1]) + "\\" + str(result_spot[2]) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 880, 200, 940, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun big_map", result_spot[1], imgs_)
                            result_juljun_attack = juljun_attack_check(cla)

                            if result_juljun_attack == True:
                                result_dead = dead_check(cla)
                                if result_dead == True:
                                    dead_recorvery(cla)
                                potion_check(cla)
                            else:
                                attack_on(cla)
                        else:
                            spot_in(cla, result_where)
        else:
            result_dead = dead_check(cla)
            if result_dead == True:
                dead_recorvery(cla)
            spot_in(cla, result_where)
            QTest.qWait(100)


    except Exception as e:
        print(e)
        return 0


def spot_in_ready(cla, where):
    import numpy as np
    import cv2
    import random
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_for
    from action_lordnine import go_maul, out_check, loading_check, confirm_all, attack_on, juljun_on
    from clean_screen_lordnine import clean_screen_start

    my_item = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\special_btn"
    file_list = os.listdir(my_item)

    try:
        print("spot_in_ready", where)

        is_special = False

        # 디엔북부/메마른호숫가_1_1_1
        # 특수/티리오사무덤/지하1층_3_3_0
        # 특수/죽은자의대지1층_4_2_1

        # result_special = where.split("/")

        result_spot = where.split("_")

        result_special = result_spot[0].split("/")

        # result_spot[1] => 큰 맵
        y_1 = 85 + 40 + (int(result_spot[1]) * 45)
        # result_spot[2] => 중간 맵 // 200 235 270 ...
        y_2 = 165 + 30 + (int(result_spot[2]) * 35)
        # result_spot[3] => 세부 맵맵
        y_3 = 95 + (int(result_spot[3]) * 36)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("worldmap", imgs_)
        else:
            go_maul(cla)


        world = False
        world_count = 0

        while world is False:
            world_count += 1
            if world_count > 6:
                world = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)


                # 자세히 들어가기
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\big_map\\" + str(result_spot[1]) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 130, 120, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("big_map", result_spot[1], imgs_)

                        click_pos_2(100, y_2, cla)
                        time.sleep(0.2)
                        click_pos_2(100, y_2, cla)
                        time.sleep(0.5)

                        print("??????????", result_special[0], result_special[1])

                        if result_special[0] == "특수":
                            # 특수일 경우
                            if result_special[1] == "비밀실험실":
                                spot_name = "secret"
                            if result_special[1] == "티리오사무덤":
                                spot_name = "tiriosa"
                            if "죽은자의대지" in result_special[1]:
                                spot_name = "landofdead"

                            print("spot_name", spot_name)

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\special_list\\" + str(
                                spot_name) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 100, 930, 600, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:

                                world = True

                                for m in range(7):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 540, 640, 600, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_confirm", imgs_)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\special_list\\" + str(
                                            spot_name) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(680, 100, 930, 600, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.2)

                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\82_move_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(800, 980, 920, 1030, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("82_move_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                    time.sleep(0.2)

                                for m in range(7):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 540, 640, 600, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_confirm", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        break

                                    time.sleep(0.2)

                                for s in range(5):
                                    result_loading = loading_check(cla)
                                    if result_loading == True:
                                        break
                                    else:
                                        confirm_all(cla)
                                    time.sleep(0.3)

                                for s in range(5):
                                    result_out_check = out_check(cla)
                                    if result_out_check == True:
                                        break
                                    else:
                                        confirm_all(cla)
                                    time.sleep(0.5)
                                break

                                # 다시 맵 오픈 후 걷기 ㄱㄱ
                            else:
                                for o in range(5):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_move_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:

                                        click_pos_2(935, 90, cla)
                                        time.sleep(0.3)
                                    time.sleep(0.5)

                        else:

                            # 특수가 아닐 경우

                            for m in range(5):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_move_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:

                                    world = True

                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\move_spot_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_for(680, 100, 750, 300, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("move_spot_btn : ", imgs_)
                                        if len(imgs_) > 1:
                                            ran_high_num = len(imgs_)
                                            result_ran = random.randint(1, ran_high_num)
                                            y_reg = imgs_[result_ran - 1][1]


                                            for s in range(7):
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 540, 640, 600, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("jadong_confirm", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break
                                                else:
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\move_spot_btn.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(680, 100, 750, 300, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("move_spot_btn : ", imgs_)
                                                        click_pos_2(750, y_reg, cla)
                                                        time.sleep(0.5)
                                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\soongan_move_btn.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(800, 980, 930, 1040, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.5)

                                        else:
                                            for s in range(7):
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(480, 540, 640, 600, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("jadong_confirm", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break
                                                else:
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\move_spot_btn.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(680, 100, 750, 300, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("move_spot_btn : ", imgs_)
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        time.sleep(0.5)
                                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\soongan_move_btn.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(800, 980, 930, 1040, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.5)

                                    for s in range(5):
                                        result_loading = loading_check(cla)
                                        if result_loading == True:
                                            break
                                        else:
                                            confirm_all(cla)
                                        time.sleep(0.3)

                                    for s in range(5):
                                        result_out_check = out_check(cla)
                                        if result_out_check == True:
                                            break
                                        else:
                                            confirm_all(cla)
                                        time.sleep(0.5)
                                    break


                                else:
                                    for o in range(5):
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_move_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:

                                            click_pos_2(935, 90, cla)
                                            time.sleep(0.3)
                                        time.sleep(0.5)

                                time.sleep(0.5)

                            break

                    else:
                        for o in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\big_map\\" + str(
                                result_spot[1]) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 130, 120, 180, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(15, y_1, cla)
                            time.sleep(0.3)
                    time.sleep(0.5)



            else:
                result_out = out_check(cla)
                if result_out == True:

                    # 피티 확인
                    # 특수/죽은자의대지1층_4_2_1, 특수/죽은자의대지2층_4_2_2
                    if "죽은자의대지" in result_special[1]:

                        result_dethland_step = result_spot[3]

                        is_btn = False
                        for i in range(len(file_list)):
                            result_file_list = file_list[i].split(".")
                            read_data = result_file_list[0]

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\special_btn\\" + str(
                                read_data) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(590, 960, 650, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("item...", str(read_data), imgs_)
                                is_btn = True
                                is_special = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.1)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                        if is_btn == True:
                            for i in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\move_stone_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 320, 630, 360, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.3)
                            for i in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\move_stone_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 320, 630, 360, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:

                                    result_confirm = confirm_all(cla)

                                    if result_confirm == False:
                                        if result_dethland_step == "1":
                                            y_reg_1 = 350
                                            y_reg_2 = 430
                                        elif result_dethland_step == "2":
                                            y_reg_1 = 420
                                            y_reg_2 = 490

                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\unlock_step.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(620, y_reg_1, 670, y_reg_2, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:

                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\unlock_step.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_for(620, y_reg_1, 670, y_reg_2, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                print("unlock_step", imgs_, len(imgs_))

                                                result_ran = random.randint(1, len(imgs_))

                                                click_pos_reg(imgs_[result_ran - 1][0], imgs_[result_ran - 1][1], cla)
                                                time.sleep(0.1)
                                                click_pos_reg(imgs_[result_ran - 1][0], imgs_[result_ran - 1][1], cla)
                                                time.sleep(0.5)
                                                click_pos_2(710, 715, cla)
                                        else:

                                            if result_dethland_step == "1":

                                                for x in range(10):
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\move_stone_title.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(350, 320, 630, 360, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_2(760, 345, cla)
                                                        time.sleep(1)
                                                    else:
                                                        break
                                                    time.sleep(0.3)

                                                click_pos_2(130, 170, cla)
                                                for x in range(10):
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        break
                                                    time.sleep(0.3)
                                            else:
                                                if result_dethland_step == "2":
                                                    y_reg_1 = 350
                                                    y_reg_2 = 430
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\unlock_step.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_for(620, y_reg_1, 670, y_reg_2, cla, img, 0.7)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("unlock_step", imgs_, len(imgs_))

                                                        result_ran = random.randint(1, len(imgs_))

                                                        click_pos_reg(imgs_[result_ran - 1][0],
                                                                      imgs_[result_ran - 1][1], cla)
                                                        time.sleep(0.1)
                                                        click_pos_reg(imgs_[result_ran - 1][0],
                                                                      imgs_[result_ran - 1][1], cla)
                                                        time.sleep(0.5)
                                                        click_pos_2(710, 715, cla)

                                                    for s in range(10):
                                                        result_loading = loading_check(cla)
                                                        if result_loading == True:
                                                            world = True
                                                            break
                                                        else:
                                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.7)
                                                            if imgs_ is not None and imgs_ != False:
                                                                print("jadong_confirm", imgs_)
                                                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                                        time.sleep(0.5)

                                                    for s in range(10):
                                                        result_out_check = out_check(cla)
                                                        if result_out_check == True:
                                                            break
                                                        time.sleep(0.5)

                                                    click_pos_2(130, 170, cla)
                                                    for x in range(10):
                                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                                                        if imgs_ is not None and imgs_ != False:
                                                            break
                                                        time.sleep(0.3)
                                                    # 2층으로 수동 이동해주깅
                                                    dethland_go(cla, result_dethland_step)
                                else:
                                    break
                                time.sleep(0.3)
                            # 후처리
                            for s in range(10):
                                result_loading = loading_check(cla)
                                if result_loading == True:
                                    world = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_confirm", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("dethland_2", imgs_)
                                            break

                                time.sleep(0.5)

                            for s in range(10):
                                result_out_check = out_check(cla)
                                if result_out_check == True:
                                    if result_dethland_step == "2":
                                        # 2층으로 수동 이동해주깅
                                        dethland_go(cla, result_dethland_step)
                                    break
                                time.sleep(0.5)

                            attack_on(cla)

                            juljun_on(cla)
                        else:
                            click_pos_2(130, 170, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.3)
                    else:
                        click_pos_2(130, 170, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)

                else:
                    clean_screen_start(cla)
            time.sleep(0.5)

        return is_special
    except Exception as e:
        print(e)
        return 0


def spot_in(cla, where):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import out_check, loading_check, move_check, attack_on, juljun_on
    from clean_screen_lordnine import clean_screen_start

    try:
        print("spot_in", where)

        # 디엔북부/메마른호숫가_1_1_1
        # 특수/티리오사무덤/지하1층_3_3_0
        # 특수/죽은자의대지/1구역_4_2_0

        # result_special = where.split("/")
        result_spot = where.split("_")
        result_special = result_spot[0].split("/")

        result_dethland_step = result_spot[3]

        # result_spot[1] => 큰 맵 // 170, 215, 260, 305
        y_1 = 85 + 40 + (int(result_spot[1]) * 45)
        # result_spot[2] => 중간 맵 // 225 260 295 ...
        y_2 = 165 + 30 + (int(result_spot[2]) * 35)
        # result_spot[3] => 세부 맵맵
        y_3 = 95 + (int(result_spot[3]) * 36)

        result_special_bloon = spot_in_ready(cla, where)
        # 특수/죽은자의대지_1, 특수/죽은자의대지_2, 특수/죽은자의대지_3...
        if "죽은자의대지" in result_special[1] and result_special_bloon == True:
            print("죽은자의대지 가즈아아아")
        else:
            world = False
            world_count = 0

            while world is False:
                world_count += 1
                if world_count > 6:
                    world = True

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap", imgs_)



                    # 자세히 들어가기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\big_map\\" + str(result_spot[1]) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 130, 120, 180, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("big_map", result_spot[1], imgs_)

                            click_pos_2(100, y_2, cla)
                            time.sleep(0.2)
                            click_pos_2(100, y_2, cla)
                            time.sleep(0.2)



                            if result_special[0] == "특수":
                                # 특수일 경우
                                if result_special[1] == "비밀실험실":
                                    spot_name = "secret"
                                if result_special[1] == "티리오사무덤":
                                    spot_name = "tiriosa"
                                if "죽은자의대지" in result_special[1]:
                                    spot_name = "landofdead"

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\special_map\\" + str(spot_name) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(680, 100, 930, 600, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:

                                    world = True

                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                    for m in range(7):
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("jadong_confirm", imgs_)
                                            break
                                        else:
                                            result_out = out_check(cla)
                                            if result_out == True:
                                                result_move = move_check(cla)
                                                print("여기문제냐", result_move, result_special[1])
                                                if result_move == True:
                                                    print("이동중")
                                                else:
                                                    if "죽은자의대지" in result_special[1]:

                                                        click_pos_2(100, 300, cla)
                                            else:
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\walking_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(700, 980, 920, 1030, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("walking_btn", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    time.sleep(0.2)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    time.sleep(0.2)
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_2(925, 50, cla)



                                        time.sleep(0.5)


                                    # 죽은자의대지는 기다렸다가...
                                    if "죽은자의대지" in result_special[1]:
                                        spot_name = "landofdead"


                                    for m in range(20):
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("jadong_confirm", imgs_)
                                            if "죽은자의대지" in result_special[1]:
                                                time.sleep(5)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                        else:
                                            result_move = move_check(cla)
                                            if result_move == True:
                                                print("이동중")


                                        time.sleep(1)

                                    for s in range(10):
                                        result_loading = loading_check(cla)
                                        if result_loading == True:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.7)
                                            if imgs_ is not None and imgs_ != False:
                                                print("jadong_confirm", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                        time.sleep(0.5)

                                    for s in range(10):
                                        result_out_check = out_check(cla)
                                        if result_out_check == True:
                                            break
                                        time.sleep(0.5)

                                    if result_special[1] == "비밀실험실":
                                        spot_click(cla, spot_name)

                                    # 여기서 죽은자의 대지는 1층 도착한 상태임.
                                    # 그래서 2층과 3층 가는거 한번더 추가해야함.

                                    if "죽은자의대지" in result_special[1]:
                                        if result_dethland_step == "2":
                                            print("2층 가는거 추가")
                                            dethland_go(cla, result_dethland_step)
                                        if result_dethland_step == "3":
                                            print("3층 가는거 추가")

                                    attack_on(cla)

                                    juljun_on(cla)


                                    break


                            else:

                                # 특수가 아닐 경우

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\up.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(850, 100, 930, 1040, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                for m in range(5):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_spot_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:

                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\up.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(850, 100, 930, 1040, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:

                                            click_pos_reg(imgs_.x - 50, imgs_.y + 35, cla)

                                            time.sleep(0.5)

                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\monster_info_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(500, 70, 640, 110, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                world = True

                                                spot_go(cla)

                                                break

                                        else:
                                            click_pos_2(800, y_3, cla)


                                    else:
                                        for o in range(5):
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_spot_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                break
                                            else:

                                                click_pos_2(935, 185, cla)
                                                time.sleep(0.3)
                                            time.sleep(0.5)

                                    time.sleep(0.5)

                                break

                        else:

                            for o in range(5):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\big_map\\" + str(
                                    result_spot[1]) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 130, 120, 180, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                else:
                                    if 0 < int(result_spot[1]) < 5:
                                        click_pos_2(50, 125, cla)
                                        time.sleep(0.5)
                                        click_pos_2(15, y_1, cla)
                                time.sleep(0.3)
                        time.sleep(0.5)



                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        click_pos_2(130, 170, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)

                    else:
                        clean_screen_start(cla)
                time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def dethland_go(cla, data):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import out_check, loading_check, move_check, confirm_all, cancle_all
    from clean_screen_lordnine import clean_screen_start

    try:
        print("spot_in", data)
        world = False
        world_count = 0

        while world is False:
            world_count += 1
            if world_count > 6:
                world = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("dethland_2", imgs_)
                world = True
            else:

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap", imgs_)

                    if data == "2":
                        print("2구역으로 가주아앙")
                        y_reg_1 = 475
                        y_reg_2 = 135

                    click_pos_2(120, y_reg_1, cla)
                    time.sleep(0.5)
                    click_pos_2(120, y_reg_1, cla)
                    time.sleep(0.5)
                    click_pos_2(800, y_reg_2, cla)
                    time.sleep(0.5)
                    click_pos_2(800, y_reg_2, cla)
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\walking_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 980, 920, 1030, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("walking_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(925, 50, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(925, 50, cla)
                        else:
                            result_move = move_check(cla)
                            if result_move == True:
                                print("이동중")
                                world = True
                                break
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("dethland_2", imgs_)
                            break
                        else:
                            loading_check(cla)
                        time.sleep(0.5)

                    # 만약 바로 2층으로 안 넘어갈 경우

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("dethland_2", imgs_)
                    else:
                        time.sleep(3)
                        click_pos_2(100, 500, cla)
                        time.sleep(2)
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("dethland_2", imgs_)
                                break
                            result_confirm = confirm_all(cla)
                            if result_confirm == False:
                                click_pos_2(655, 600, cla)
                            time.sleep(1)
                        for i in range(10):
                            result_loading = loading_check(cla)
                            if result_loading == True:
                                is_loading = True
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("dethland_2", imgs_)
                                    break
                            time.sleep(0.5)
                    # 마지막 도착 점검
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            dethland_random_move(cla)
                            break
                        time.sleep(1)




                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        cancle_all(cla)
                        time.sleep(0.5)
                        click_pos_2(130, 170, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)

                    else:
                        clean_screen_start(cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def spot_click(cla, where):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import out_check, loading_check, move_check, attack_on, juljun_on
    from clean_screen_lordnine import clean_screen_start

    try:
        print("spot_in", where)
        world = False
        world_count = 0

        while world is False:
            world_count += 1
            if world_count > 6:
                world = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)


                click_pos_2(495, 625, cla)
                time.sleep(0.5)
                click_pos_2(495, 625, cla)
                time.sleep(0.5)


                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(925, 50, cla)
                    else:
                        result_move = move_check(cla)
                        if result_move == True:
                            print("이동중")
                            world = True
                            break
                    time.sleep(1)



            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(130, 170, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

                else:
                    clean_screen_start(cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def dethland_random_move(cla):
    import numpy as np
    import cv2
    import random

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import out_check, loading_check, move_check, attack_on, juljun_on
    from clean_screen_lordnine import clean_screen_start

    try:
        print("dethland_random_move")
        # 마지막 랜덤 이동
        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\dethland_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(155, 105, 180, 135, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("dethland_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(2)

                result_random_num = random.randint(1, 4)
                if result_random_num == 1:
                    click_pos_2(410, 435, cla)
                elif result_random_num == 2:
                    click_pos_2(455, 480, cla)
                elif result_random_num == 3:
                    click_pos_2(530, 435, cla)
                elif result_random_num == 4:
                    click_pos_2(530, 480, cla)
                time.sleep(2)
                click_pos_2(930, 55, cla)
                time.sleep(2)
                move_check(cla)

            result_out = out_check(cla)
            if result_out == True:
                break
            QTest.qWait(1000)


    except Exception as e:
        print(e)
        return 0


def spot_go(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import move_check, attack_on, juljun_on
    from clean_screen_lordnine import clean_screen_start

    try:
        print("spot_go")

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\monster_info_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(500, 70, 640, 110, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("monster_info_title", imgs_)

            click_pos_2(635, 460, cla)
            time.sleep(0.1)
            click_pos_2(635, 460, cla)
            time.sleep(0.1)

            is_confirm = False

            for m in range(7):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_confirm", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_confirm = True
                    break
                time.sleep(0.2)

            if is_confirm == False:
                click_pos_2(520, 460, cla)
                time.sleep(0.1)
                clean_screen_start(cla)

        for i in range(10):
            result_move = move_check(cla)
            if result_move == True:
                break
            time.sleep(0.5)

        attack_on(cla)

        juljun_on(cla)

    except Exception as e:
        print(e)
        return 0

def spot_get(where):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("spot_get", where)

        result_list = "none"

        # 디엔북부/메마른호숫가

        # 사냥터
        dir_path = "C:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder)
        file_path1 = dir_path + "\\jadong\\dien.txt"
        file_path2 = dir_path + "\\jadong\\rindlis.txt"
        file_path3 = dir_path + "\\jadong\\woolan.txt"
        file_path4 = dir_path + "\\jadong\\serbis.txt"

        all_list = []

        if os.path.isfile(file_path1) == True:
            with open(file_path1, "r", encoding='utf-8-sig') as file:
                read_serabog = file.read().splitlines()
                for i in range(len(read_serabog)):
                    all_list.append(read_serabog[i])

            with open(file_path2, "r", encoding='utf-8-sig') as file:
                read_baran = file.read().splitlines()
                for i in range(len(read_baran)):
                    all_list.append(read_baran[i])

            with open(file_path3, "r", encoding='utf-8-sig') as file:
                read_countryregioon = file.read().splitlines()
                for i in range(len(read_countryregioon)):
                    all_list.append(read_countryregioon[i])

            with open(file_path4, "r", encoding='utf-8-sig') as file:
                read_yourokina = file.read().splitlines()
                for i in range(len(read_yourokina)):
                    all_list.append(read_yourokina[i])
        # print("all_list", all_list)


        for i in range(len(all_list)):
            result_list_ready = all_list[i].split("_")
            if result_list_ready[0] == where:
                result_list = all_list[i]
                break

        # print("result_list", result_list)



        return result_list
    except Exception as e:
        print(e)
        return 0