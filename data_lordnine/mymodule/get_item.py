import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_start(cla):
    from guild_lordnine import guild_start
    from power_up import power_up_sungmool
    from potion_lordnine import potion_buy_start

    try:
        print("get_start")

        potion_buy_start(cla)

        # get_gold_sohwan(cla)

        get_event(cla)

        get_battle_pass(cla)
        get_post(cla)
        get_upjuk(cla)
        get_monster_dogam(cla)

        power_up_sungmool(cla)

        guild_start(cla)



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
            imgs_ = imgs_set_(400, 300, 540, 340, cla, img, 0.85)
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
                    imgs_ = imgs_set_(400, 300, 540, 340, cla, img, 0.85)
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

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\seven_point_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(190, 325, 240, 740, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("seven_point_1", imgs_)
                click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                is_point = True
            else:
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
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\seven_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_for = imgs_set_for(245, 380, 880, 760, cla, img, 0.7)
                if imgs_for is not None and imgs_for != False:
                    print("seven_point_1", imgs_for)
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




def get_gold_sohwan(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, out_check
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_gold_sohwan")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("sangjum", imgs_)

                get = True

                ########################################################################

                #######################
                # 블랙프라이데이 사기
                #######################
                # for i in range(10):
                #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\black_friday_2024.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(170, 100, 770, 150, cla, img, 0.9)
                #     if imgs_ is not None and imgs_ != False:
                #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\100gold.PNG"
                #         img_array = np.fromfile(full_path, np.uint8)
                #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #         imgs_ = imgs_set_(190, 100, 340, 150, cla, img, 0.8)
                #         if imgs_ is not None and imgs_ != False:
                #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\wooho.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(190, 295, 340, 335, cla, img, 0.8)
                #             if imgs_ is not None and imgs_ != False:
                #                 break
                #             else:
                #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\100days_btn.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(0, 100, 130, 300, cla, img, 0.8)
                #                 if imgs_ is not None and imgs_ != False:
                #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                #
                #         else:
                #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\100days_btn.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(0, 100, 130, 300, cla, img, 0.8)
                #             if imgs_ is not None and imgs_ != False:
                #                 click_pos_reg(imgs_.x, imgs_.y, cla)
                #     else:
                #         # click_pos_2(150, 85, cla)
                #         for g in range(10):
                #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\black_friday_2024.PNG"
                #             img_array = np.fromfile(full_path, np.uint8)
                #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #             imgs_ = imgs_set_(170, 100, 770, 150, cla, img, 0.9)
                #             if imgs_ is not None and imgs_ != False:
                #                 break
                #             else:
                #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\black_friday_btn.PNG"
                #                 img_array = np.fromfile(full_path, np.uint8)
                #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #                 imgs_ = imgs_set_(0, 100, 130, 500, cla, img, 0.9)
                #                 if imgs_ is not None and imgs_ != False:
                #                     click_pos_reg(imgs_.x, imgs_.y, cla)
                #             QTest.qWait(200)
                #     time.sleep(0.5)
                #
                #
                # # 특별상품
                # get_event_sohwan_start(cla)

                ########################################################################

                #######################
                # 일반 골드 소환
                #######################
                # 골드소환
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sangjum_gold_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 100, 70, 300, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(190, 100, 340, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\ganghwasuk_sohwan_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(190, 295, 340, 335, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sangjum_gold_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 100, 70, 300, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sangjum_gold_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 100, 70, 300, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        # click_pos_2(150, 85, cla)
                        for g in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sangjum_gold_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 100, 70, 300, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\gyohwanso_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 70, 500, 110, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(200)
                    time.sleep(0.5)

                # 아바타 소환하기
                # 200 ~ 350, 400 ~ 550
                get_gold_sohwan_start(cla)

                # 방어구 강화석 사기
                # 200 ~ 350, 400 ~ 550
                get_ganghwasuk_sohwan_start(cla)







                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sangjum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        click_pos_2(755, 50, cla)
                    time.sleep(0.5)
                if get_point == False:
                    get = True
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def get_gold_sohwan_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos, click_pos_2, click_pos_reg
    from action_lordnine import confirm_all
    from massenger import line_to_me

    try:
        print("get_gold_sohwan_start")

        sohwan = True
        sohwan_count = 0

        while sohwan is True:
            sohwan_count += 1
            if sohwan_count > 7:
                sohwan = False

            is_sohwan = False

            for i in range(4):

                x_1 = 200 + (i * 200)
                x_2 = x_1 + 150
                x_reg = (x_1 + x_2) / 2

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\moogi_level_not_enough.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_1, 170, x_2, 290, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print(str(i + 1) + "번째는 무기레벨 제한이다.")
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_1, 170, x_2, 290, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print(str(i + 1) + "번째는 품절")
                    else:

                        is_sohwan = True
                        is_sold_out = False

                        for c in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("avatar_sohwan_title", imgs_)
                                # 확인 누르고 그전에 푸시 있으면 푸시 하고...
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\clicked_sold_out.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(320, 500, 400, 540, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    is_sold_out = True
                                break
                            else:
                                click_pos_2(x_reg, 200, cla)
                            time.sleep(0.5)
                        if is_sold_out == True:

                            for e in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        break
                                time.sleep(0.5)
                            break
                        else:
                            for c in range(20):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    confirm_all(cla)
                                else:
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == True:
                                        time.sleep(2)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\push_right_drag.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(300, 700, 750, 1040, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("push_right_drag", imgs_)
                                            drag_pos(400, 500, 850, 500, cla)

                                            why = "작살나는 아바타 나왔다. 확인해라"
                                            line_to_me(cla, why)

                                            time.sleep(3)
                                time.sleep(1)

                            for c in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sangjum.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("sangjum", imgs_)
                                    time.sleep(1)
                                    break
                                else:
                                    confirm_all(cla)
                                time.sleep(0.2)
                            if is_sohwan == True:
                                break

                time.sleep(0.2)

            if is_sohwan == False:
                sohwan = False

            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


def get_ganghwasuk_sohwan_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos, click_pos_2, click_pos_reg
    from action_lordnine import confirm_all
    from massenger import line_to_me

    try:
        print("get_ganghwasuk_sohwan_start")

        sohwan = True
        sohwan_count = 0

        while sohwan is True:
            sohwan_count += 1
            if sohwan_count > 7:
                sohwan = False

            is_sohwan = False

            for i in range(4):

                # 무기 강화석 까지 사려면 x_1 =200, range(4), 방어구만 사려면 600, range(2)
                x_1 = 200 + (i * 200)
                x_2 = x_1 + 150
                x_reg = (x_1 + x_2) / 2

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\moogi_level_not_enough.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_1, 360, x_2, 460, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print(str(i + 1) + "번째는 무기레벨 제한이다.")
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_1, 360, x_2, 460, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print(str(i + 1) + "번째는 품절")
                    else:

                        is_sohwan = True
                        is_sold_out = False

                        for c in range(5):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\ganghwasuk_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("ganghwasuk_title", imgs_)
                                # 확인 누르고 그전에 푸시 있으면 푸시 하고...
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\clicked_sold_out.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(320, 500, 400, 540, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    is_sold_out = True
                                break
                            else:
                                click_pos_2(x_reg, 400, cla)
                            time.sleep(0.5)
                        if is_sold_out == True:

                            for e in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\ganghwasuk_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        break
                                time.sleep(0.5)
                            break
                        else:

                            for c in range(20):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\ganghwasuk_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 340, 540, 400, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\max.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(370, 600, 450, 650, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        click_pos_2(415, 625, cla)
                                    time.sleep(0.5)

                                    confirm_all(cla)
                                else:
                                    break

                                time.sleep(1)
                            if is_sohwan == True:
                                break

                time.sleep(0.2)

            if is_sohwan == False:
                sohwan = False

            time.sleep(0.5)

        # 마지막으로 오른쪽에 있는 200만원짜리 사기
        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\talgut_box.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 110, 840, 140, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sold_out.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 235, 860, 270, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("200만원은 품절")
                    break
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\talgut_box_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 330, 480, 400, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(415, 615, cla)
                        time.sleep(0.5)
                        click_pos_2(570, 690, cla)
                    else:
                        click_pos_2(830, 215, cla)
            else:
                drag_pos(800, 300, 300, 300, cla)
            QTest.qWait(500)




    except Exception as e:
        print(e)
        return 0


def get_event_sohwan_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos, click_pos_2, click_pos_reg
    from action_lordnine import confirm_all
    from massenger import line_to_me

    try:
        print("get_event_sohwan_start")




        # ### 윗쪽 4개
        # sohwan = True
        # sohwan_count = 0
        #
        # while sohwan is True:
        #     sohwan_count += 1
        #     if sohwan_count > 7:
        #         sohwan = False
        #
        #     is_sohwan = False
        #
        #     for i in range(4):
        #
        #         x_1 = 200 + (i * 200)
        #         x_2 = x_1 + 150
        #         x_reg = (x_1 + x_2) / 2
        #
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sold_out.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(x_1, 170, x_2, 290, cla, img, 0.7)
        #         if imgs_ is not None and imgs_ != False:
        #             print(str(i + 1) + "번째는 품절")
        #         else:
        #
        #             is_sohwan = True
        #             is_sold_out = False
        #
        #             for c in range(5):
        #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("avatar_sohwan_close", imgs_)
        #                     # 확인 누르고 그전에 푸시 있으면 푸시 하고...
        #                     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\clicked_sold_out.PNG"
        #                     img_array = np.fromfile(full_path, np.uint8)
        #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                     imgs_ = imgs_set_(320, 500, 400, 540, cla, img, 0.8)
        #                     if imgs_ is not None and imgs_ != False:
        #                         is_sold_out = True
        #                     break
        #                 else:
        #                     click_pos_2(x_1, 200, cla)
        #                 time.sleep(0.5)
        #             if is_sold_out == True:
        #
        #                 for e in range(10):
        #                     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
        #                     img_array = np.fromfile(full_path, np.uint8)
        #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                     imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
        #                     if imgs_ is not None and imgs_ != False:
        #                         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
        #                         img_array = np.fromfile(full_path, np.uint8)
        #                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                         imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
        #                         if imgs_ is not None and imgs_ != False:
        #                             click_pos_reg(imgs_.x, imgs_.y, cla)
        #                         else:
        #                             break
        #                     time.sleep(0.5)
        #                 break
        #             else:
        #                 for c in range(10):
        #                     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
        #                     img_array = np.fromfile(full_path, np.uint8)
        #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                     imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
        #                     if imgs_ is not None and imgs_ != False:
        #                         click_pos_reg(imgs_.x, imgs_.y, cla)
        #                         time.sleep(0.2)
        #                         click_pos_reg(imgs_.x, imgs_.y, cla)
        #                         time.sleep(0.2)
        #                         result_confirm = confirm_all(cla)
        #                         if result_confirm == True:
        #                             time.sleep(1)
        #                             break
        #                     else:
        #                         result_confirm = confirm_all(cla)
        #                         if result_confirm == True:
        #                             time.sleep(1)
        #                             break
        #
        #                     time.sleep(0.5)
        #
        #                 for c in range(10):
        #                     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
        #                     img_array = np.fromfile(full_path, np.uint8)
        #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                     imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
        #                     if imgs_ is not None and imgs_ != False:
        #                         click_pos_reg(imgs_.x, imgs_.y, cla)
        #                         sohwan = False
        #                     else:
        #                         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sangjum.PNG"
        #                         img_array = np.fromfile(full_path, np.uint8)
        #                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                         imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
        #                         if imgs_ is not None and imgs_ != False:
        #                             print("sangjum", imgs_)
        #                             time.sleep(1)
        #                             break
        #                         else:
        #                             confirm_all(cla)
        #                     time.sleep(0.2)
        #                 if is_sohwan == True:
        #                     break
        #
        #
        #         time.sleep(0.2)
        #
        #     if is_sohwan == False:
        #         sohwan = False
        #
        #     time.sleep(0.5)

        ### 아래쪽 2개
        sohwan = True
        sohwan_count = 0

        while sohwan is True:
            sohwan_count += 1
            if sohwan_count > 7:
                sohwan = False

            is_sohwan = False

            for i in range(2):

                x_1 = 200 + (i * 200)
                x_2 = x_1 + 150
                x_reg = (x_1 + x_2) / 2

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sold_out.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_1, 360, x_2, 460, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print(str(i + 1) + "번째는 품절")

                    if i == 1:
                        sohwan = False

                else:

                    is_sohwan = True
                    is_sold_out = False

                    for c in range(5):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("avatar_sohwan_close", imgs_)
                            # 확인 누르고 그전에 푸시 있으면 푸시 하고...
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\clicked_sold_out.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(320, 560, 400, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                is_sold_out = True
                            break
                        else:
                            click_pos_2(x_reg, 400, cla)
                        time.sleep(0.5)
                    if is_sold_out == True:

                        for e in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                            time.sleep(0.5)
                        break
                    else:
                        for c in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                result_confirm = confirm_all(cla)
                                if result_confirm == True:
                                    time.sleep(1)
                                    break
                            else:
                                result_confirm = confirm_all(cla)
                                if result_confirm == True:
                                    time.sleep(1)
                                    break

                            time.sleep(0.5)

                        for c in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sangjum.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("sangjum", imgs_)
                                    time.sleep(1)
                                    break
                                else:
                                    confirm_all(cla)
                            time.sleep(0.2)

                time.sleep(0.2)

            if is_sohwan == False:
                sohwan = False

            time.sleep(0.5)

        ###
        # 당분간은 이걸로만 마무리하기


        # # 오른쪽으로 드래그 부터
        # for i in range(5):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\100gold.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(235, 110, 300, 140, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         break
        #     else:
        #         drag_pos(400, 300, 800, 300, cla)
        #     QTest.qWait(300)
        #
        # # 아래쪽 첫번째 품절인지
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sold_out.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(200, 360, 300, 460, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("아래 첫번째는 품절")
        # else:
        #     is_sold_out = False
        #
        #     for c in range(5):
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print("max", imgs_)
        #             # 확인 누르고 그전에 푸시 있으면 푸시 하고...
        #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\clicked_sold_out.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(320, 500, 400, 540, cla, img, 0.8)
        #             if imgs_ is not None and imgs_ != False:
        #                 is_sold_out = True
        #             break
        #         else:
        #             click_pos_2(200, 400, cla)
        #         time.sleep(0.5)
        #     if is_sold_out == True:
        #
        #         for e in range(10):
        #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
        #             if imgs_ is not None and imgs_ != False:
        #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
        #                 if imgs_ is not None and imgs_ != False:
        #                     click_pos_reg(imgs_.x, imgs_.y, cla)
        #                 else:
        #                     break
        #             time.sleep(0.5)
        #     else:
        #         for c in range(10):
        #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\event\\max.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(380, 600, 440, 640, cla, img, 0.85)
        #             if imgs_ is not None and imgs_ != False:
        #                 click_pos_reg(imgs_.x, imgs_.y, cla)
        #                 time.sleep(0.2)
        #                 click_pos_reg(imgs_.x, imgs_.y, cla)
        #                 time.sleep(0.2)
        #                 confirm_all(cla)
        #                 result_confirm = confirm_all(cla)
        #                 if result_confirm == True:
        #                     time.sleep(1)
        #                     break
        #             else:
        #                 result_confirm = confirm_all(cla)
        #                 if result_confirm == True:
        #                     time.sleep(1)
        #                     break
        #
        #             time.sleep(0.5)
        #
        #         for c in range(10):
        #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\avatar_sohwan_close.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(650, 340, 730, 400, cla, img, 0.8)
        #             if imgs_ is not None and imgs_ != False:
        #                 click_pos_reg(imgs_.x, imgs_.y, cla)
        #             else:
        #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sangjum.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("sangjum", imgs_)
        #                     time.sleep(1)
        #                     break
        #                 else:
        #                     confirm_all(cla)
        #             time.sleep(0.2)



        #######################
        ### 추후에 골드로 전환하기
        #######################

    except Exception as e:
        print(e)
        return 0

def get_diary(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, skip_start
    from clean_screen_lordnine import clean_screen_start

    try:
        print("get_diary")

        get = False
        get_count = 0

        while get is False:
            get_count += 1
            if get_count > 6:
                get = True


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\diary.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("diary", imgs_)

                get = True

                # 아템 얻자자
                is_diary = False

                # 하단 포인트 클릭
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 930, 480, 990, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("menu_point_1", imgs_)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                    is_diary = True
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 930, 480, 990, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_point_2", imgs_)
                        click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                        is_diary = True

                if is_diary == True:
                    time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\back.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 130, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\diary_open.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 550, 570, 660, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("diary_open", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                    # 받기
                    for i in range(10):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\back.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 130, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("back", imgs_)

                            ###
                            is_get_dairy = False
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(130, 85, 200, 400, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                is_get_dairy = True
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(130, 85, 200, 400, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point_2", imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                    is_get_dairy = True
                            if is_get_dairy == True:
                                time.sleep(0.5)
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\diary_get_point_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(360, 400, 500, 440, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("diary_get_point_1", imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                    for s in range(5):
                                        result_skip = skip_start(cla)
                                        if result_skip == True:
                                            time.sleep(1)
                                            break
                                        time.sleep(0.2)
                                else:
                                    break
                            else:
                                break
                            ###


                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\diary_open.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 550, 570, 660, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("diary_open", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)



                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\diary.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(910, 140, 950, 180, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                            get_point = True
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(910, 140, 950, 180, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 20, cla)
                                get_point = True
                    time.sleep(0.5)
                if get_point == False:
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
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
    from action_lordnine import menu_open_last
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
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("post", imgs_)

                post = True

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.65)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_point_1", imgs_)
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.65)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_2", imgs_)
                            break

                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.65)
                            if imgs_ is not None and imgs_ != False:
                                print("post_point_1", imgs_)
                                break
                    time.sleep(0.5)
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
                            imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.65)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1", imgs_)
                                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                                is_point = True

                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.65)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_point_2", imgs_)
                                    click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

                                    is_point = True

                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\post_point_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(50, 50, 610, 100, cla, img, 0.65)
                                    if imgs_ is not None and imgs_ != False:
                                        print("post_point_1", imgs_)
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
                menu_open_last(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
            imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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
                    imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
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



