import webbrowser
import pyautogui
import time
import pyimgur
from twilio.rest import Client


def is_loaded():
    while True:
        if not pyautogui.locateOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/loading.png'):
            return True


def first_login():
    locate = pyautogui.locateCenterOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/first_login_submit.png')
    if locate:
        pyautogui.moveTo(locate)
        pyautogui.click()
    elif pyautogui.locateCenterOnScreen('E:\PyCharmProjects\ScheduleGrabber\images\schedules_link.png'):
        pass
    else:
        first_login()


def go_to_schedules():
    locate = pyautogui.locateCenterOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/schedules_link.png')
    if locate:
        pyautogui.moveTo(locate)
        pyautogui.click()
    else:
        go_to_schedules()


def second_login():
    locate = pyautogui.locateOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/second_login_submit.png')
    if locate:
        pyautogui.moveTo(locate)
        pyautogui.click()
    elif pyautogui.locateCenterOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/schedule_dropdown.png'):
        pass
    else:
        second_login()


def get_schedules():
    for i in range(1, 4):
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/schedule_dropdown.png'))
        pyautogui.click()
        time.sleep(1)
        pyautogui.keyDown('down')
        pyautogui.keyDown('return')
        locate_run_button = pyautogui.locateCenterOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/first_run_report.png')
        if locate_run_button:
            pyautogui.moveTo(locate_run_button)
            pyautogui.click()
        else:
            locate_run_button = pyautogui.locateCenterOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/second_run_report.png')
            pyautogui.moveTo(locate_run_button)
            pyautogui.click()
        time.sleep(5)
        if is_loaded():
            pyautogui.moveTo(pyautogui.locateOnScreen('E:/PyCharmProjects/ScheduleGrabber/images/focusing_element.png'))
            pyautogui.click()
            pyautogui.keyDown('pagedown')
            time.sleep(1)
            pyautogui.screenshot(f'E:/PyCharmProjects/ScheduleGrabber/images/schedules/week_{i}.png', (603, 479, 407, 278))


def send_schedules():
    twilio_account_sid = 'ACb936365585fe401cefcbf6d388a51b1d'
    twilio_auth_token = '7e79d15300158f21e3ee724866ca3b07'
    imgur_client_id = '6ccd1be5e1ac5bb'
    to_number = '+19164106323'
    from_number = '+12029196615'
    client = Client(twilio_account_sid, twilio_auth_token)
    imgur = pyimgur.Imgur(imgur_client_id)
    for i in range(1, 4):
        path = f'E:/PyCharmProjects/ScheduleGrabber/images/schedules/week_{i}.png'
        uploaded_image = imgur.upload_image(path, title=f'Upload #{i}')
        img_url = uploaded_image.link
        client.api.account.messages.create(to=to_number,
                                           from_=from_number,
                                           body=f'Week {i}',
                                           media_url=img_url)


def run_program():
    webbrowser.open('https://ess.costco.com')
    time.sleep(5)
    first_login()
    go_to_schedules()
    second_login()
    get_schedules()
    send_schedules()


if __name__ == '__main__':
    run_program()
