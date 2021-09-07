import tkinter as tk
import pynput as pnt
from pynotifier import Notification as notif
import win32api
import win32con
import keyboard
import time
import threading


# Variables
defaultClickDelay = 1
defaultMouseButton = 0  # 0: Left, 1: Right, 2: Middle
defaultClickMode = 2  # 0: Single, 1: Double, 2: Hold & Release
defaultHoldTime = 1

startStopKey = 'r'
exitKey = 'ctrl+e'

Modes = ["Left", "Right", "Middle"]
CModes = ["Single", "Double", "Hold&Release"]

windowTitleName = "SCS - AutoClicker 1.1"

# Classes


class Application(threading.Thread):
    def __init__(self):
        super(Application, self).__init__()
        self.mouseButton = defaultMouseButton
        self.delay = defaultClickDelay
        self.programRunning = True
        self.running = False

        print(  # Printing The Current Configuration of The AutoClicker
            "Pet SimX AutoClicker by Sky City Studio",
            "\n",
            "\n",
            "Start/Stop Key: '{e}'".format(e=startStopKey),
            "\n",
            "Exit Key: '{e}'".format(e=exitKey),
            "\n",
            "Mouse Button: '{e}'".format(e=Modes[self.mouseButton]),
            "\n",
            "Click Mode: '{e}'".format(e=CModes[defaultClickMode]),
            "\n",
            "Click Delay: {e} seconds".format(e=self.delay),
            "\n",
            "Click Hold Time: {e} seconds".format(e=defaultHoldTime),
            "\n"
        )
        notif(
            title=windowTitleName,
            description="Start/Stop Key: '{a}', Exit Key: '{b}'\nMouse Button: '{c}', Click Mode: '{d}'\nClick Delay: {e} seconds, Click Hold Time: {f} seconds".format(
                a=startStopKey,
                b=exitKey,
                c=Modes[self.mouseButton],
                d=CModes[defaultClickMode],
                e=self.delay,
                f=defaultHoldTime
            ),
            icon_path=None,
            duration=5,
            urgency='normal'
        ).send()

    def start_clicking(self):
        self.running = True
        print("RUNNING")

    def stop_clicking(self, e=None):
        self.running = False
        if e == None:
            print("STOPPED")

    def exit(self):
        self.stop_clicking(True)
        print("EXITING")
        self.programRunning = False

    def run(self):
        while self.programRunning:
            while self.running:
                if defaultClickMode == 2:
                    mouse.holdNRelease(
                        defaultMouseButton, defaultHoldTime)
                    time.sleep(self.delay)
                else:
                    mouse.singleClick(defaultMouseButton)
                    time.sleep(self.delay)

            time.sleep(0.1)


class Mouse(threading.Thread):
    def __init__(self):
        super(Mouse, self).__init__()

    def moveTo(x, y):
        pass

    def singleClick(self, btn=int):
        if btn == 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        elif btn == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        elif btn == 2:
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

    def doubleClick(self, btn=int):
        if btn == 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        elif btn == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        elif btn == 2:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.1)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def holdNRelease(self, btn=int, hold=float):
        if btn == 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(hold)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        elif btn == 1:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            time.sleep(hold)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        elif btn == 2:
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
            time.sleep(hold)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)


# Startup etc.
mouse = Mouse()
mouse.start()

App = Application()
App.start()


def on_pressed(key):
    if key == 1:
        if App.programRunning:
            if App.running:
                App.stop_clicking(None)
            else:
                App.start_clicking()
    elif key == 0:
        App.exit()


keyboard.add_hotkey(startStopKey, on_pressed, args=[1],
                    suppress=True, timeout=0.1, trigger_on_release=False)
keyboard.add_hotkey(exitKey, on_pressed, args=[0],
                    suppress=True, timeout=0.1, trigger_on_release=False)
