#Author:Error063
#last update on 2020/11/20

from os import system as term
from os import name as systype

unix = str("~/Desktop")
windows = str("%USERPROFILE%/Desktop")
android = str("/sdcard")

adb = str("adb ")

class cmd():    #用户自定义adb命令（包括Linux shell命令行）

    def adb(cmd):
        term("adb " + str(cmd))

    def shell(cmd):
        term("adb shell " + str(cmd))    ##

class status():    #用来控制adb server的开关

    def start(self):
        term("adb start-server")

    def kill(self):
        term("adb kill-server")

    def restart(self):
        term("adb restart-server")

class device():    #用来管理已连接的设备、连接网络adb设备和开启网络adb

    def list(self):
        term("adb device")

    def connect(ip,port):
        if port == "":    #为无输入设置默认值，下同
            port = 5555
        term("adb connect " + str(ip) + ":" + str(port))
        ip = ""    #重置ip的状态，下同
        port = ""

    def disconnect(ip,port):
        if port == "":
            port = 5555
        term("adb disconnect" + str(ip) + ":" + str(port))
        ip = ""
        port = ""

    def netadb(port):
        if port == "":
            port=5555
        term("adb tcpip" + str(port))
        port = ""

class application():    #用来安装、卸载和停止等管理设备上应用

    def list(method):
        if method == "":
            term("adb shell pm list packages")
        elif method == "3" or method == "third":
            term("adb shell pm list packages -3")
        elif method == "s" or method == "system" or method == "builtin":
            term("adb shell pm list packages -s")
        elif method == "e" or method == "enabled":
            term("adb shell pm list packages -e")
        elif method == "d" or method == "disabled":
            term("adb shell pm list packages -d")
        else:
            term("adb shell pm list packages " + str(method))

    def install(path,method):
        if method == "":
            term("adb install " + str(path))
        elif method == "r":
            term("adb install -r " + str(path))
        elif method == "g":
            term("adb install -g " + str(path))
        elif method == "rg" or method == "gr":
            term("adb install -r -g " + str(path))
        else:
            term("adb install -" +str(method) + " " + str(path))

    def uninstall(packagename,method):
        if method == "":
            term("adb uninstall " + str(packagename))
        elif method == "k":
            term("adb uninstall -k " + str(packagename))
        else:
            term("adb uninstall -" +str(method) + " " + str(packagename))

    def path(packagename):
        term("adb shell pm path " + str(packagename))

    def stop(packagename):
        term("adb shell am force-stop " + str(packagename))

    def clear(packagename):
        term("adb shell pm clear " + str(packagename))

    def disable(packagename):
        term("adb shell pm disable-user " + str(packagename))

    def enable(packagename):
        term("adb shell pm enable " + str(packagename))

    def open(packagename,activity):
        if activity == "":
            activity = ".MainActivity"
        term("adb shell am start -n " + str(packagename) + "/" + str(activity))
        activity = ""

class input():    #用来控制设备触屏、发送文字（仅英文字符、数字及一些符号）和模拟按键

    def text(text):
        term("adb shell input text " + str(text))

    def tap(x,y):
        term("adb shell input tap " + str(x) + " " + str(y))

    def swipe(fromx,fromy,tox,toy):
        term("adb shell input swipe " + str(fromx) + " " + str(fromy) + " " + str(tox) + " " + str(toy))

    def keyevent(keycode):
        if keycode == "home":
            keycode = str(3)
        elif keycode == "back":
            keycode = str(4)
        elif keycode == "swich":
            keycode = str(187)
        elif keycode == "menu":
            keycode = str(82)
        elif keycode == "mute":
            keycode = str(164)
        elif keycode == "assistant":
            keycode = str(231)
        elif keycode == "power":
            keycode = str(26)
        elif keycode == "del":
            keycode = str(67)
        elif keycode == "volup":
            keycode = str(24)
        elif keycode == "voldown":
            keycode = str(25)
        term("adb shell input " + str(keycode))

