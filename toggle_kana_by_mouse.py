import pyautogui
import time

## 一番上のバーの設定をクリックする座標
# top_bar_input_setting_coord = (2847, 12)
# mozc_coord = (2847, 111)
# input_mode_coord = (2847, 163)
# kana_mode_coord = (2847, 234)

## 下の画面の設定をクリックする座標
top_bar_input_setting_coord = (2207, 1096)
mozc_coord = (2207, 1191)
input_mode_coord = (2207, 1245)
kana_mode_coord = (2207, 1316)

default_pause_time = 0.1


def my_click(*coord, pause=default_pause_time):
    time.sleep(pause)
    pyautogui.click(*coord)


def main():
    beginning_position = pyautogui.position()
    my_click(*top_bar_input_setting_coord)
    my_click(*mozc_coord)
    my_click(*top_bar_input_setting_coord)
    my_click(*input_mode_coord)
    my_click(*kana_mode_coord, pause=0.2)
    pyautogui.moveTo(*beginning_position)


main()
