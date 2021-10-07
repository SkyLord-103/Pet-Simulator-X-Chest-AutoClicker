import tkinter as tk
import pynput as pnt
import plyer
from plyer import notification
import win32api
import win32con
import keyboard
import time
import threading

# Variables
# AutoClicker default variables

_defaultMouseButton = 0  # Equals the index of _mousesToStr
_defaultMode = 2  # Equals the index of _mouseModesToStr
_defaultDelay = 100  # Delay will be measured in milliseconds
_defaultHoldDelay = 1  # milliseconds
_mousesToStr = ["Left", "Right", "Middle"]
_mouseModesToStr = ["Single", "Double", "Hold&Release"]

_activationKey = 'r'
_exitKey = 'ctrl+e'

WindowTitle = ": PyAuto by Sky City Studio"
WindowTitleActiveTag = ["Running", "Stopped"]

currentTime = time.time()


class Application(threading.Thread):
    def __init__(self):
        super(Application, self).__init__()
        self.ProgramRunning = True
        self.ActivelyClicking = False

        self.mouseButton = _defaultMouseButton
        self.mouseMode = _defaultMode
        self.clickDelay = _defaultDelay
        self.clickHoldDelay = _defaultHoldDelay

        self.currentTime = time.time()

        self.activationKey = _activationKey
        self.exitKey = _exitKey

        self._mouseButton = self.mouseButton
        self._mouseMode = _defaultMode
        self._clickDelay = _defaultDelay
        self._clickHoldDelay = _defaultHoldDelay
        self._currentTime = time.time()
        self._activationKey = _activationKey
        self._exitKey = _exitKey

        print(  # Printing The Current Configuration of The AutoClicker
            "Pet SimX AutoClicker by Sky City Studio",
            "\n",
            "\n",
            "Mouse Button: '{e}'".format(e=_mousesToStr[self.mouseButton]),
            "\n",
            "Click Mode: '{e}'".format(e=_mouseModesToStr[self.mouseMode]),
            "\n",
            "Click Delay: {e} milliseconds".format(e=self.clickDelay),
            "\n",
            "Click Hold Time: {e} milliseconds".format(e=_defaultHoldDelay),
            "\n"
        )
        notification.notify(
            title="SCS Auto",
            message="SCS Auto has started!\nPress: 'r' to start or stop clicking\nPress: 'ctrl+e' to exit the program",
            app_icon=None, timeout=4)

    def click(self, *args):
        self.mouseFunc()

    def changed(self):
        if self._mouseButton != self.mouseButton:
            pass

        self._mouseButton = self.mouseButton
        self._mouseMode = _defaultMode
        self._clickDelay = _defaultDelay
        self._clickHoldDelay = _defaultHoldDelay
        self._currentTime = time.time()
        self._activationKey = _activationKey
        self._exitKey = _exitKey

    def run(self):
        while self.ProgramRunning:
            self.changed()
            while self.ActivelyClicking:
                if (time.time() - self.currentTime) >= self.delay:
                    if self.mouseButton == 0:
                        mouse.leftSingle()
                        # mouse.leftDouble
                        # mouse.leftHold
                        # mouse.rightSingle
                    elif self.mouseButton == 1:
                        pass
                    elif self.mouseButton == 2:
                        mouse.holdNRelease(
                            self.mouseButton, self.clickHoldDelay)

                self.currentTime = time.time()

        time.sleep(0.1)


##############################################################################################
defaultClickDelay = 1
defaultMouseButton = 0  # 0: Left, 1: Right, 2: Middle
defaultClickMode = 2  # 0: Single, 1: Double, 2: Hold & Release
defaultHoldTime = 1

startStopKey = 'r'
exitKey = 'ctrl+e'

Modes = ["Left", "Right", "Middle"]
CModes = ["Single", "Double", "Hold&Release"]

windowTitleName = "SCS - AutoClicker 1.0"

# Classes


class AHHH(threading.Thread):
    def __init__(self):
        super(Application, self).__init__()
        self.MouseButton = defaultMouseButton
        self.Delay = defaultClickDelay

        self.MouseButton = 0
        self.MouseMode = 2

        self.programRunning = True
        self.running = False
        print(  # Printing The Current Configuration of The AutoClicker
            "Pet SimX AutoClicker by Sky City Studio",
            "\n",
            "\n",
            "Mouse Button: '{e}'".format(e=Modes[self.MouseButton]),
            "\n",
            "Click Mode: '{e}'".format(e=CModes[self.MouseMode]),
            "\n",
            "Click Delay: {e}'s".format(e=self.Delay),
            "\n",
            "Click Hold Time: {e}".format(e=defaultHoldTime),
            "\n"
        )

    def start_clicking(self):
        self.running = True
        print("RUNNING")

    def stop_clicking(self, e):
        self.running = False
        if e:
            print("EXITING")
        else:
            print("STOPPED")

    def exit(self):
        self.stop_clicking(True)
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
                App.stop_clicking(False)
            else:
                App.start_clicking()
    elif key == 0:
        App.exit()


keyboard.add_hotkey(startStopKey, on_pressed, args=[1],
                    suppress=False, timeout=0.1, trigger_on_release=False)
keyboard.add_hotkey(exitKey, on_pressed, args=[0],
                    suppress=False, timeout=0.1, trigger_on_release=False)
