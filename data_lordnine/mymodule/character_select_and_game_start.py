import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def game_start_screen(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me



    try:

        # 완전 바깥 화면인지 파악하며 기다리기
        game_ready(cla)


        # 실수로 새 캐릭터 클릭시...
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\character_create_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(750, 970, 920, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 이건 잘못 클릭시 나가기
            click_pos_2(25, 45, cla)
            print("class_select", imgs_)
            why = "캐릭 선택 잘 못 누름"
            line_to_me(cla, why)

            for i in range(10):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\confirm_btn_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 570, 640, 640, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

        # 캐릭터 선택 화면
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            character_change(cla, character_id)

        else:
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            elif cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            elif cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            elif cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
            elif cla == 'five':
                file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
            elif cla == 'six':
                file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

            same = False

            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_id = file.read()
                    if str(character_id) == str(read_id):
                        # 메뉴 안 열어도 됨
                        same = True
            if same == False:
                character_change(cla, character_id)


    except Exception as e:
        print(e)

def character_change(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_lordnine import out_check, menu_open, loading_check, go_maul

    from massenger import line_to_me
    try:



        print(str(character_id), "번으로 캐릭터 체인지")


        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

            # 실수로 새 캐릭터 클릭시...
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\character_create_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 970, 920, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 이건 잘못 클릭시 나가기
                click_pos_2(25, 45, cla)
                print("character_create_btn", imgs_)
                why = "캐릭 선택 잘 못 누름"
                line_to_me(cla, why)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\confirm\\confirm_btn_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(470, 570, 640, 640, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

            # 저장된 캐릭 번호 불러오기
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            elif cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            elif cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            elif cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
            elif cla == 'five':
                file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
            elif cla == 'six':
                file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

            # 캐릭터 선택 화면
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                x_reg = imgs_.x
                y_reg = imgs_.y

                # select 1 (150, 425)
                # select 2 (150, 475)

                y_click = 375 + (int(character_id) * 50)

                click_pos_2(150, y_click, cla)
                time.sleep(0.5)
                click_pos_reg(x_reg, y_reg, cla)
                time.sleep(0.1)

                #진입 버튼 누르면서 캐릭번호 저장하기
                save = False
                save_count = 0
                while save is False:
                    save_count += 1
                    if save_count > 15:
                        save = True
                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                save = True
                            else:
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(str(character_id))
                            time.sleep(0.3)
                    else:
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(character_id))

                # 대기 화면 있는지 확인하면서 진입확인하기
                joined = False
                joined_count = 0
                while joined is False:
                    joined_count += 1
                    if joined_count > 30:
                        joined = True

                    result_out = out_check(cla)
                    if result_out == True:
                        joined = True
                        cha_select = True

                        print("게임 접속 끝")
                        time.sleep(0.1)
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            x_reg = imgs_.x
                            y_reg = imgs_.y

                            # select 1 (150, 425)
                            # select 2 (150, 475)

                            y_click = 375 + (int(character_id) * 50)

                            click_pos_2(150, y_click, cla)
                            time.sleep(0.5)
                            click_pos_reg(x_reg, y_reg, cla)
                            time.sleep(0.1)
                        else:
                            loading_check(cla)

                    time.sleep(1)
            else:
                # 캐릭 번호와 체인지 하려는 번호 비교하기

                same = False

                if os.path.isfile(file_path) == True:
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        read_id = file.read()
                        if str(character_id) == str(read_id):
                            # 메뉴 안 열어도 됨
                            same = True
                            cha_select = True
                if same == False:

                    # 포션만 채우기(수집 분해도 함)

                    # 장비 빼기

                    # 마을부터 가서 메뉴 열기


                    go_maul(cla)

                    menu_open(cla)
                    time.sleep(1)


                    for i in range(20):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\menu\\character_change_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(860, 890, 960, 1000, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("character_change_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)


                else:
                    print("같은 번호의 캐릭이라서 체인지 안함")

    except Exception as e:
        print(e)

def game_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, text_check_get, int_put_, click_pos_reg
    from action_lordnine import confirm_all
    from massenger import line_to_me
    from clean_screen_lordnine import clean_screen_just_on_start

    try:

        ready_ = False

        # out_skip(character ready)
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\out_skip.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 380, 550, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("서버대기")
                ready_ = True
            else:
                down = False

                # 완전 바깥일 경우 일딴 들어가기(터치)
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\lordnine_mark.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 820, 540, 940, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("lordnine_mark")


                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(500, 500, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\path_down_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 400, 700, 500, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)

                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(500, 500, cla)
                            for i in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\path_down_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(250, 400, 700, 500, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)



                    result_confirm = confirm_all(cla)
                    if result_confirm == True:

                        for i in range(20):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\downloading_time.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 950, 300, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                down = True
                                break

                            time.sleep(0.5)
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\downloading_time.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 950, 300, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("downloading_time")
                            down = True
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\downloading_time.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 950, 300, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("downloading_time")
                        down = True
                if down == True:
                    down_count = 0
                    while down is True:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 900, 660, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            down = False
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                down = False
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(500, 500, cla)
                            down = False
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(500, 500, cla)
                                down = False
                            else:
                                down_count += 1
                                print("다운로드 중", down_count, "초")
                        time.sleep(1)

                is_touch = False
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_touch = True
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        is_touch = True
                if is_touch == True:
                    for i in range(20):
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(530, 900, 660, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(500, 500, cla)
                            else:
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(500, 500, cla)
                        time.sleep(0.5)

        # 완전 바깥일 경우 일딴 들어가기
        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(530, 900, 660, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            click_pos_reg(imgs_.x, imgs_.y, cla)

            detecter = False

            for i in range(10):

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\detecter_login.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 420, 600, 500, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    detecter = True
                time.sleep(0.5)

            if detecter == True:
                clean_screen_just_on_start(cla)

                why = "자동 로그인 방지"
                line_to_me(cla, why)

                dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
                file_path = dir_path + "\\start.txt"
                # cla.txt
                cla_data = str(cla) + "cla"
                file_path2 = dir_path + "\\" + cla_data + ".txt"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    data = 'no'
                    file.write(str(data))
                    time.sleep(0.2)
                with open(file_path2, "w", encoding='utf-8-sig') as file:
                    data = cla
                    file.write(str(data))
                    time.sleep(0.2)
                os.execl(sys.executable, sys.executable, *sys.argv)




            for i in range(10):
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_ready.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 380, 550, 450, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        ready_ = True
                        break
                time.sleep(0.5)

        else:
            # 최근 접속
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_select_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                for i in range(10):

                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_select_join_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(750, 400, 880, 450, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_select_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(350, 380, cla)
                    time.sleep(0.5)
            
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 380, 550, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                ready_ = True
            # else:
            #     confirm_all(cla)


        # 접속대기일 경우 기다리기
        game_ready_count = 0
        while ready_ is True:

            result = "none"

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\server_join_ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 380, 550, 450, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                game_ready_count += 5

                result = "none"
                result = text_check_get(505, 512, 560, 550, cla)
                result_num = int_put_(result)
                print("result", result_num)

                print("기다리는중", game_ready_count, "초, 대기순번 : ", result_num)


            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    ready_ = False
                    # 점검중일때만 켜기
                    why = str(game_ready_count) + "초 기다렸다. 대기열 끝나고 게임시작한다."
                    line_to_me(cla, why)
            time.sleep(5)



    except Exception as e:
        print(e)