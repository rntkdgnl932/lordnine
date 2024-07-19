import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tower_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import attack_on_tower
    from potion_lordnine import potion_check
    from dead_die import dead_check
    from schedule import myQuest_play_add

    try:
        print("guild_start")

        dead_check(cla)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\tower_in.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 100, 180, 160, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\next_level.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 90, 700, 300, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("next_level")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\re_challenge.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 90, 700, 300, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("re_challenge")
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 90, 500, 300, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("exit")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        myQuest_play_add(cla, "시련의탑")
                    time.sleep(1)

            attack_on_tower(cla)

            potion_check(cla)


        else:
            tower_in(cla)



    except Exception as e:
        print(e)
        return 0


def tower_in(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, loading_check, out_check, attack_on
    from dead_die import dead_check
    from boonhae_collection import col_boon_start

    try:
        print("tower_in")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\tower.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("tower", imgs_)



                click_pos_2(845, 1005, cla)

                inven_full = False

                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\inventory_full.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 100, 630, 160, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        col_boon_start(cla)
                        inven_full = True
                        break
                    time.sleep(0.1)

                if inven_full == False:

                    get = True


                    tower_in_start(cla)

                # 마무리 나가기

            else:

                menu_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\tower.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\menu_tower.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 180, 770, 300, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def tower_in_start(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2
    from action_lordnine import loading_check, out_check

    try:
        print("tower_in_start")

        for i in range(10):
            result_loading = loading_check(cla)
            if result_loading == False:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tower\\tower_in.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 100, 180, 160, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
            time.sleep(1)

        for i in range(10):
            result_out = out_check(cla)
            if result_out == True:
                click_pos_2(870, 850, cla)
                time.sleep(0.5)
                break
            time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0