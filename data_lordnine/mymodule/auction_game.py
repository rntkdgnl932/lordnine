import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:

        result_dia = 0
        result_silver = 0

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)

            result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
            result_text = change_number(result_text)
            result_dia = int_put_(result_text)
            result_dia_num = in_number_check(result_dia)
            print("result_text", result_dia_num, result_dia)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("silver_reg", imgs_)
            result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
            result_text2 = change_number(result_text2)
            result_silver = int_put_(result_text2)
            result_silver_num = in_number_check(result_silver)
            print("result_text2", result_silver_num, result_silver)

        if result_dia_num == True:

            return result_silver, result_dia

    except Exception as e:
        print(e)


def auction_start(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, out_check
    from clean_screen_lordnine import clean_screen_start
    from boonhae_collection import col_boon_start

    try:
        print("auction_start")

        # 팔기전에 콜렉션 및 분해 진행하기
        col_boon_start(cla)

        auction = False
        auction_count = 0

        while auction is False:
            auction_count += 1
            if auction_count > 6:
                auction = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)

                auction = True

                # 먼저 정산...
                auction_ready(cla)



                # 장비...및 스킬북
                click_pos_2(855, 120, cla)
                time.sleep(0.2)
                click_pos_2(855, 120, cla)
                time.sleep(0.2)

                result_full_list = auction_jangbi(cla)

                if result_full_list == False:

                    # 아이템...
                    click_pos_2(915, 120, cla)
                    time.sleep(0.2)
                    click_pos_2(915, 120, cla)
                    time.sleep(0.2)

                    auction_item(cla)

                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 150, 710, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                if get_point == False:
                    auction = True
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0



