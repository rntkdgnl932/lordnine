import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def power_up_sungmool(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import menu_open, confirm_all
    from clean_screen_lordnine import clean_screen_start

    try:
        print("power_up_sungmool")

        sungmool = True
        sungmool_count = 0

        while sungmool is True:
            sungmool_count += 1
            if sungmool_count > 6:
                sungmool = False


            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sungmool.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("sungmool", imgs_)

                sungmool = False

                # 차례대로 성물 등록하쟈
                # 110, 110 180 250

                # for 로 3개짜리 씌우자자



                for list in range(3):
                    num = list + 1

                    up_start = False

                    is_break = False

                    print("num......................", num)

                    for i in range(10):
                        # 활성화 되어 있음
                        # 오른쪽 성물 리스트 확인
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\list_" + str(num) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 100, 880, 160, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("list_ : ", str(num), imgs_)
                            up_start = True
                        else:
                            # 활성화 되어 안 되어 있음
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\hwalsunghwa_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(780, 980, 880, 1030, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("hwalsunghwa_btn", imgs_)


                                for h in range(10):
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\hwalsunghwa_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 400, 550, 500, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("hwalsunghwa_title", imgs_)
                                        result_confirm = confirm_all(cla)
                                        if result_confirm == True:
                                            for c in range(10):
                                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\not_enough_item.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(300, 100, 550, 160, cla, img, 0.7)
                                                if imgs_ is not None and imgs_ != False:
                                                    # 활성화 시킬 아이템이 없음
                                                    print("아이템 없지롱")
                                                    is_break = True
                                                    break
                                                else:
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\ganghwa_btn_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(700, 985, 860, 1030, cla, img, 0.7)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("ganghwa_btn_1", imgs_)
                                                        up_start = True
                                                        break
                                                time.sleep(0.1)
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\hwalsunghwa_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(780, 980, 880, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)

                                    if is_break == True:
                                        print("hwalsunghwa_btn...break")
                                        break

                                    time.sleep(0.5)
                            else:
                                # 왼쪽 성물 리스트 누름
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\list_" + str(num) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 75, 160, 270, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("list_ ... : ", str(num), imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                        if is_break == True:
                            print("is_break", num)
                            break
                        elif up_start == True:
                            print("up_start", num)


                            up_end = True

                            for g in range(10):
                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\ganghwa_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(770, 70, 885, 115, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("ganghwa_title", imgs_)

                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\ganghwa_btn_ilgwal.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(840, 985, 940, 1030, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("ganghwa_btn_ilgwal", imgs_)

                                        for c in range(5):
                                            result_g_confirm = confirm_all(cla)
                                            if result_g_confirm == True:
                                                up_end = False

                                                time.sleep(3)

                                                for b in range(10):
                                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\ganghwa_btn_ilgwal.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(840, 985, 940, 1030, cla, img, 0.8)
                                                    if imgs_ is not None and imgs_ != False:
                                                        break
                                                    time.sleep(1)

                                                break
                                            else:
                                                up_end = True
                                            time.sleep(0.2)
                                        if up_end == True:
                                            print("up_end in..", up_end)
                                            break
                                        else:
                                            print("up_end in....", up_end)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\ganghwa_btn_ilgwal.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(840, 985, 940, 1030, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("ganghwa_btn_ilgwal", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\ganghwa_btn_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(700, 985, 860, 1030, cla, img, 0.7)
                                        if imgs_ is not None and imgs_ != False:
                                            print("ganghwa_btn_1", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)

                            if up_end == True:
                                print("up_end out..", up_end)
                                break
                            else:
                                print("up_end out....", up_end)

                        time.sleep(0.5)
                    time.sleep(0.3)


                # 마무리 나가기
                clean_screen_start(cla)

            else:

                menu_open(cla)

                for i in range(10):
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\title\\sungmool.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\power_up\\menu_sungmool.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(720, 200, 790, 280, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0


