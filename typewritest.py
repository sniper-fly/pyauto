import time
import pyautogui
import pyperclip
import subprocess


def safe_paste(text: str):
    # 1. クリップボードの現在の内容を保存
    original_clipboard = pyperclip.paste()

    # 2. 指定したテキストをコピー
    pyperclip.copy(text)

    # if is_terminal_focused():
    #     # 3. ターミナルの場合、シフト+Ctrl+Vで貼り付け
    #     pyautogui.hotkey("shift", "ctrl", "v")
    # else:
    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.1)

    # 4. クリップボードを元に戻す
    pyperclip.copy(original_clipboard)


def get_focused_window_class():
    window_class = subprocess.run(
        ["xdotool", "getactivewindow", "getwindowclassname"],
        capture_output=True,
        text=True,
    ).stdout.strip()
    # window_class = subprocess.run(
    #     ["xprop", "-id", window_id, "WM_CLASS"], capture_output=True, text=True
    # ).stdout
    return window_class.lower()


def is_terminal_focused():
    terminal_classes = [
        "gnome-terminal",
    ]
    window_class = get_focused_window_class()
    return any(term in window_class for term in terminal_classes)


safe_paste("こんにちは、世界！")
