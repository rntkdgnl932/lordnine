import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def confirm_all(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        is_confirm = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\confirm_btn_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 570, 640, 640, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm_btn_1 : 무엇", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        # 소환
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\confirm_btn_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 980, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm_btn_2 : 소환 확인", imgs_)
            x_reg = imgs_.x
            y_reg = imgs_.y

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\sohwan_not_checked.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 980, 40, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.3)

            click_pos_reg(x_reg, y_reg, cla)
            is_confirm = True
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sohwan_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 980, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("sohwan_confirm : 소환 확인", imgs_)
                print("confirm_btn_2 : 소환 확인", imgs_)
                x_reg = imgs_.x
                y_reg = imgs_.y

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\sohwan_not_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 980, 40, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.3)

                click_pos_reg(x_reg, y_reg, cla)
                is_confirm = True
        # 이동
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\move_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(470, 570, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("move_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        # 감정
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\gamjung_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 570, 960, 770, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("gamjung_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        # 포션
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\potion\\potion_buy_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(460, 660, 600, 720, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("potion_buy_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        # 우편
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_get_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(460, 560, 640, 640, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("post_get_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        # 자동사냥 이동
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jadong\\jadong_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 540, 640, 600, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("jadong_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        # 던전 나가기
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\dun_exit_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 540, 640, 640, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("dun_exit_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True

        return is_confirm

    except Exception as e:
        print(e)



def out_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from stop_event18 import game_check
    from character_select_and_game_start import game_start_screen
    from schedule import myQuest_play_check
    try:

        print("out_check 하면서 게임체크도 하기")

        game_check(cla)


        out_screen = False
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            out_screen = True
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                out_screen = True


        if out_screen == True:
            result_schedule = myQuest_play_check(cla, "check")
            character_id = result_schedule[0][1]
            result_schedule_ = result_schedule[0][2]

            game_start_screen(cla, character_id)

        else:
            is_out = False

            result_menu_open = menu_open_check(cla)
            if result_menu_open == False:

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\out\\talk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 940, 60, 990, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    is_out = True

            return is_out

    except Exception as e:
        print(e)




def menu_open_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("menu_open_check")

        is_menu = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("character_change_btn", imgs_)
            is_menu = True

        return is_menu

    except Exception as e:
        print(e)


def menu_open(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from clean_screen_lordnine import clean_screen_start
    from get_item import get_post
    try:

        print("menu_open")

        result_menu_open = menu_open_check(cla)

        menu_open_count = 0
        while result_menu_open is False:
            menu_open_count += 1
            if menu_open_count > 5:
                result_menu_open = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("character_change_btn", imgs_)

                result_menu_open = True

                # 우편물 확인하자

                get_point = False

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(740, 880, 800, 930, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_point_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                    get_point = True
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 880, 800, 930, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_point_2", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                        get_point = True

                if get_point == True:
                    get_post(cla)
                    menu_open_last(cla)
            else:
                clean_screen_start(cla)
                click_pos_2(915, 50, cla)
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)
            time.sleep(0.5)


    except Exception as e:
        print(e)


def menu_open_last(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    from clean_screen_lordnine import clean_screen_start
    from get_item import get_post
    try:

        print("menu_open_last")

        result_menu_open = menu_open_check(cla)

        menu_open_count = 0
        while result_menu_open is False:
            menu_open_count += 1
            if menu_open_count > 5:
                result_menu_open = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("character_change_btn", imgs_)
                result_menu_open = True
            else:
                clean_screen_start(cla)
                click_pos_2(915, 50, cla)
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)
            time.sleep(0.5)


    except Exception as e:
        print(e)

def skip_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from clean_screen_lordnine import clean_screen_just_on_start
    from schedule import myQuest_play_check

    try:

        print("skip_start")

        is_skip = False

        # top
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_skip = True
        else:
            # bottom
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\skip_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 940, 960, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_skip = True
            else:
                # screen_click
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\screen_click_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 600, 700, 1040, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_skip = True
                else:
                    # out_skip(character ready)
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\out_skip.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_skip = True

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("off")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
        # else:
        #
        #     result_schedule = myQuest_play_check(cla, "check")
        #     result_schedule_ = result_schedule[0][2]
        #
        #     if result_schedule_ == "튜토육성":
        #
        #         clean_screen_just_on_start(cla)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\tuto\\quest_check\\on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("on")

            click_pos_2(480, 820, cla)
            time.sleep(0.2)

            is_skip = True

        if is_skip == True:
            time.sleep(0.5)

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\next_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 940, 960, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\exit_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
        # touch me

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("touch_me", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\touch_me.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("touch_me", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_skip

    except Exception as e:
        print(e)



def move_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("move_check")

        is_move = False

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 570, 550, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("move_check : ok")
                is_move = True
                break
            time.sleep(0.2)

        is_move_count = 0
        is_move_second = 0
        while is_move is True:
            is_move_second += 1

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\move\\move_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(440, 570, 550, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("이동중", is_move_second, "초")
                is_move_count = 0

            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\out\\talk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 940, 60, 990, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    is_move_count += 1
                    if is_move_count > 3:
                        is_move = False
                else:
                    result_loading = loading_check(cla)
                    if result_loading == True:
                        is_move_count = 0
                    else:
                        is_move_count += 1
                        if is_move_count > 3:
                            is_move = False

            time.sleep(1)


        return is_move

    except Exception as e:
        print(e)



def loading_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("loading_check")

        is_loading = False

        is_move = False

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\loading\\tip.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 900, 150, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("tip : loading...")
                is_move = True
                is_loading = True
                break
            time.sleep(0.2)

        is_move_count = 0
        is_move_second = 0
        while is_move is True:
            is_move_second += 1

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\loading\\tip.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 900, 150, 1040, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("로딩중", is_move_second, "초")
                is_move_count = 0

            else:
                is_move_count += 1
                if is_move_count > 3:
                    is_move = False

            time.sleep(1)

        return is_loading
    except Exception as e:
        print(e)

def juljun_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("juljun_check")

        is_juljun = False

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on", imgs_)
            is_juljun = True

        return is_juljun
    except Exception as e:
        print(e)
        return 0


def juljun_attack_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("juljun_attack_check")

        is_attack = False

        for i in range(25):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_attack_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("juljun_attack_on", imgs_)
                is_attack = True
                break
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_move_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_move_on", imgs_)
                    for r in range(25):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_attack_on.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_attack_on", imgs_)
                            is_attack = True
                            break
                        time.sleep(0.2)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_rest_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("juljun_rest_on", imgs_)
                        for r in range(25):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\juljun_attack_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 630, 600, 700, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("juljun_attack_on", imgs_)
                                is_attack = True
                                break
                            time.sleep(0.2)
            time.sleep(0.2)

        return is_attack
    except Exception as e:
        print(e)
        return 0



def juljun_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_lordnine import clean_screen_start
    from tuto_lordnine import way_check

    try:
        print("juljun_on")

        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on", imgs_)
                break
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(35, 790, cla)
                    time.sleep(0.5)
                else:
                    clean_screen_start(cla)
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def juljun_off(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, drag_pos
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("juljun_off")

        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                drag_pos(430, 530, 730, 530, cla)

                for o in range(5):
                    result_out = out_check(cla)
                    if result_out == True:
                        break
                    else:
                        time.sleep(0.2)

            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0



def go_maul(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from clean_screen_lordnine import clean_screen_start
    from tuto_lordnine import way_check

    try:
        print("go_maul")



        for i in range(10):
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                juljun_off(cla)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\maul\\jabhwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(730, 770, 810, 850, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa", imgs_)
                    break

                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\maul\\maul.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 90, 100, 140, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("maul", imgs_)
                        result_out = out_check(cla)
                        if result_out == False:
                            clean_screen_start(cla)
                        break
                    else:
                        result_loading = loading_check(cla)
                        if result_loading == False:
                            result_out = out_check(cla)
                            if result_out == True:
                                click_pos_2(30, 205, cla)
                                for c in range(3):
                                    result_loading = loading_check(cla)
                                    if result_loading == False:
                                        confirm_all(cla)
                                    time.sleep(0.2)
                                time.sleep(3)
                            else:
                                clean_screen_start(cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



def bag_open(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from clean_screen_lordnine import clean_screen_start
    from tuto_lordnine import way_check

    try:
        print("bag_open")



        for i in range(10):
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                juljun_off(cla)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\bag\\my_bag.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 80, 830, 130, cla, img, 0.75)
                if imgs_ is not None and imgs_ != False:
                    print("my_bag", imgs_)
                    break
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        click_pos_2(875, 50, cla)
                        for c in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\bag\\my_bag.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 80, 830, 130, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)
                    else:
                        clean_screen_start(cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



def attack_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    try:

        print("attack_on")

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 350, 600, 400, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            juljun_off(cla)

        attack = False

        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\attack\\attack_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 40, 420, 130, cla, img, 0.75)
            if imgs_ is not None and imgs_ != False:
                print("attack on!!", imgs_)
                attack = True
                break
            time.sleep(0.3)

        if attack == False:
            click_pos_2(865, 850, cla)
            time.sleep(0.3)

    except Exception as e:
        print(e)