class screen():    #用来调整屏幕分辨率和dpi以及截屏和录屏

    def size(size):
        if size == "get":
            term("adb shell wm size")
        else:
            term("adb shell wm size " + str(size))

    def dpi(size):
        if size == "get":
            term("adb shell wm density")
        else:
            term("adb shell wm density " + str(size))

    def cap(top,keep,fname):
        if top == "":
            if type() == "posix":    #检测操作系统类型，posix为unix，nt为windows，下同
                top = unix
            elif type() == "nt":
                top = windows
        if fname == "":
            fname = "sc"
        term("adb shell screencap -p /sdcard/" + str(fname) + ".png")
        term("adb pull /sdcard/" + str(fname) + ".png" + str(top))
        if keep == "n" or keep == "no":
            term("adb shell rm -rf /sdcard/" + str(fname) + ".png")

    def rec(top,keep,fname):
        if top == "":
            if type() == "posix":
                top = unix
            elif type() == "nt":
                top = windows
        if fname == "":
            fname = "sc"
        term("adb shell screenrecord /sdcard/" + str(fname) + ".mp4")
        term("adb pull /sdcard/" + str(fname) + ".mp4" + str(top))
        if keep == "n" or keep == "no" or keep == "":
            term("adb shell rm -rf /sdcard/" + str(fname) + ".mp4")


class ime():

    def enable(pid):
        term("adb shell ime enable " + str(pid))

    def set(pid):
        term("adb shell ime set " + str(pid))

    def list(self):
        term("adb shell ime list -a")

class backup():

    def sdcard(top):
        if top == "":
            if systype() == "posix":
                top = unix
            elif systype() == "nt":
                top = windows
        term("adb pull /sdcard " + str(output))

class file():

    def pull(fromp,top):
        if top == "":
            if systype() == "posix":
                top = unix
            elif systype() == "nt":
                top = windows
        term("adb pull " + str(fromp) + str(top))

    def push(fromp,top):
        if top =="":
            top = android
        term("adb push " + str(fromp) + str(top))

class power():

    def shutdown(self):
        term("adb shell reboot -p")

    @property
    def reboot(method):
        if method == "normal":
            term("adb shell reboot")
        elif method == "recovey":
            term("adb shell reboot recovey")
        elif method == "fastboot":
            term("adb shell reboot fastboot")
        elif method == "edl":
            term("adb shell reboot edl")
        else:
            term("adb shell reboot" + str(method))

    def powerkey(self):
        term("adb shell input keyevent 26")

    def battery_level_set(level):
        term("adb shell dumpsys battery set level " + str(level))

    def virtual_plug(status):
        if status == True:
            term("adb shell dumpsys battery plug")
        elif status == False:
            term("adb shell dumpsys battery unplug")
        else:
            return error

    def reset(self):
        term("adb shell dumpsys battery reset")

class setting():

    def bt_on(status):
        if status == True:
            term("adb shell service call bluetooth_manager 6")
        elif status == False:
            term("adb shell service call bluetooth_manager 9")
        else:
            return error

    def wifi_on(status):
        if status == True:
            term("adb shell svc wifi enable")
        elif status == False:
            term("adb shell svc wifi disable")
        else:
            return error

    def screen_stay_on(status):
        if status == "ture":
            term("adb shell svc power stayon true")
        elif status == "false":
            term("adb shell svc power stayon false")
        elif status == "usb":
            term("adb shell svc power stayon usb")
        elif status == "ac":
            term("adb shell svc power stayon ac")
        elif status == "wireless":
            term("adb shell svc power stayon wireless")
        else:
            return error

    @property
    def screen_brightness(status):
        if status == "get":
            term("adb shell settings get system screen_brightness")
        elif 255 >= status >= 0:
            term("adb shell settings put system screen_brightness " + str(status))
        else:
            return error

    def screen_off_timeout(status):
        if status == "get":
            term("adb shell settings get system screen_off_timeout")
        else:
            term("adb shell settings put system screen_off_timeout " + str(status))