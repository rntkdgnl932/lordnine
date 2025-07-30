import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')





def item_jejak(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open
    from clean_screen_lordnine import clean_screen_start

    try:
        print("item_jejak")

        jejak = False
        jejak_count = 0

        while jejak is False:
            jejak_count += 1
            if jejak_count > 7:
                jejak = True
                clean_screen_start(cla)

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\jejak.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("jejak", imgs_)
                jejak = True

                # 즐겨찾기 클릭
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\tarket_upgrade_whetstone_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 70, 670, 125, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\marksman_whetstone_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 70, 670, 125, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\monster_hunt_oil_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 70, 670, 125, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\bookmark_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 70, 180, 1030, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("bookmark_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\bookmark_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 70, 180, 1030, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("bookmark_2", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)


                # # 명중 강화 숯돌
                # for i in range(5):
                #
                #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\tarket_upgrade_whetstone_title.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(440, 70, 670, 125, cla, img, 0.95)
                #     if imgs_ is not None and imgs_ != False:
                #         print("명중 강화 숯돌", imgs_)
                #         jejak_btn_click(cla)
                #         break
                #     else:
                #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\tarket_upgrade_whetstone.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(190, 70, 340, 400, cla, img, 0.95)
                #         if imgs_ is not None and imgs_ != False:
                #             click_pos_reg(imgs_.x, imgs_.y, cla)
                #     time.sleep(0.5)

                # 명사수의 숯돌
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\marksman_whetstone_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 70, 670, 125, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        print("명사수의 숯돌", imgs_)
                        jejak_btn_click(cla)
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\marksman_whetstone.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(190, 70, 340, 400, cla, img, 0.95)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)


                # 괴물 사냥 기름
                for i in range(5):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\monster_hunt_oil_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 70, 670, 125, cla, img, 0.95)
                    if imgs_ is not None and imgs_ != False:
                        print("괴물 사냥 기름", imgs_)
                        jejak_btn_click(cla)
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\monster_hunt_oil.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(190, 70, 340, 400, cla, img, 0.95)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)



                # 나가기
                clean_screen_start(cla)


            else:
                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\jejak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\menu_jejak.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 30, 950, 500, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_jejak", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def jejak_btn_click(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open

    try:
        print("jejak_btn_click")

        # 제작되었는지 보기
        time.sleep(0.3)
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\max.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(570, 930, 660, 1010, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("max", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\jejak_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 950, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("jejak_btn", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)

        is_jejak = False
        for i in range(10):

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\touch_me_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 970, 600, 1030, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("touch_me_btn", imgs_)
                is_jejak = True
                break
            time.sleep(0.5)

        if is_jejak == True:

            for i in range(7):

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\touch_me_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 970, 600, 1030, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    print("touch_me_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0


