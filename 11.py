import os
def pull_screenshot():
    out1=os.popen('adb shell screencap -p /sdcard/autojump.png')
    out2=os.popen('adb pull /sdcard/autojump.png .')
    print(out1.read())
    print(out2.read())
pull_screenshot()