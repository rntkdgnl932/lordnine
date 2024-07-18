import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def mission_get(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("mission_get")

        skip_start(cla)
        way_check(cla)

        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(1)
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0


def mission_get_daily(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import menu_open, confirm_all
    from clean_screen_lordnine import clean_screen_start

    try:
        print("mission_get_daily")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("mission", imgs_)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\mission_refresh_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 980, 100, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    get = True

                    # 일일 임무를 클릭하기 전 준비
                    for a in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("아직 수락할 수 없다는 글이 보인다.")
                        else:
                            break
                        time.sleep(1)

                    # 일일 임무를 얻쟈
                    for i in range(40):

                        anymore = False

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\ing.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            y_reg = imgs_.y
                        else:
                            y_reg = 700

                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\time_jogag.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(180, 100, 350, y_reg, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_soolock_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(810, 980, 950, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for a in range(5):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        anymore = True
                                        break
                                    time.sleep(0.1)
                        else:
                            for c in range(10):
                                result_confirm = confirm_all(cla)
                                if result_confirm == True:
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\mission_refresh_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 980, 100, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.4)

                        if anymore == True:
                            break



                    # 나가자
                    clean_screen_start(cla)


                else:
                    click_pos_2(48, 88, cla)

            else:

                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\menu_mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 140, 870, 220, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def mission_get_week(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_lordnine import menu_open, confirm_all
    from clean_screen_lordnine import clean_screen_start

    try:
        print("mission_get_daily")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("mission", imgs_)

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\week_mission.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 100, 50, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("week_mission", imgs_)
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\week_mission2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 950, 920, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("week_mission2", imgs_)

                        get = True


                        # 주간 임무를 클릭하기 전 준비
                        for a in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("아직 수락할 수 없다는 글이 보인다.")
                            else:
                                break
                            time.sleep(1)

                        # 주간 임무를 얻자
                        for w in range(10):

                            anymore = False

                            clicked = False

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\ing.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 100, 620, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("ing", imgs_)
                                y_reg = imgs_.y - 20
                            else:
                                y_reg = 700

                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\gamjung_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_for = imgs_set_for(170, 100, 400, y_reg, cla, img, 0.9)
                            if imgs_for is not None and imgs_for != False:
                                print("gamjung_1", imgs_for)
                                if len(imgs_for) > 0:
                                    for i in range(len(imgs_for)):
                                        click_pos_reg(imgs_for[i][0], imgs_for[i][1], cla)
                                        time.sleep(0.5)
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\gamjung_2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(600, 60, 700, 110, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("gamjung_2", imgs_)
                                            clicked = True
                                            break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_misson.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(170, 100, 400, y_reg, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("daily_misson", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        clicked = True
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\guild_donation.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(170, 100, 400, y_reg, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("guild_donation", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            clicked = True
                            if clicked == True:
                                time.sleep(0.5)
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\daily_soolock_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(810, 980, 950, 1030, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for a in range(5):
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\any_more_daily_quest.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(300, 100, 660, 160, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            anymore = True
                                            break
                                        time.sleep(0.1)

                            if anymore == True:
                                break
                            time.sleep(0.5)

                        # 나가자
                        clean_screen_start(cla)
                    else:
                        click_pos_2(148, 88, cla)

                else:
                    click_pos_2(148, 88, cla)

            else:

                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\mission\\menu_mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 140, 870, 220, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0