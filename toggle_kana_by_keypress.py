import pyautogui
import time

default_sleep_time = 0.1

def my_hotkey(*args, default = default_sleep_time):
  time.sleep(default)
  pyautogui.hotkey(*args)

def my_press(*args, default = default_sleep_time):
  time.sleep(default)
  pyautogui.press(*args)

# focus on the top bar

my_hotkey('ctrl', 'alt', 'tab')

# move to the input mode field
my_hotkey('shift', 'tab')
my_hotkey('shift', 'tab')

# change the input mode to mozc
my_press('down')
my_press('down')
my_press('enter')

# change the input mode to kana

my_press('down')
my_press('down')
my_press('down')
my_press('enter')

my_press('down')
my_press('down')
my_press('enter')