def auction_ready(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action_lordnine import menu_open, out_check
    from clean_screen_lordnine import clean_screen_start
    from boonhae_collection import col_boon_start

    try:
        print("auction_ready")


        auction = False
        auction_count = 0

        while auction is False:
            auction_count += 1
            if auction_count > 6:
                auction = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)

                auction = True

                # 먼저 정산...
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\scan_option_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 980, 150, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("scan_option_btn", imgs_)
                        break
                    time.sleep(1)

                # 정산하기
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\ilgwal_jungsan_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(820, 980, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("ilgwal_jungsan_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        break
                    else:
                        click_pos_2(250, 90, cla)
                    time.sleep(1)

                # 판매 실패한 상품 취소하기
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\auction_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 60, 290, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("auction_point_1", imgs_)


                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 150, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("sell_cancle", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y + 30, cla)
                        else:
                            drag_pos(540, 740, 540, 240, cla)
                    else:
                        break
                    time.sleep(0.5)

                # 팔기 준비
                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\scan_option_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 980, 150, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("scan_option_btn", imgs_)
                        break
                    else:
                        click_pos_2(50, 90, cla)
                    time.sleep(1)





            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 150, 710, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                if get_point == False:
                    auction = True
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def auction_jangbi(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, text_check_get_num, change_number_float
    from action_lordnine import menu_open, confirm_all

    try:
        print("auction_jangbi")

        anymore_sell = False

        auction = False
        auction_count = 0

        while auction is False:
            auction_count += 1
            if auction_count > 6:
                auction = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)

                auction = True




                # 장비...



                for i in range(10):
                    x_reg = 0
                    y_reg = 0

                    is_jangbi = False

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_jangbi\\list_q_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("list_q_1", imgs_)
                        x_reg = imgs_.x + 15
                        y_reg = imgs_.y + 15
                        is_jangbi = True
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_jangbi\\list_q_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("list_q_2", imgs_)
                            x_reg = imgs_.x + 15
                            y_reg = imgs_.y + 15
                            is_jangbi = True
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_jangbi\\skill_book_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(760, 130, 950, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("skill_book_1", imgs_)
                                x_reg = imgs_.x + 15
                                y_reg = imgs_.y + 15
                                is_jangbi = True

                    if is_jangbi == True:
                        print("팔자")

                        # 현재 최저가
                        low_price = 0
                        quantity = 0

                        # 해당 템 클릭
                        for s in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(650, 680, 755, 725, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("sell_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\diamond.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 360, 540, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\cancle.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 660, 470, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("cancle", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(710, 435, cla)
                                    else:
                                        click_pos_reg(x_reg, y_reg, cla)
                            time.sleep(0.5)

                        no_informaiton = False

                        # 현재 최저가 구하기

                        for s in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:

                                print("sell_title", imgs_)

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\no_information.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 530, 465, 565, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("no_information", imgs_)
                                    no_informaiton = True

                                else:
                                    low_price_1 = get_low_price(cla, "low")
                                    low_price_2 = get_low_price(cla, "yesterday")

                                    if int(low_price_1) > int(low_price_2):
                                        low_price = low_price_1
                                    else:
                                        low_price = (low_price_1 + low_price_2) / 2

                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(650, 680, 755, 725, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("sell_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        if no_informaiton == True:
                            for s in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("sell_title", imgs_)
                                    click_pos_2(710, 435, cla)
                                else:
                                    break
                                time.sleep(0.5)
                        else:
                            # 판매수량 구하기

                            quantity = 1

                            # 다이아 재화 선택하기
                            for s in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\diamond.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 360, 540, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("diamond", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(670, 470, cla)
                                    else:
                                        confirm_all(cla)
                                time.sleep(0.5)

                            # 계산하기

                            print("low_price", low_price)
                            print("quantity", quantity)

                            if low_price != 0:
                                result_price = int(low_price)
                                print("result_price", result_price)

                                if result_price > 10:
                                    print("판매하자")
                                    anymore_sell = sell_click(cla, result_price)


                    else:
                        print("접자")
                    time.sleep(0.5)


            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 150, 710, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                if get_point == False:
                    auction = True
            time.sleep(0.5)

        return anymore_sell

    except Exception as e:
        print(e)
        return 0


def auction_item(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2, text_check_get_num, change_number_float
    from action_lordnine import menu_open, confirm_all

    my_item = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_item"
    file_list = os.listdir(my_item)

    try:
        print("auction_item")

        anymore_sell = False

        auction = False
        auction_count = 0

        while auction is False:
            auction_count += 1
            if auction_count > 6:
                auction = True

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)

                auction = True

                # 아이템...

                # 판매시작
                for i in range(len(file_list)):
                    result_file_list = file_list[i].split(".")
                    read_data = result_file_list[0]

                    is_jangbi = False

                    x_reg = 0
                    y_reg = 0

                    # 종류 쭈욱 시작
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\list_item\\" + str(read_data) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 130, 950, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("item...", str(read_data), imgs_)
                        x_reg = imgs_.x
                        y_reg = imgs_.y
                        is_jangbi = True

                    if is_jangbi == True:
                        print("팔자")

                        # 현재 최저가
                        low_price = 0
                        quantity = 0

                        # 해당 템 클릭
                        for s in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(650, 680, 755, 725, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("sell_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\diamond.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 360, 540, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\cancle.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 660, 470, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("cancle", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(710, 435, cla)
                                    else:
                                        click_pos_reg(x_reg, y_reg, cla)
                            time.sleep(0.5)

                        # 현재 최저가 구하기

                        no_informaiton = False

                        for s in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("sell_title", imgs_)

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\no_information.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 530, 465, 565, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("no_information", imgs_)
                                    no_informaiton = True

                                else:
                                    low_price_1 = get_low_price(cla, "low")
                                    low_price_2 = get_low_price(cla, "yesterday")

                                    if int(low_price_1) > int(low_price_2):
                                        low_price = low_price_1
                                    else:
                                        low_price = (low_price_1 + low_price_2) / 2

                                break
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(650, 680, 755, 725, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("sell_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)


                        if no_informaiton == True:
                            for s in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("sell_title", imgs_)
                                    click_pos_2(710, 435, cla)
                                else:
                                    break
                                time.sleep(0.5)
                        else:
                            # 판매수량 구하기
                            for s in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\diamond.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 360, 540, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\cancle.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 660, 470, 700, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("cancle", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\max.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(510, 620, 580, 660, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("max", imgs_)

                                        result_many_ = 0

                                        for r in range(3):
                                            result_many_ready = text_check_get_num(420, 465, 520, 492, cla)
                                            print("result_many_ready", result_many_ready)

                                            result_many_ready = result_many_ready.replace('\n', '')

                                            if result_many_ready != "":

                                                result_many_ready = change_number_float(result_many_ready)
                                                print("result_price_change", result_many_ready)

                                                result_many_ = float(result_many_ready)
                                                print("result_many_", result_many_)

                                                if result_many_ == 1:
                                                    print("숫자 1")
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    time.sleep(0.5)
                                                else:
                                                    print("숫자 1 아니다")
                                                    break
                                            time.sleep(0.5)
                                        if result_many_ != 0:

                                            print(type(result_many_))

                                            if str(type(result_many_)) == "<class 'float'>":
                                                print("숫자", result_many_)
                                                quantity = result_many_
                                            else:
                                                print("숫자 아니다. 망했다.")

                                            for t in range(10):
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    break
                                                else:
                                                    confirm_all(cla)
                                                time.sleep(0.5)

                                        break
                                    else:
                                        click_pos_2(670, 500, cla)
                                time.sleep(0.5)
                            # 다이아 재화 선택하기
                            for s in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\diamond.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 360, 540, 410, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("diamond", imgs_)
                                    break
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(670, 470, cla)
                                    else:
                                        confirm_all(cla)
                                time.sleep(0.5)

                            # 계산하기

                            print("low_price", low_price)
                            print("quantity", quantity)

                            if low_price != 0 and quantity != 0:
                                result_price = int(low_price * quantity)
                                print("result_price", result_price)

                                if result_price > 10:
                                    print("판매하자")
                                    anymore_sell = sell_click(cla, result_price)
                    else:
                        print("접자")
                    time.sleep(0.5)


            else:

                menu_open(cla)

                get_point = False

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        get_point = True
                        break

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 150, 710, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                if get_point == False:
                    auction = True
            time.sleep(0.5)

        return anymore_sell

    except Exception as e:
        print(e)
        return 0




def get_low_price(cla, data):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_reg

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960
    if cla == 'three':
        plus = 960 * 2
    if cla == 'four':
        plus = 960 * 3
    if cla == 'five':
        plus = 960 * 4
    if cla == 'six':
        plus = 960 * 5

    try:
        print("get_low_price", data)

        x_1 = 400 + plus
        x_2 = 456 + plus

        if data == "low":
            y_1 = 542
            y_2 = 560
        elif data == "yesterday":
            # test
            y_1 = 574
            y_2 = 597

        point_reg = 0
        is_point = False

        #
        result_min = 0
        list_x = []
        for i in range(10):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("x_1", i, imgs_)
                list_x.append(imgs_.x)
                print("list_x", list_x)
                result_min = min(list_x)
        print("result_min", result_min)
        x_1 = result_min - 5
        x_2 = x_1 + 10

        # x_1 = result_min - 7
        # x_2 = x_1 + 12

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\num_point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_reg(415 + plus, y_1, 455 + plus, y_2, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("num_point", imgs_)
            point_reg = imgs_.x
            is_point = True
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\num_point2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(415 + plus, y_1, 455 + plus, y_2, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("num_point2", imgs_)
                point_reg = imgs_.x
                is_point = True
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\num_point3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_reg(415 + plus, y_1, 455 + plus, y_2, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("num_point3", imgs_)
                    point_reg = imgs_.x
                    is_point = True


        print("################")
        print("x_1", x_1)
        print("x_2", x_2)
        print("################")

        # 소수점 이전
        num = False
        num_count = 0
        result_num = ""
        while num is False:
            # print("x_1...", x_1, num_count)
            # print("num_count...", num_count)
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\price_num\\" + str(num_count) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("is num...", str(num_count), imgs_)

                if str(num_count) == "4":
                    x_1 = imgs_.x # - 1

                # elif str(num_count) == "1":
                #     x_1 = imgs_.x + 1

                else:
                    x_1 = imgs_.x - 1
                x_2 = x_1 + 10

                if is_point == True:
                    if imgs_.x > point_reg:
                        num = True
                    else:
                        result_num += str(num_count)
                else:
                    result_num += str(num_count)
                # print("result_num...", result_num)
                num_count = 0
            else:
                num_count += 1
                if num_count > 9:
                    num = True

        # 소수점 이후
        if is_point == True:

            x_1 = point_reg - 2
            x_2 = x_1 + 9

            result_num += "."

            print("result_num(point)", result_num)

            num = False
            num_count = 0
            while num is False:
                # print("x_1...", x_1, num_count)
                # print("num_count...", num_count)
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\price_num\\" + str(
                    num_count) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("is num...", str(num_count), imgs_)

                    if str(num_count) == "4":
                        x_1 = imgs_.x  # - 1
                    else:
                        x_1 = imgs_.x - 1
                    x_2 = x_1 + 10
                    result_num += str(num_count)
                    # print("result_num...", result_num)
                    num_count = 0
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\price_num\\1_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("is num...1",  imgs_)

                        x_1 = imgs_.x - 1
                        x_2 = x_1 + 10
                        result_num += "1"
                        # print("result_num...", result_num)
                        num_count = 0

                    else:
                        num_count += 1
                        if num_count > 9:
                            num = True
        result_num = float(result_num)
        print("result_num", result_num)


        return result_num
    except Exception as e:
        print(e)
        return 0




def sell_click(cla, result_price):
    import numpy as np
    import cv2
    import os

    from function_game import click_pos_2, text_check_get_num, change_number_float, imgs_set_, click_pos_reg
    from action_lordnine import confirm_all

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960
    if cla == 'three':
        plus = 960 * 2
    if cla == 'four':
        plus = 960 * 3
    if cla == 'five':
        plus = 960 * 4
    if cla == 'six':
        plus = 960 * 5

    try:
        print("sell_click", result_price)

        anymore_sell = False

        for i in range(5):



            result_price_str = str(result_price)
            for n in range(len(result_price_str)):

                num_x = 400  # 50
                num_y = 535  # 35

                print(n + 1, result_price_str[n])
                if int(result_price_str[n]) == 2 or int(result_price_str[n]) == 5 or int(
                        result_price_str[n]) == 8 or int(result_price_str[n]) == 0:
                    num_x = 450
                elif int(result_price_str[n]) == 3 or int(result_price_str[n]) == 6 or int(
                        result_price_str[n]) == 9:
                    num_x = 500

                if int(result_price_str[n]) == 4 or int(result_price_str[n]) == 5 or int(
                        result_price_str[n]) == 6:
                    num_y = 570
                elif int(result_price_str[n]) == 7 or int(result_price_str[n]) == 8 or int(
                        result_price_str[n]) == 9:
                    num_y = 605
                elif int(result_price_str[n]) == 0:
                    num_y = 640
                click_pos_2(num_x, num_y, cla)
                time.sleep(0.3)

            # 클릭한거랑 계산된거랑 비교해서 같으면 확인
            time.sleep(0.2)
            result_many_ready = text_check_get_num(420, 465, 520, 492, cla)
            print("result_many_ready", result_many_ready)

            result_many_ready = result_many_ready.replace('\n', '')

            if result_many_ready != "":
                result_many_ready = change_number_float(result_many_ready)
                print("result_price_change", result_many_ready)

                result_many_ = int(result_many_ready)
                print("result_many_", result_many_)

            if result_price == result_many_:
                print("오케이!!!!!!!!", result_price, result_many_)
                confirm_all(cla)
                break
            else:
                print("다시 누르자")
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\diamond.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 360, 540, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("diamond", imgs_)
                    click_pos_2(500, 645, cla)

            time.sleep(0.5)

        for i in range(7):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            else:
                confirm_all(cla)


            time.sleep(0.5)

        for i in range(5):


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 410, 520, 460, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_enroll_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 600, 540, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sell_enroll_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 370, 520, 405, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_title2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 370, 520, 405, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\sell_enroll_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 600, 540, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("sell_enroll_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

        for i in range(5):
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\auction\\auction_list_full.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 100, 660, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("auction_list_full", imgs_)
                anymore_sell = True
                break
            time.sleep(0.1)

        return anymore_sell

    except Exception as e:
        print(e)
        return 0


