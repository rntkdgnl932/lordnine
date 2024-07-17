import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def col_boon_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open
    from tuto_lordnine import way_check

    try:
        print("col_boon_start")

        item_gamjung_start(cla)
        collection_start(cla)
        boonhae_start(cla)




    except Exception as e:
        print(e)
        return 0

def collection_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open
    from clean_screen_lordnine import clean_screen_start
    from tuto_lordnine import way_check

    try:
        print("collection_start")

        collection_count = 0
        collection = False

        while collection is False:
            collection_count += 1
            if collection_count > 7:
                collection = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\item_collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("item_collection", imgs_)

                way_check(cla)

                collection_scan_option(cla)

                for i in range(20):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\col_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        print("col_point_1 : ", imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

                        time.sleep(0.5)
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\col_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(820, 880, 940, 940, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                    else:
                        collection = True
                        clean_screen_start(cla)
                        break
                    time.sleep(0.5)
            else:
                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\item_collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\menu_collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 80, 960, 170, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)




    except Exception as e:
        print(e)
        return 0


def collection_scan_option(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import confirm_all
    from tuto_lordnine import way_check

    try:
        print("collection_scan_option")

        collection_count = 0
        collection = False

        while collection is False:
            collection_count += 1
            if collection_count > 7:
                collection = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("scan_option_title", imgs_)

                check_end = False

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_not_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 450, 240, 510, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(180, 490, 360, 545, cla, img, 0.75)
                    if imgs_ is not None and imgs_ != False:
                        check_end = False
                    else:
                        # 일반만 체크된 상황
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(290, 450, 350, 510, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            # 고급까지 체크인지 확인인
                            if v_.onCollection == True:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 450, 460, 510, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(500, 450, 760, 510, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        check_end = False
                                    else:
                                        check_end = True

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 450, 760, 510, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    check_end = False
                                else:
                                    check_end = True

                if check_end == True:

                    collection = True

                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            confirm_all(cla)
                        else:
                            break
                        time.sleep(0.5)
                else:


                    # 일반체크하기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(290, 450, 350, 510, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(290, 450, 350, 510, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    if v_.onCollection == True:
                        # 고급까지체크하기

                        for i in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 450, 460, 510, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_not_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 450, 460, 510, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        # 나머지 해제하기 1
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 450, 760, 510, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("scan_option_checked : ", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                            time.sleep(0.5)

                    else:
                        # 나머지 해제하기 1
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 450, 760, 510, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("scan_option_checked : ", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                            time.sleep(0.5)

                    # 나머지 해제하기 2
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(180, 490, 360, 545, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("scan_option_checked : ", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\item_collection.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_bottom.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 980, 200, 1040, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0



def item_gamjung_boonhae_ready(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2
    from action_lordnine import bag_open

    try:
        print("item_gamjung_boonhae_ready")

        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                bag_open(cla)
                click_pos_2(800, 1005, cla)
                for n in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.3)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def item_gamjung_start(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action_lordnine import bag_open

    try:
        print("item_gamjung_start")

        item_gamjung_boonhae_ready(cla)

        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\gamjung_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(310, 670, 410, 740, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\gamjung_dajoong.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 490, 410, 560, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(760, 730, cla)

                    is_end = False

                    for s in range(20):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\screen_click_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 600, 700, 1040, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("screen_click_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\gamjung_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 570, 960, 770, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("gamjung_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                # break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\anymore_item.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 100, 600, 160, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    is_end = True
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(365, 710, cla)
                        time.sleep(0.3)

                    if is_end == True:
                        break

                else:
                    click_pos_2(415, 335, cla)
            else:
                click_pos_2(210, 300, cla)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_lordnine import clean_screen_start
    from tuto_lordnine import way_check

    try:
        print("boonhae_start")

        item_gamjung_boonhae_ready(cla)

        # 여기서 한번만 세팅해주자
        boonhae_option(cla)

        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(310, 670, 410, 740, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:



                click_pos_2(760, 730, cla)
                time.sleep(0.1)
                click_pos_2(760, 730, cla)

                time.sleep(1)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_selected.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 500, 500, 600, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    clean_screen_start(cla)
                    break
                else:
                    for s in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\touch_me.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 600, 700, 1040, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            print("touch_me", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(365, 710, cla)
                        time.sleep(0.3)



            else:
                click_pos_2(510, 300, cla)
                for s in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(310, 670, 410, 740, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:

                        break
                    time.sleep(0.5)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0




def boonhae_option(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import confirm_all
    from tuto_lordnine import way_check

    try:
        print("boonhae_option")

        boonhae_option_count = 0
        boonhae_option = False

        while boonhae_option is False:
            boonhae_option_count += 1
            if boonhae_option_count > 7:
                boonhae_option = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_option_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("boonhae_option_title", imgs_)

                check_end = False

                # 귀속체크
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 450, 335, 495, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 515, 350, 600, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        check_end = False
                    else:
                        # 일반만 체크된 상황
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 430, 335, 475, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            # 고급까지 체크인지 확인
                            if v_.onCollection_boonhae == True:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(375, 430, 430, 475, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:

                                    # 체크 되지 않아야 할 부분에 체크 되어있는지 확인
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(450, 430, 640, 475, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        check_end = False
                                    else:
                                        check_end = True

                            else:
                                # 체크 되지 않아야 할 부분에 체크 되어있는지 확인
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(360, 430, 640, 475, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    check_end = False
                                else:
                                    check_end = True


                if check_end == True:

                    boonhae_option = True

                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_setting_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 650, 550, 720, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(0.5)
                else:


                    # 일반체크하기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 430, 335, 475, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 430, 335, 475, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    # 귀속체크하기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 450, 335, 495, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 450, 335, 495, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    if v_.onCollection_boonhae == True:
                        # 고급까지체크하기

                        for i in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(375, 430, 430, 475, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(375, 430, 430, 475, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        # 나머지 해제하기 1
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 430, 640, 475, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("boonhae_checked : ", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                            time.sleep(0.5)
                    else:
                        # 나머지 해제하기 1
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(360, 430, 640, 475, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("boonhae_checked : ", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                            time.sleep(0.5)

                    # 나머지 해제하기 2
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 520, 355, 610, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("boonhae_checked : ", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(830, 730, cla)
                        time.sleep(0.3)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0


