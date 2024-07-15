import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla, where):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import juljun_check
    from potion_lordnine import potion_check

    try:
        print("jadong_start", where)

        result_where = spot_get(where)

        # 디엔북부/메마른호숫가_1_1_1

        result_spot = result_where.split("_")

        result_juljun = juljun_check(cla)

        if result_juljun == True:




            # result_spot[1] => 큰 맵
            # result_spot[2] => 중간 맵 // 200 235 270 ...
            # result_spot[3] => 세부 맵

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\juljun_spot\\" + str(result_spot[1]) + "\\" + str(result_spot[2]) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 890, 130, 940, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("juljun big_map", result_spot[1], imgs_)

                potion_check(cla)

            else:


                spot_in(cla, result_where)
        else:
            spot_in(cla, result_where)


    except Exception as e:
        print(e)
        return 0


def spot_in_ready(cla, where):
    import numpy as np
    import cv2
    import random

    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_for
    from action_lordnine import go_maul, out_check, loading_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("spot_in_ready", where)

        # 디엔북부/메마른호숫가_1_1_1

        result_spot = where.split("_")

        # result_spot[1] => 큰 맵
        y_1 = 85 + (int(result_spot[1]) * 45)
        # result_spot[2] => 중간 맵 // 200 235 270 ...
        y_2 = 165 + (int(result_spot[2]) * 35)
        # result_spot[3] => 세부 맵맵
        y_3 = 95 + (int(result_spot[3]) * 36)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
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
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)



                # 자세히 들어가기
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\big_map\\" + str(result_spot[1]) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 100, 120, 150, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("big_map", result_spot[1], imgs_)

                        click_pos_2(100, y_2, cla)
                        time.sleep(0.2)
                        click_pos_2(100, y_2, cla)
                        time.sleep(0.2)

                        for m in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_move_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.7)
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
                                    time.sleep(0.2)

                                for s in range(5):
                                    result_out_check= out_check(cla)
                                    if result_out_check == True:
                                        break
                                    time.sleep(0.5)
                                break


                            else:
                                for o in range(5):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\hunt_move_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.7)
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
                            imgs_ = imgs_set_(20, 100, 120, 150, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
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
                        imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

                else:
                    clean_screen_start(cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def spot_in(cla, where):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import go_maul, out_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("spot_in", where)

        # 디엔북부/메마른호숫가_1_1_1

        result_spot = where.split("_")

        # result_spot[1] => 큰 맵
        y_1 = 85 + (int(result_spot[1]) * 45)
        # result_spot[2] => 중간 맵 // 200 235 270 ...
        y_2 = 165 + (int(result_spot[2]) * 35)
        # result_spot[3] => 세부 맵맵
        y_3 = 95 + (int(result_spot[3]) * 36)

        spot_in_ready(cla, where)


        world = False
        world_count = 0

        while world is False:
            world_count += 1
            if world_count > 6:
                world = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\worldmap.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("worldmap", imgs_)



                # 자세히 들어가기
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\big_map\\" + str(result_spot[1]) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 100, 120, 150, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("big_map", result_spot[1], imgs_)

                        click_pos_2(100, y_2, cla)
                        time.sleep(0.2)
                        click_pos_2(100, y_2, cla)
                        time.sleep(0.2)

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
                            imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.7)
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
                                    imgs_ = imgs_set_(500, 70, 640, 110, cla, img, 0.7)
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
                                    imgs_ = imgs_set_(750, 60, 860, 110, cla, img, 0.7)
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
                            imgs_ = imgs_set_(20, 100, 120, 150, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
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
                        imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

                else:
                    clean_screen_start(cla)
            time.sleep(0.5)


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
        imgs_ = imgs_set_(500, 70, 640, 110, cla, img, 0.7)
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
                imgs_ = imgs_set_(480, 540, 640, 600, cla, img, 0.7)
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
                move_check(cla)
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
        print("all_list", all_list)


        for i in range(len(all_list)):
            result_list_ready = all_list[i].split("_")
            if result_list_ready[0] == where:
                result_list = all_list[i]
                break

        print("result_list", result_list)



        return result_list
    except Exception as e:
        print(e)
        return 0