from email.policy import default
import pyautogui
import time

default_sleep_time = 0.2

work_path = '/home/rnakai/work/hackathon/P2P-matching'

def my_press(*args, sleep_time = default_sleep_time):
  time.sleep(sleep_time)
  pyautogui.press(*args)

def my_write(*args, sleep_time = default_sleep_time):
  time.sleep(sleep_time)
  pyautogui.write(*args)
  pyautogui.press('enter')

pyautogui.press('win')
my_write('terminal', sleep_time=0.5)
my_write('cd ' + work_path, sleep_time=0.5)
my_write('pwd')
my_write('code .')
