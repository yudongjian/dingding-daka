import uiautomator2 as u2
import time
from apscheduler.schedulers.blocking import BlockingScheduler

d = u2.connect_usb('HMQ4C19A14003541')

def click_daka(d):
    # 唤醒屏幕
    d.press("power")
    # 滑动解锁
    d.swipe(280, 1678, 790, 1678, steps=100)
    # 点击 钉钉 d(text="钉钉").click()
    # d.click(0.665, 0.249)
    d(text="钉钉").click()
    time.sleep(3)
    # 点击工作台
    # d.click(0.503, 0.951)
    d(text="工作台").click()
    time.sleep(3)

    # 进入考勤打卡界面
    d.click(0.086, 0.542)
    d(text="考勤打卡").click()
    time.sleep(3)

    # 点击打卡
    d.click(0.46, 0.543)

click_daka(d)