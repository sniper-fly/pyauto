import pyautogui
import time

top_bar_input_setting_coord = (2847, 12)
mozc_coord = (2847, 111)
input_mode_coord = (2847, 163)
kana_mode_coord = (2847, 234)

default_pause_time = 0.1

def my_click(*coord, pause = default_pause_time):
  time.sleep(pause)
  pyautogui.click(*coord)

def main():
  beginning_position = pyautogui.position()
  my_click(*top_bar_input_setting_coord)
  my_click(*mozc_coord)
  my_click(*top_bar_input_setting_coord)
  my_click(*input_mode_coord)
  my_click(*kana_mode_coord)
  pyautogui.moveTo(*beginning_position)

main()
