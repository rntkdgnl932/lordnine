import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_lordnine import skip_start
    from tuto_lordnine import way_check

    try:
        print("_stop_please")

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


def game_check(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg
    from action_lordnine import confirm_all
    from character_select_and_game_start import game_ready
    from massenger import line_to_me

    try:
        print("game_check")

        why = "none"

        is_error = False
        error_code = 0

        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\network_error.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 300, 670, 1000, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("network_error")
            is_error = True
            error_code = 1
            why = str(v_.this_game) + "네트워크 에러"
        else:
            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\long_time.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 500, 500, 600, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("long_time")
                error_code = 2
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\fix_ing.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 470, 500, 550, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("fix_ing")
                    is_error = True
                    error_code = 3
                    why = str(v_.this_game) + "점검진행"
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\fix_ing_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 470, 500, 550, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("fix_ing_2")
                        is_error = True
                        error_code = 3
                        why = str(v_.this_game) + "서버 안정화 점검진행"
                    else:
                        full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\code_201.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 470, 540, 650, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("code_201")
                            is_error = True
                            error_code = 4
                            why = str(v_.this_game) + "code 201 점검진행인듯"
                        else:
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\boan_failed_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 300, 800, 900, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("boan_failed_title")
                                is_error = True
                                error_code = 4
                                why = str(v_.this_game) + "보안체크 로드 실패"

        if error_code == 2:
            print("재접해보자")

            restart = True
            restart_count = 0

            while restart is True:
                restart_count += 1
                if restart_count > 7:
                    restart = False
                    why = "장시간 이었으나 재접속 실패..."
                    is_error = True

                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\game_start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(600, 900, 920, 1030, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    restart = False
                    why = "장시간 이었으나 재접속 성공"
                    print(why)
                    line_to_me(v_.now_cla, why)
                else:
                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\long_time.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 500, 500, 600, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        confirm_all(cla)


                        for i in range(30):
                            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\character_select_and_game_start\\touch_to_start.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 900, 660, 1000, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:

                                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\action\\skip\\out_skip.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 30, 960, 100, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\long_time.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(350, 500, 500, 600, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        confirm_all(cla)
                            time.sleep(1)


                    game_ready(cla)

                time.sleep(1)

        if is_error == True:

            full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\end_game_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 550, 650, 750, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("end_game_btn")
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\lordnine\\data_lordnine\\imgs\\check\\etc_check\\code_201.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(350, 470, 540, 650, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    confirm_all(cla)

            print(why)
            line_to_me(v_.now_cla, why)

            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
            file_path = dir_path + "\\start.txt"
            # cla.txt
            cla_data = str(v_.now_cla) + "cla"
            file_path2 = dir_path + "\\" + cla_data + ".txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = v_.now_cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)


    except Exception as e:
        print(e)
        return 0

