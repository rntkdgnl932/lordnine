import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def col_boon_start(cla):
    from jejak_lordnine import item_jejak

    try:
        print("col_boon_start")

        item_gamjung_start(cla)
        collection_start(cla)
        boonhae_start(cla)

        # 숫돌 등 버프 아이템 제작하기
        # 잠시 보류
        # item_jejak(cla)




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


        ### +5강 추가하기

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_5.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("plus_5 : ", imgs_)

        collection_count = 0
        collection = False

        while collection is False:
            collection_count += 1
            if collection_count > 7:
                collection = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\item_collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("item_collection", imgs_)

                collection = True

                way_check(cla)

                collection_scan_option(cla)
                time.sleep(0.3)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    collection_scan_option(cla)
                else:
                    ganghwa = True

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
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\col_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("col_point_2 : ", imgs_)
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
                                if ganghwa == True:
                                    is_item = True

                                    upgrade = 0

                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_5.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("plus_5 : ", imgs_)
                                        click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                                        upgrade = 5
                                        time.sleep(0.2)

                                        for c in range(5):
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_registery_item.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("not_registery_item : ", imgs_)
                                                is_item = False
                                                break
                                            time.sleep(0.1)
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_5_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("plus_5_3 : ", imgs_)
                                            click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                                            upgrade = 5
                                            time.sleep(0.2)
                                            for c in range(5):
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_registery_item.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("not_registery_item : ", imgs_)
                                                    is_item = False
                                                    break
                                                time.sleep(0.1)
                                        else:
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_7.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
                                            if imgs_ is not None and imgs_ != False:
                                                print("plus_7 : ", imgs_)
                                                click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                                                upgrade = 7
                                                time.sleep(0.2)
                                                for c in range(5):
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_registery_item.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("not_registery_item : ", imgs_)
                                                        is_item = False
                                                        break
                                                    time.sleep(0.1)
                                            else:
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_3.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("plus_3 : ", imgs_)
                                                    click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                                                    upgrade = 3
                                                    time.sleep(0.2)
                                                    for c in range(5):
                                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_registery_item.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("not_registery_item : ", imgs_)
                                                            is_item = False
                                                            break
                                                        time.sleep(0.1)
                                                else:
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_8.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("plus_8 : ", imgs_)
                                                        click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                                                        upgrade = 8
                                                        time.sleep(0.2)
                                                        for c in range(5):
                                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_registery_item.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
                                                            if imgs_ is not None and imgs_ != False:
                                                                print("not_registery_item : ", imgs_)
                                                                is_item = False
                                                                break
                                                            time.sleep(0.1)
                                                    else:
                                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_9.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("plus_9 : ", imgs_)
                                                            click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)
                                                            upgrade = 9
                                                            time.sleep(0.2)
                                                            for c in range(5):
                                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_registery_item.PNG"
                                                                img_array = np.fromfile(full_path, np.uint8)
                                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                                imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
                                                                if imgs_ is not None and imgs_ != False:
                                                                    print("not_registery_item : ", imgs_)
                                                                    is_item = False
                                                                    break
                                                                time.sleep(0.1)
                                                        else:
                                                            is_item = False
                                    #
                                    if is_item == True:
                                        print("강화 후 등록하자")

                                        ganghwa = False


                                        for c in range(10):
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                is_upgrade = False
                                                if upgrade == 5:
                                                    is_upgrade = True
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_5_btn.PNG"
                                                elif upgrade == 7:
                                                    is_upgrade = True
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_7_btn.PNG"
                                                elif upgrade == 3:
                                                    is_upgrade = True
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_3_btn.PNG"
                                                elif upgrade == 8:
                                                    is_upgrade = True
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_8_btn.PNG"
                                                elif upgrade == 9:
                                                    is_upgrade = True
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_9_btn.PNG"
                                                if is_upgrade == True:
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(220, 600, 610, 650, cla, img, 0.95)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("upgrade : ", imgs_)
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        time.sleep(0.1)
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        time.sleep(0.1)
                                                        click_pos_2(365, 705, cla)
                                                        for f in range(5):
                                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\ganghwa_fail_notice.PNG"
                                                            img_array = np.fromfile(full_path, np.uint8)
                                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                            imgs_ = imgs_set_(400, 390, 550, 450, cla, img,
                                                                              0.85)
                                                            if imgs_ is not None and imgs_ != False:
                                                                click_pos_2(365, 705, cla)
                                                                break
                                                            time.sleep(1)
                                                        ganghwa = True
                                                        break
                                                    else:
                                                        click_pos_2(415, 340, cla)
                                                        time.sleep(1)

                                            else:
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\ganghwa_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(730, 880, 820, 930, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("ganghwa_btn : ", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.5)

                                        if ganghwa == False:
                                            clean_screen_start(cla)
                                        else:
                                            for c in range(10):
                                                # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\fail_is_destroy.PNG"
                                                # img_array = np.fromfile(full_path, np.uint8)
                                                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                # imgs_ = imgs_set_(280, 650, 465, 690, cla, img, 0.85)
                                                # if imgs_ is not None and imgs_ != False:
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_2(830, 305, cla)
                                                    time.sleep(0.5)
                                                else:
                                                    click_pos_2(885, 910, cla)
                                                    time.sleep(0.5)
                                                    break
                                                time.sleep(0.5)

                                    else:
                                        clean_screen_start(cla)
                                        break
                        time.sleep(0.5)
            else:
                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\item_collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
            if collection_count > 10:
                collection = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("scan_option_title", imgs_)

                check_end = False

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_not_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 450, 240, 510, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:

                    print("scan_option_not_checked", imgs_)

                    # 바 내리기
                    print("바 내리기")
                    click_pos_2(660, 580, cla)
                    time.sleep(0.5)
                    click_pos_2(660, 580, cla)
                    time.sleep(0.5)

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
                        imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            confirm_all(cla)
                        else:
                            break
                        time.sleep(0.5)
                else:
                    # 바 내리기
                    print("바 내리기...")
                    click_pos_2(660, 580, cla)
                    time.sleep(0.5)
                    click_pos_2(660, 580, cla)
                    time.sleep(0.5)

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
                            else:
                                click_pos_2(370, 480, cla)
                                time.sleep(0.5)
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
                                else:
                                    click_pos_2(480, 480, cla)
                                    time.sleep(0.5)
                            time.sleep(0.5)

                        # 나머지 해제하기 1
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 450, 760, 510, cla, img, 0.75)
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
                            imgs_ = imgs_set_(380, 450, 760, 510, cla, img, 0.75)
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
                        imgs_ = imgs_set_(180, 490, 360, 545, cla, img, 0.75)
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
                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\scan_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 380, 540, 440, cla, img, 0.85)
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
            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                bag_open(cla)
                click_pos_2(800, 1005, cla)
                for n in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
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
                                    imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
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
    from clean_screen_lordnine import clean_screen_start, clean_screen_just_on_start
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
                    # clean_screen_start(cla)
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
                            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
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

        # 여기서 희귀...
        if v_.onCollection_boonhae_rare == True:
            boonhae_option_rare(cla)

            for i in range(10):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 670, 410, 740, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:




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
                                imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
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

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\not_selected.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 500, 500, 600, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                clean_screen_start(cla)
            else:
                break
            time.sleep(1)

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
            imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.85)
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
                    imgs_ = imgs_set_(270, 515, 450, 600, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        check_end = False
                    else:
                        # 일반만 체크된 상황
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 425, 335, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            # 고급까지 체크인지 확인
                            if v_.onCollection_boonhae == True:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(375, 425, 430, 470, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:

                                    # 체크 되지 않아야 할 부분에 체크 되어있는지 확인
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(450, 425, 640, 470, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        check_end = False
                                    else:
                                        check_end = True

                            else:
                                # 체크 되지 않아야 할 부분에 체크 되어있는지 확인
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(360, 425, 640, 470, cla, img, 0.7)
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
                        imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.85)
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
                        imgs_ = imgs_set_(280, 425, 335, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 425, 335, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    # 귀속체크하기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 455, 335, 495, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 455, 335, 495, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)



                    if v_.onCollection_boonhae == True:
                        # 고급까지체크하기

                        for i in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(375, 425, 430, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(375, 425, 430, 470, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        # 나머지 해제하기 1
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 425, 640, 470, cla, img, 0.8)
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
                            imgs_ = imgs_set_(360, 425, 640, 470, cla, img, 0.8)
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
                        imgs_ = imgs_set_(280, 520, 450, 610, cla, img, 0.8)
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
                imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(830, 730, cla)
                        time.sleep(0.3)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0


def boonhae_option_rare(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import confirm_all
    from tuto_lordnine import way_check

    try:
        print("boonhae_option_rare")

        boonhae_option_count = 0
        boonhae_option = False

        while boonhae_option is False:
            boonhae_option_count += 1
            if boonhae_option_count > 7:
                boonhae_option = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_option_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.85)
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
                    imgs_ = imgs_set_(270, 515, 450, 600, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        check_end = False
                    else:
                        # 일반만 체크된 상황
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 425, 335, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            # 희귀까지 체크인지 확인
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(375, 425, 430, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 425, 515, 470, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:

                                    # 체크 되지 않아야 할 부분에 체크 되어있는지 확인
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(560, 425, 640, 470, cla, img, 0.7)
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
                        imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.85)
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

                    # 희귀는 무기 빼주자

                    print("희귀 무기 빼는 작업")
                    for i in range(15):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\right_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(795, 360, 825, 420, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("무기 클릭됨", i)
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(620, 315, 815, 700, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_for(620, 315, 815, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("item_checked_1", imgs_)
                                    for o in range(len(imgs_)):
                                        click_pos_reg(imgs_[o][0] - 15, imgs_[o][1], cla)
                                        time.sleep(0.5)

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(620, 315, 815, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_for(620, 315, 815, 700, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("item_checked_2", imgs_)
                                        for o in range(len(imgs_)):
                                            click_pos_reg(imgs_[o][0] - 15, imgs_[o][1], cla)
                                            time.sleep(0.5)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(620, 315, 815, 700, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_3.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_for(620, 315, 815, 700, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("item_checked_3", imgs_)
                                            for o in range(len(imgs_)):
                                                click_pos_reg(imgs_[o][0] - 15, imgs_[o][1], cla)
                                                time.sleep(0.5)
                                    else:
                                        print("더이상 없다.")
                                        break
                        else:
                            click_pos_2(830, 395, cla)
                        time.sleep(0.5)

                else:


                    # 일반체크하기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 425, 335, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 425, 335, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    # 귀속체크하기
                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 455, 335, 495, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 455, 335, 495, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)


                    # 희귀까지체크하기

                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(375, 425, 430, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(375, 425, 430, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    for i in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 425, 515, 470, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_not_checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 425, 515, 470, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    # 나머지 해제하기 1
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(560, 425, 640, 470, cla, img, 0.8)
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
                        imgs_ = imgs_set_(280, 520, 450, 610, cla, img, 0.8)
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
                imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_option_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 340, 550, 440, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, 270, 465, 335, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(830, 730, cla)
                        time.sleep(0.3)
            time.sleep(0.5)




    except Exception as e:
        print(e)
        return 0
