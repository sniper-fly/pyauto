import pyautogui
import time

# このページを翻訳、の座標を取得
# クリック
# キーボード 右入力
# キーボード ESC

default_pause_time = 0.1

x, y = pyautogui.locateCenterOnScreen('translate_button.png', grayscale=True)
beginning_cursor_position = pyautogui.position()
pyautogui.click(x, y)
time.sleep(default_pause_time)
pyautogui.press('right')
time.sleep(default_pause_time)
pyautogui.press('esc')
pyautogui.moveTo(beginning_cursor_position)
