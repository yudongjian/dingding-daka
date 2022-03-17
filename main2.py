import uiautomator2 as u2
import time, datetime
from apscheduler.schedulers.blocking import BlockingScheduler

#d = u2.connect_usb('HMQ4C19A14003541')
d = u2.connect_wifi('10.42.141.6')


def try_exce(d, str):
    try:
        d(text=str).click()
        return True
    except Exception as e:
        print(e)
        return False



def click_daka(d):

    # 唤醒屏幕
    d.press("power")
    # 滑动解锁
    d.swipe(280, 1678, 790, 1678, steps=100)
    time.sleep(2)
    d.press("home")
    time.sleep(2)

    # 打开钉钉这个位置是不是应该设置一个try
    # 以防止其他人打开钉钉 直接大退到桌面
    d(text="钉钉").click()
    time.sleep(3)
    print('正在打开工作台...')
    d.click(0.485, 0.954)
    time.sleep(3)

    print('正在打开考勤打卡...')
    try_exce(d, "考勤打卡")
    d(text="考勤打卡").click()
    time.sleep(3)

    # 点击打卡
    print('正在点击打卡...')
    if datetime.datetime.now().hour == 8:
        d(text="上班打卡").click()
    else:
        d(text="下班打卡").click()
    time.sleep(8)
    d.press("back")
    time.sleep(3)
    d.press("back")
    time.sleep(2)
    d.press("back")
    time.sleep(2)


def send_message(d, message):
    # 思路 ： 打完卡发消息
    d.press("home")
    time.sleep(2)
    # 点击qq
    print('点击qq')
    d(text="QQ").click()
    time.sleep(8)
    # 点击置顶的人
    print('点击置顶')
    d.click(0.071, 0.194)
    # 点击选中文本框
    print('点击输入框')
    d.click(0.118, 0.935)
    print('输入消息')
    d.send_keys(message, clear=True)
    time.sleep(2)
    print('发送消息')
    d.click(0.892, 0.883)
    time.sleep(2)
    d.press("back")
    time.sleep(2)
    d.press("back")
    time.sleep(2)
    d.press("back")
    # 此时已经返回主页面，为了保证安全，多返回一次
    time.sleep(2)
    d.press("back")
    time.sleep(1)
    d.press("power")
    time.sleep(2)


def main():
    # 没打上要有报错，提示
    # 打卡三次提示
    count = 5
    while count > 0:
        try:
            print(datetime.datetime.now())
            click_daka(d)
            mes = "successful, 打卡成功"
            print(mes)
            send_message(d, mes)
            break
        except Exception as e:
            mes = "failed，打卡失败" + str(e)
            print(mes)
            try:
                send_message(d, mes)
            except Exception as e:
                print('发送消息失败...')
            count = count - 1


# if __name__ == "__main__":
#     sched = BlockingScheduler()  # 设置定时任务，周一至周五 上午8.50自动打上班卡，下午6.10自动打下班卡
#     sched.add_job(main, 'cron', day_of_week='mon-fri', hour='8', minute='30')
#     sched.add_job(main, 'cron', day_of_week='mon-fri', hour='18', minute='01')
#     sched.start()

main()