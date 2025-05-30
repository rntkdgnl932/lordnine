import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    from datetime import datetime
    import pyautogui
    import random
    import pydirectinput

    from function_game import text_check_get_num, drag_pos, imgs_set_, imgs_set_for, click_pos_reg, click_pos_2, text_check_get, text_check_get_black_white, in_number_check, change_number_float
    from tuto_lordnine import way_check
    from action_lordnine import attack_on, juljun_on, juljun_off, bag_open, juljun_check, confirm_all, go_maul, out_check, homoon_clear, juljun_time_check, silhumsil_ganghwa
    from clean_screen_lordnine import clean_screen_just_on_start, clean_screen_start
    from boonhae_collection import collection_scan_option, item_gamjung_start, col_boon_start, boonhae_option, boonhae_start
    from potion_lordnine import potion_buy_start, potion_check, potion_setting
    from get_item import get_start, get_event, get_battle_pass, get_gold_sohwan, get_diary, get_ganghwasuk_sohwan_start, get_arena

    from jadong_lordnine import jadong_start, spot_go, dethland_go
    from dead_die import dead_recorvery, dead_check
    from dungeon_lordnine import dun_in, garbana_move, step_select
    from power_up import power_up_sungmool
    from mission_lordnine import mission_get, mission_get_daily
    from guild_lordnine import guild_start
    from auction_game import auction_start, get_low_price, auction_jangbi, mine_check, sell_click_new, auction_jangbi_new_sell
    from jejak_lordnine import item_jejak
    from property_game import my_property_upload

    from auction_game import get_now_low_price


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5


    try:
        # potion_check("three")

        nowHour = int(datetime.today().strftime("%H"))

        print("nowHour", nowHour)

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_click_title\\garbana.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 100, 150, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("garbana", imgs_)
            # 124

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_complete_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(205, 175, 255, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dun_complete_1", imgs_)
                # + 51 / + 25
                # 175, 200
                # + 71 / + 25
                # 195, 220

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_click_title\\adoom.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 100, 150, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("adoom", imgs_)
            # 239

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_click_title\\talag.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 100, 150, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("talag", imgs_)
            # 334

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_click_title\\soolyun.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 100, 150, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("soolyun", imgs_)
            # 469

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_3.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
        # if imgs_ is not None and imgs_ != False:
        #     print("plus_3 : ", imgs_)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_8.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.9)
        # if imgs_ is not None and imgs_ != False:
        #     print("plus_8 : ", imgs_)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\plus_9.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("plus_9 : ", imgs_)

        # get_now_low_price(cla)

        # sell_click_new(cla, "item")

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_jangbi\\list_q_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_for(760, 130, 950, 1000, cla, img, 0.9)
        # if imgs_ is not None and imgs_ != False:
        #     print("list_q_1", imgs_)
        #     for o in range(len(imgs_)):
        #         result_anymore = auction_jangbi_new_sell(cla, imgs_[len(imgs_) - 1 - o][0] + 15, imgs_[len(imgs_) - 1 - o][1] + 15)
        #         time.sleep(0.5)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\no_information.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(400, 530, 465, 565, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("no_information 1", imgs_)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\no_information.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(640, 530, 700, 565, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("no_information 2", imgs_)

        # result_get_price_ready = str(get_now_low_price(cla))
        # result_get_price = result_get_price_ready.split(".")
        # print("result_get_price", result_get_price)
        # print("len(result_get_price[0])", len(result_get_price[0]))


        # x_reg = 700
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\auction_num_point.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(650, 540, 700, 695, cla, img, 0.9)
        # if imgs_ is not None and imgs_ != False:
        #     print("auction : auction_num_point", imgs_)
        #     x_reg = imgs_.x
        # if x_reg != 700:
        #     result_get_1 = text_check_get_black_white(640, 540, x_reg - plus, 697, cla)
        #     print("auction : result_get_1", result_get_1)
        # else:
        #     # 제일 먼저....
        #     print("1")


        # for i in range(30):
        #     result_get_2 = text_check_get_black_white(630, 540, 700, 560, cla)
        #     print("auction : result_get_2", result_get_2)
        #     if result_get_1 != result_get_2:
        #         is_data = True
        #         break
        #     time.sleep(1)

        # print("attack : last result", result_get_1, result_get_2)


        #################################################


        # for g in range(10):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\sangjum_gold_btn.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 100, 70, 300, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         break
        #     else:
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\gyohwanso_btn.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(0, 70, 500, 110, cla, img, 0.8)
        #         if imgs_ is not None and imgs_ != False:
        #             click_pos_reg(imgs_.x, imgs_.y, cla)
        #     QTest.qWait(200)


        # for i in range(15):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\right_checked.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(795, 360, 825, 420, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         print("무기 클릭됨", i)
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_1.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(620, 315, 815, 700, cla, img, 0.7)
        #         if imgs_ is not None and imgs_ != False:
        #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_1.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_for(620, 315, 815, 700, cla, img, 0.7)
        #             if imgs_ is not None and imgs_ != False:
        #                 print("item_checked_1", imgs_)
        #                 for o in range(len(imgs_)):
        #                     click_pos_reg(imgs_[o][0] - 15, imgs_[o][1], cla)
        #                     time.sleep(0.5)
        #
        #         else:
        #             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_2.PNG"
        #             img_array = np.fromfile(full_path, np.uint8)
        #             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #             imgs_ = imgs_set_(620, 315, 815, 700, cla, img, 0.7)
        #             if imgs_ is not None and imgs_ != False:
        #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_2.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_for(620, 315, 815, 700, cla, img, 0.7)
        #                 if imgs_ is not None and imgs_ != False:
        #                     print("item_checked_2", imgs_)
        #                     for o in range(len(imgs_)):
        #                         click_pos_reg(imgs_[o][0] - 15, imgs_[o][1], cla)
        #                         time.sleep(0.5)
        #             else:
        #                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_3.PNG"
        #                 img_array = np.fromfile(full_path, np.uint8)
        #                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                 imgs_ = imgs_set_(620, 315, 815, 700, cla, img, 0.7)
        #                 if imgs_ is not None and imgs_ != False:
        #                     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\item_checked_3.PNG"
        #                     img_array = np.fromfile(full_path, np.uint8)
        #                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #                     imgs_ = imgs_set_for(620, 315, 815, 700, cla, img, 0.7)
        #                     if imgs_ is not None and imgs_ != False:
        #                         print("item_checked_3", imgs_)
        #                         for o in range(len(imgs_)):
        #                             click_pos_reg(imgs_[o][0] - 15, imgs_[o][1], cla)
        #                             time.sleep(0.5)
        #                 else:
        #                     print("더이상 없다.")
        #                     break
        #     else:
        #         click_pos_2(830, 395, cla)
        #     time.sleep(0.5)



        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_jangbi\\skill_book_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("skill_book_1", imgs_)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_jangbi\\skill_book_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("skill_book_2", imgs_)

        # homoon_clear(cla)

        # data = "Three:1:각종템받기:대기중:Four:1:각종템받기:대기중\nThree:1:거래소등록:대기중:Four:1:튜토육성:대기중\nThree:1:튜토육성:대기중:Four:1:일일임무_3_우호:대기중\nThree:1:일일임무_5_우호:대기중:Four:1:던전_어둠의숲_2:대기중\nThree:1:버프와물약사기:대기중:Four:1:던전_타락한미궁_2:대기중\nThree:1:던전_검은실험실_2:대기중:Four:1:각종템받기:대기중\nThree:1:던전_어둠의숲_3:대기중:Four:1:거래소등록:대기중\nThree:1:던전_조각의숲_3:대기중:Four:1:거래소등록:대기중\nThree:1:던전_타락한미궁_3:대기중:Four:1:던전_어둠의숲_3:대기중\nThree:1:각종템받기:대기중:Four:1:던전_조각의숲_3:대기중\nThree:1:던전_이벤트_3:대기중:Four:1:던전_타락한미궁_3:대기중\nThree:1:시련의탑:대기중:Four:1:일일임무_4_우호:대기중\nThree:1:거래소등록:대기중:Four:1:일일임무_3_우호:대기중\nThree:1:특수/티리오사무덤/지하1층:대기중:Four:1:던전_이벤트_3:대기중\n"
        #
        # dir_path = "C:\\my_games\\" + str(v_.game_folder)
        # file_path = dir_path + "\\mysettings\\myschedule\\schedule.txt"
        # file_path3 = dir_path + "\\mysettings\\myschedule\\schedule2.txt"
        #
        # with open(file_path, "w", encoding='utf-8-sig') as file:
        #     file.write(str(data))
        # with open(file_path3, "w", encoding='utf-8-sig') as file:
        #     file.write(str(data))



        # for i in range(10):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\my_property\\" + str(i) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(745, 45, 805, 58, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         print("num", i, imgs_)

        # result = mine_check(cla)
        # print("result", result)

        # x_standard = 805
        #
        # for i in range(10):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\my_property\\" + str(i) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(745, 45, 805, 58, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         # print("num", i, imgs_)
        #         if x_standard > imgs_.x:
        #             x_standard = imgs_.x - plus
        #
        # print("x_standard", x_standard)
        #
        # x_standard = x_standard - 5
        #
        # for i in range(10):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\my_property\\" + str(i) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(x_standard, 45, x_standard + 10, 58, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         print("while num", x_standard, i, imgs_)
        #         text_check_get_reg(x_standard, 45, x_standard + 10, 58)
        #         x_standard = imgs_.x - plus
        #     else:
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\propert_point.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(x_standard, 45, x_standard + 10, 58, cla, img, 0.9)
        #         if imgs_ is not None and imgs_ != False:
        #             print("propert_point", x_standard, i, imgs_)
        #             text_check_get_reg(x_standard, 45, x_standard + 10, 58)
        #             x_standard = imgs_.x - plus

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\jejak\\tarket_upgrade_whetstone.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(190, 70, 340, 400, cla, img, 0.95)
        # if imgs_ is not None and imgs_ != False:
        #     print("tarket_upgrade_whetstone", imgs_)

        # get_gold_sohwan(cla)
        # where = "던전_가르바나지하수로_5"
        #
        # dun_in(cla, where)

        # result_dia = text_check_get(745, 45, 805, 58, cla)
        # print("result_dia", result_dia)

        # result_gold = text_check_get(840, 45, 903, 58, cla)
        # print("result_gold", result_gold)

        # result_dia = text_check_get(782 - 5, 45, 782 + 5, 58, cla)
        # print("result_dia", result_dia)

        # auction_start(cla)

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sungmool.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("sungmool", imgs_)
        #     power_up_sungmool(cla)
        # else:
        #     homoon_clear(cla)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\homoon\\321.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(420, 910, 630, 960, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("321", imgs_)



        #################################################
        # get_diary(cla)

        # text_check_get(512, 315, 542, 360, cla)



        # x_1 = 200 + 70
        # y_1 = 900
        # x_2 = 217 + 70
        # y_2 = 920
        #
        # x_1 = 700 + 70
        # y_1 = 905
        # x_2 = 722 + 70
        # y_2 = 923
        #
        # text_check_get(x_1, y_1, x_2, y_2, cla)

        # mission_get_daily(cla, data)

        # nowMinute = int(datetime.today().strftime("%M"))
        # print("nowMinute", nowMinute)
        # result_m = nowMinute % 10
        # print("result_m", result_m)
        #
        # if nowMinute == 0:
        #     print("00000")
        # else:
        #     print("result_m")
        #
        # # get_gold_sohwan(cla)
        #
        # # auction_start(cla)
        #
        # for i in range(5):
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\push_right_drag.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(300, 700, 750, 1040, "three", img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         print("push_right_drag", imgs_)
        #         click_pos_2(400, 500, cla)
        #         drag_pos(400, 500, 850, 500, cla)
        #
        #     time.sleep(1)


        # 성물 레벨
        # result_level_ready = text_check_get(65, 110, 135, 140, cla)
        # print("result_level_ready", result_level_ready)
        # result_level_ = int_put_(result_level_ready)
        # print("result_level_", result_level_)

        # result_price_ready = text_check_get_num(410, 545, 455, 560, cla)
        #
        # result_price_ready = change_number(result_price_ready)
        # print("result_price_change", result_price_ready)

        ##############

        # result_price_ready = text_check_get_num(415, 546, 456, 556, cla)
        # print("1. result_price_ready", result_price_ready)

        # 판매수량 구하기

        # auction_start(cla)

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_enroll_btn.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(400, 600, 540, 700, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("sell_enroll_btn", imgs_)
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\col_point_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.75)
        # if imgs_ is not None and imgs_ != False:
        #     print("col_point_1 : ", imgs_)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\col_point_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(350, 105, 720, 980, cla, img, 0.75)
        # if imgs_ is not None and imgs_ != False:
        #     print("col_point_2 : ", imgs_)
        #
        # collection_start(cla)




        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\clean_screen\\close_3.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("close_3")

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\num_point.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(415 , y_1, 435 + plus, y_2, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("num_point", imgs_)

        # result_price_ready = text_check_get_num(410, 581, 456, 593, cla)
        # print("2. result_price_ready", result_price_ready)
        #
        # result_price_ready = change_number_float(result_price_ready)
        # print("22. result_price_change", result_price_ready)

        # auction_start(cla)
        ##################################


        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list\\list_q_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("list_q_1", imgs_)
        #
        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list\\list_q_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("list_q_2", imgs_)




        ######################################

        # v_.onCollecion = True
        # v_.onCollecion_boonhae = True

        # collection_scan_option(cla)


        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\boonhae_collection\\boonhae_checked.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(270, 515, 350, 600, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("체크", imgs_)
        # else:
        #     print("ㅎㅁㄴㅇㅎㅁ")



        # for i in range(5):
        #     x_1 = i + 1
        #     print("x_1", x_1)
        #
        #     for y in range(3):
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_step\\bottom\\" + str(x_1) + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(340, 740, 900, 850, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print("result : x_1", imgs_)
        #             click_pos_reg(imgs_.x, imgs_.y, cla)
        #             time.sleep(0.2)
        #         else:
        #             if x_1 > 3:
        #                 drag_pos(630, 810, 300, 810, cla)
        #         time.sleep(0.3)
        #     time.sleep(0.2)

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\monster_close.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(230, 330, 870, 720, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("monster_close", imgs_)

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\out\\talk.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 940, 60, 990, cla, img, 0.75)
        # if imgs_ is not None and imgs_ != False:
        #     print("talk")

        # full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(100, 50, 170, 950, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("menu_point_1", imgs_)
        #     is_point = True
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_1.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_for(100, 50, 170, 950, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         print("menu_point_1", imgs_)
        #         if len(imgs_) > 0:
        #             last = len(imgs_) - 1
        #             click_pos_reg(imgs_[last][0] - 30, imgs_[last][1] + 10, cla)
        #             time.sleep(0.5)
        # else:
        #     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(100, 50, 170, 950, cla, img, 0.7)
        #     if imgs_ is not None and imgs_ != False:
        #         print("menu_point_2", imgs_)
        #         is_point = True
        #         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\get_item\\menu_point_2.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_for(100, 50, 170, 950, cla, img, 0.7)
        #         if imgs_ is not None and imgs_ != False:
        #             print("menu_point_2", imgs_)
        #             if len(imgs_) > 0:
        #                 last = len(imgs_) - 1
        #                 click_pos_reg(imgs_[last][0] - 30, imgs_[last][1] + 10, cla)
        #                 time.sleep(0.5)


    except Exception as e:
        print(e)

def go_def_test(cla):
    import numpy as np
    import cv2
    from datetime import datetime
    import pyautogui
    import random
    import pydirectinput

    from function_game import text_check_get_num, drag_pos, imgs_set_, imgs_set_for, click_pos_reg, click_pos_2, text_check_get_num, mouse_move_cpp, in_number_check, change_number_float
    from tuto_lordnine import way_check
    from action_lordnine import skip_start, juljun_on, juljun_off, bag_open, juljun_check, confirm_all, go_maul, out_check
    from clean_screen_lordnine import clean_screen_just_on_start
    from boonhae_collection import collection_scan_option, item_gamjung_start, col_boon_start, boonhae_option, boonhae_start, collection_start
    from potion_lordnine import potion_buy_start
    from get_item import get_start, get_event, get_battle_pass, get_gold_sohwan, get_diary
    from jadong_lordnine import jadong_start, spot_go
    from dead_die import dead_recorvery, dead_check
    from dungeon_lordnine import dun_in
    from power_up import power_up_sungmool
    from mission_lordnine import mission_get
    from guild_lordnine import guild_start
    from auction_game import auction_start, get_low_price



    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5


    try:
        print("test")

    except Exception as e:
        print(e)

#
# def dun_in(cla, where):
#     import numpy as np
#     import cv2
#     import os
#
#     from function_game import imgs_set_, click_pos_reg, click_pos_2
#     from action_lordnine import menu_open, out_check, loading_check, attack_on, juljun_on
#     from potion_lordnine import potion_buy_start
#
#     from schedule import myQuest_play_add
#
#     try:
#         print("dun_in", where)
#
#         # 이벤트 던전 여부
#         event_dungeon = False
#
#         y_e_plus = 0
#         if event_dungeon == True:
#             y_e_plus = 120
#
#
#         # 검은 실험실 이벤트 여부
#         black_laboratory = True
#
#         # 던전_어둠의숲_3
#
#         result_spot = where.split("_")
#
#         # result_spot[1] => 던전종류
#         # resut_spot[2] => 층수
#         if result_spot[1] == "검은실험실":
#             if black_laboratory == True:
#                 y_1 = 160 + y_e_plus
#             else:
#                 y_1 = 590 + y_e_plus
#             dun_name = "black"
#         elif result_spot[1] == "어둠의숲":
#             if black_laboratory == True:
#                 y_1 = 390 + y_e_plus
#             else:
#                 y_1 = 280 + y_e_plus
#             dun_name = "adoom"
#
#         elif result_spot[1] == "타락한미궁":
#             if black_laboratory == True:
#                 y_1 = 510 + y_e_plus
#             else:
#                 y_1 = 400 + y_e_plus
#             dun_name = "talag"
#         elif result_spot[1] == "가르바나지하수로":
#             if black_laboratory == True:
#                 y_1 = 280 + y_e_plus
#             else:
#                 y_1 = 170 + y_e_plus
#             dun_name = "garbana"
#
#         elif result_spot[1] == "이벤트":
#             y_1 = 170
#             dun_name = "event"
#
#         elif result_spot[1] == "수련의전당":
#             if black_laboratory == True:
#                 y_1 = 620 + y_e_plus
#             else:
#                 y_1 = 520
#
#             dun_name = "soolyun"
#
#         # 던전 가기전 물약 사자
#         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
#         img_array = np.fromfile(full_path, np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
#         if imgs_ is not None and imgs_ != False:
#             print("던전 고르는 중")
#         else:
#             potion_buy_start(cla)
#
#
#         QTest.qWait(500)
#
#         dun = False
#         dun_count = 0
#         print("dun True??? False???", dun)
#
#         while dun is False:
#             dun_count += 1
#             if dun_count > 7:
#                 dun = True
#
#             full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
#             img_array = np.fromfile(full_path, np.uint8)
#             img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#             imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
#             if imgs_ is not None and imgs_ != False:
#                 print("dungeon", imgs_)
#
#                 dun = True
#
#                 complete = False
#
#                 y_plus = 0
#
#                 if event_dungeon == True:
#                     y_plus = 115
#
#                 # 만료여부
#                 full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_complete_1.PNG"
#                 img_array = np.fromfile(full_path, np.uint8)
#                 img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                 if str(dun_name) == "black":
#                     if black_laboratory == True:
#                         imgs_ = imgs_set_(205, 175 + y_plus, 255, 200 + y_plus, cla, img, 0.8)
#                     else:
#                         if event_dungeon == True:
#                             imgs_ = imgs_set_(205, 715 + y_plus, 255, 745 + y_plus, cla, img, 0.8)
#                         else:
#                             imgs_ = imgs_set_(205, 600 + y_plus, 255, 630 + y_plus, cla, img, 0.8)
#
#                 elif str(dun_name) == "garbana":
#                     if black_laboratory == True:
#                         imgs_ = imgs_set_(205, 290 + y_plus, 255, 315 + y_plus, cla, img, 0.8)
#                     else:
#                         if event_dungeon == True:
#                             imgs_ = imgs_set_(205, 175 + y_plus, 255, 200 + y_plus, cla, img, 0.8)
#                         else:
#                             imgs_ = imgs_set_(205, 175, 255, 200, cla, img, 0.8)
#
#                 elif str(dun_name) == "adoom":
#                     if black_laboratory == True:
#                         imgs_ = imgs_set_(205, 405 + y_plus, 255, 430 + y_plus, cla, img, 0.8)
#                     else:
#                         if event_dungeon == True:
#                             imgs_ = imgs_set_(205, 290 + y_plus, 255, 315 + y_plus, cla, img, 0.8)
#                         else:
#                             imgs_ = imgs_set_(205, 290, 255, 315, cla, img, 0.8)
#
#                 elif str(dun_name) == "talag":
#                     if black_laboratory == True:
#                         imgs_ = imgs_set_(205, 520 + y_plus, 255, 545 + y_plus, cla, img, 0.8)
#                     else:
#                         if event_dungeon == True:
#                             imgs_ = imgs_set_(205, 405 + y_plus, 255, 430 + y_plus, cla, img, 0.8)
#                         else:
#                             imgs_ = imgs_set_(205, 405, 255, 430, cla, img, 0.8)
#
#                 elif str(dun_name) == "soolyun":
#                     if black_laboratory == True:
#                         imgs_ = imgs_set_(205, 635, 255, 660, cla, img, 0.8)
#                     else:
#                         if event_dungeon == True:
#                             imgs_ = imgs_set_(205, 520 + y_plus, 255, 545 + y_plus, cla, img, 0.8)
#                         else:
#                             imgs_ = imgs_set_(205, 520, 255, 545, cla, img, 0.8)
#
#
#
#                 elif str(dun_name) == "event":
#                     imgs_ = imgs_set_(205, 175, 255, 205, cla, img, 0.8)
#
#
#
#                 if imgs_ is not None and imgs_ != False:
#                     print("dun_complete_1", imgs_)
#
#                     if str(dun_name) == "event":
#                         complete = True
#
#                     else:
#
#                         # 만료여부
#                         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_complete_2.PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         if str(dun_name) == "black":
#                             if black_laboratory == True:
#                                 imgs_ = imgs_set_(205, 195 + y_plus, 255, 225 + y_plus, cla, img, 0.8)
#                             else:
#                                 if event_dungeon == True:
#                                     imgs_ = imgs_set_(205, 620 + y_plus, 255, 650 + y_plus, cla, img, 0.8)
#                                 else:
#                                     imgs_ = imgs_set_(205, 620, 255, 650, cla, img, 0.8)
#
#                         elif str(dun_name) == "garbana":
#                             if black_laboratory == True:
#                                 imgs_ = imgs_set_(205, 310 + y_plus, 255, 335 + y_plus, cla, img, 0.8)
#                             else:
#                                 if event_dungeon == True:
#                                     imgs_ = imgs_set_(205, 195 + y_plus, 255, 225 + y_plus, cla, img, 0.8)
#                                 else:
#                                     imgs_ = imgs_set_(205, 195, 255, 220, cla, img, 0.8)
#
#                         elif str(dun_name) == "adoom":
#                             if black_laboratory == True:
#                                 imgs_ = imgs_set_(205, 425 + y_plus, 255, 450 + y_plus, cla, img, 0.8)
#                             else:
#                                 if event_dungeon == True:
#                                     imgs_ = imgs_set_(205, 310 + y_plus, 255, 335 + y_plus, cla, img, 0.8)
#                                 else:
#                                     imgs_ = imgs_set_(205, 310, 255, 335, cla, img, 0.8)
#
#                         elif str(dun_name) == "talag":
#                             if black_laboratory == True:
#                                 imgs_ = imgs_set_(205, 540 + y_plus, 255, 570 + y_plus, cla, img, 0.8)
#                             else:
#                                 if event_dungeon == True:
#                                     imgs_ = imgs_set_(205, 425 + y_plus, 255, 450 + y_plus, cla, img, 0.8)
#                                 else:
#                                     imgs_ = imgs_set_(205, 425, 255, 450, cla, img, 0.8)
#                         elif str(dun_name) == "soolyun":
#                             if black_laboratory == True:
#                                 imgs_ = imgs_set_(205, 655, 255, 685, cla, img, 0.8)
#                             else:
#                                 if event_dungeon == True:
#                                     imgs_ = imgs_set_(205, 540 + y_plus, 255, 565 + y_plus, cla, img, 0.8)
#                                 else:
#                                     imgs_ = imgs_set_(205, 540, 255, 565, cla, img, 0.8)
#
#
#
#
#
#                         if imgs_ is not None and imgs_ != False:
#                             print("dun_complete_2", imgs_)
#
#                             complete = True
#
#
#
#                 if complete == True:
#
#                     myQuest_play_add(cla, where)
#
#                 else:
#
#
#                     # 던전 클릭
#                     for i in range(5):
#                         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\dun_ready_check\\" + str(dun_name) + ".PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set_(500, 70, 800, 110, cla, img, 0.9)
#                         if imgs_ is not None and imgs_ != False:
#
#                             int_step = int(result_spot[2])
#
#                             if result_spot[1] == "가르바나지하수로":
#                                 if int_step > 2:
#                                     x_1 = 3
#                                 else:
#                                     x_1 = int_step
#
#                                 step_select(cla, x_1)
#
#                             elif result_spot[1] == "검은실험실":
#
#                                 if int_step > 5:
#                                     x_1 = 6
#                                 else:
#                                     x_1 = int_step
#
#                                 step_select(cla, x_1)
#
#                             elif result_spot[1] == "수련의전당":
#
#                                 if int_step > 4:
#                                     x_1 = 5
#                                 else:
#                                     x_1 = int_step
#
#                                 step_select(cla, x_1)
#
#
#                             else:
#                                 step_select(cla, result_spot[2])
#
#
#
#                             break
#                         else:
#                             click_pos_2(150, y_1, cla)
#                         time.sleep(0.5)
#
#                     # 던전 입장
#                     is_out = False
#                     for i in range(5):
#                         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
#                         if imgs_ is not None and imgs_ != False:
#                             print("dungeon", imgs_)
#                             click_pos_2(805, 1005, cla)
#                         else:
#                             for o in range(10):
#                                 result_out = out_check(cla)
#                                 if result_out == True:
#                                     is_out = True
#
#                                     break
#                                 else:
#                                     loading_check(cla)
#                                 time.sleep(0.5)
#                         if is_out == True:
#                             for o in range(3):
#                                 result_loading = loading_check(cla)
#                                 if result_loading == True:
#                                     break
#                                 time.sleep(0.2)
#                             break
#                         time.sleep(0.5)
#                     # 던전 입장 후
#
#                     # 가르바나 지하수로 일 경우 지도 체크 후 공격
#                     if str(dun_name) == "garbana":
#                         garbana_move(cla)
#                     attack_on(cla)
#                     time.sleep(0.2)
#                     juljun_on(cla)
#
#
#                     # for i in range(5):
#                     #     result_out = out_check(cla)
#                     #     if result_out == True:
#                     #         # 공격하고 절전모드 ㄱㄱ
#                     #         attack_on(cla)
#                     #         time.sleep(0.2)
#                     #         juljun_on(cla)
#                     #
#                     #         break
#                     #     else:
#                     #         loading_check(cla)
#                     #     time.sleep(0.5)
#
#             else:
#                 menu_open(cla)
#                 for i in range(10):
#                     full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\dungeon.PNG"
#                     img_array = np.fromfile(full_path, np.uint8)
#                     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                     imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.85)
#                     if imgs_ is not None and imgs_ != False:
#                         break
#                     else:
#                         full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\dungeon\\menu_dungeon.PNG"
#                         img_array = np.fromfile(full_path, np.uint8)
#                         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#                         imgs_ = imgs_set_(680, 190, 750, 290, cla, img, 0.7)
#                         if imgs_ is not None and imgs_ != False:
#                             print("menu_dungeon", imgs_)
#                             click_pos_reg(imgs_.x, imgs_.y, cla)
#                     time.sleep(0.3)
#             QTest.qWait(500)
#             # time.sleep(0.5)
#
#
#     except Exception as e:
#         print(e)
#         return 0