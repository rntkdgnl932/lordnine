import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def guild_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("guild_start")

        guild_in(cla)



    except Exception as e:
        print(e)
        return 0


def guild_in(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_lordnine import menu_open, skip_start
    from clean_screen_lordnine import clean_screen_start

    try:
        print("guild_in")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\guild.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("guild", imgs_)





                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_donation.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 980, 230, 1030, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("guild_donation", imgs_)

                    get = True

                    # 자동 출석 보상임
                    skip_start(cla)

                    # 기부하기
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_donation_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 600, 400, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            time.sleep(0.5)
                            break
                        else:

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_donation.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(120, 980, 230, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("guild_donation", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_donation_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 600, 400, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\donation_zero.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 690, 540, 730, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                click_pos_2(370, 650, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_donation_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 600, 400, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(680, 360, cla)
                        else:
                            break
                        time.sleep(0.5)

                    # 추방하기

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_member_screen_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 980, 350, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            click_pos_2(415, 120, cla)
                        time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_member_screen_in.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 980, 350, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_before_day.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(850, 150, 950, 1000, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:


                                for b in range(40):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_before_day.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(850, 150, 950, 1000, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                        for y in range(10):
                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_post_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(670, 100, 800, 1040, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                break
                                            time.sleep(0.2)

                                        # 추방이 있다면 아래 진행, 없다면 진행하면 안됨
                                        bye = False
                                        for y in range(10):

                                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\bye_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(670, 100, 800, 1040, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                bye = True
                                                break
                                            time.sleep(0.2)

                                        if bye == False:
                                            break
                                        else:
                                            for y in range(10):

                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\bye_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(470, 570, 660, 660, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    break
                                                else:
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\bye_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(670, 100, 800, 1040, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.3)

                                    else:
                                        break
                                    time.sleep(0.5)
                            else:
                                anymore = True
                                for c in range(5):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_before_day.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(850, 150, 950, 1000, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        anymore = False
                                        break
                                    else:
                                        drag_pos(770, 850, 770, 250, cla)
                                    time.sleep(0.5)

                                if anymore == True:
                                    break

                        else:
                            click_pos_2(415, 120, cla)
                        time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\guild_create.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 970, 580, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("guild_donation", imgs_)

                        get = True

                        # 자동 출석 보상임
                        skip_start(cla)





                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\guild\\menu_guild.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(630, 250, 710, 360, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

