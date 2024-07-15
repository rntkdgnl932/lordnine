import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("get_start")

        get_event(cla)

        get_battle_pass(cla)
        get_post(cla)
        get_upjuk(cla)
        get_monster_dogam(cla)



    except Exception as e:
        print(e)
        return 0



def get_event(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, out_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_event")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 540, 340, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("event_title", imgs_)

                get = True

                # 아템 얻자자
                get_event_click(cla)



                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 540, 340, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        click_pos_2(715, 55, cla)
                    time.sleep(0.5)
                if get_point == False:
                    get = True
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def get_event_click(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import menu_open, out_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_event_click")

        get = False
        get_count = 0

        while get is False:
            print("get_count...........", get_count)


            is_point = False

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("touch_me", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\monster_close.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(230, 330, 870, 720, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("monster_close", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(190, 325, 240, 740, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_point_1", imgs_)
                click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                is_point = True
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(190, 325, 240, 740, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_point_2", imgs_)
                    click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                    is_point = True
            time.sleep(0.5)

            if is_point == True:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_for = imgs_set_for(245, 380, 880, 760, cla, img, 0.7)
                if imgs_for is not None and imgs_for != False:
                    print("menu_point_1", imgs_for)
                    # click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                    if len(imgs_for) > 0:
                        for i in range(len(imgs_for)):
                            click_pos_reg(imgs_for[i][0] - 30, imgs_for[i][1] + 10, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("touch_me", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\monster_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 330, 870, 720, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("monster_close", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_for = imgs_set_for(245, 380, 880, 760, cla, img, 0.7)
                if imgs_for is not None and imgs_for != False:
                    print("menu_point_1", imgs_for)
                    # click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                    if len(imgs_for) > 0:
                        for i in range(len(imgs_for)):
                            click_pos_reg(imgs_for[i][0] - 30, imgs_for[i][1] + 10, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("touch_me", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\monster_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 330, 870, 720, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("monster_close", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_for = imgs_set_for(245, 380, 880, 760, cla, img, 0.7)
                if imgs_for is not None and imgs_for != False:
                    print("event_point_1", imgs_for)
                    if len(imgs_for) > 0:
                        for i in range(len(imgs_for)):
                            click_pos_reg(imgs_for[i][0] - 30, imgs_for[i][1] + 10, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 560, 640, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("touch_me", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\monster_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(230, 330, 870, 720, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("monster_close", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
            else:
                get_count += 1
                if get_count > 6:
                    get = True

            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


def get_battle_pass(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, out_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_battle_pass")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\battle_pass.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("battle_pass", imgs_)

                get = True

                # 아템 얻자자
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\anymore_battle_pass.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 80, 650, 160, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(660, 475, cla)
                time.sleep(0.4)



                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\battle_pass.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        click_pos_2(675, 50, cla)
                    time.sleep(0.5)
                if get_point == False:
                    get = True
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def get_post(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_post")

        post = False
        post_count = 0

        while post is False:
            post_count += 1
            if post_count > 6:
                post = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("post", imgs_)

                post = True

                # 상단 포인트
                for i in range(10):

                    is_point = False

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 560, 640, 740, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("touch_me", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_get_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 560, 640, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("post_get_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                                is_point = True

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point_2", imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                                    is_point = True

                                else:
                                    break

                    if is_point == True:
                        time.sleep(0.5)

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_write_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 980, 630, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("post_write_btn", imgs_)
                            click_pos_2(490, 1005, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\all_get_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 980, 630, 1030, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("all_get_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                    time.sleep(0.5)

                # 마무리 나가기
                clean_screen_start(cla)

            else:
                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break

                    else:
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
                    time.sleep(0.5)
                if get_point == False:
                    post = True



    except Exception as e:
        print(e)
        return 0


def get_upjuk(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_upjuk")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("upjuk", imgs_)

                get = True

                # 상단 포인트
                for i in range(10):

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 560, 640, 740, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("touch_me", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_get_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 560, 640, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("post_get_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                                time.sleep(0.5)

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\all_complete_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 980, 960, 1030, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("all_complete_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point_2", imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                                    time.sleep(0.5)

                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\all_complete_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(800, 980, 960, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("all_complete_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(0.5)

                                else:
                                    break


                    time.sleep(0.5)

                # 마무리 나가기
                clean_screen_start(cla)

            else:
                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\upjuk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 140, 905, 180, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                            get_point = True
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(860, 140, 905, 180, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                get_point = True
                    time.sleep(0.5)
                if get_point == False:
                    get = True



    except Exception as e:
        print(e)
        return 0


def get_monster_dogam(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, imgs_set_for, click_pos_2
    from action_lordnine import menu_open
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_monster_dogam")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\monster_dogam.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("monster_dogam", imgs_)

                get = True

                # 상단 포인트
                for i in range(10):

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\touch_me.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 560, 640, 740, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("touch_me", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_get_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(460, 560, 640, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("post_get_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 50, 170, 950, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1", imgs_)

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\all_get_btn_monster.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 980, 165, 1040, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("all_get_btn_monster", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 50, 170, 950, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point_2", imgs_)

                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\all_get_btn_monster.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 980, 165, 1040, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("all_get_btn_monster", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                else:
                                    break



                    time.sleep(0.5)

                # 마무리 나가기
                clean_screen_start(cla)

            else:
                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\monster_dogam.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(830, 200, 870, 240, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                            get_point = True
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(830, 200, 870, 240, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                get_point = True
                    time.sleep(0.5)

                if get_point == False:
                    get = True


    except Exception as e:
        print(e)
        return 0
