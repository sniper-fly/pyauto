import pyautogui
import time

top_bar_input_setting_coord = (2841, 89)
mozc_coord = (2849, 183)
input_mode_coord = (2824, 230)
kana_mode_coord = (2834, 309)

default_pause_time = 0.1

def my_click(*coord, pause = default_pause_time):
  time.sleep(pause)
  pyautogui.click(*coord)

def main():
  beginning_position = pyautogui.position()
  my_click(*top_bar_input_setting_coord, pause=0)
  my_click(*mozc_coord)
  my_click(*top_bar_input_setting_coord, pause=0)
  my_click(*input_mode_coord)
  my_click(*kana_mode_coord)
  pyautogui.moveTo(*beginning_position)

main()
