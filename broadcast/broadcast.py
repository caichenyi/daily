# encoding: utf-8
# Author: Cai Chenyi
from _api import getinfo
from _email import sendemail
from _voice import speak

import sys


def jiraSpeak(url_path, tl_path, action, message_title, subject, cc, loop_time, mail_func=False, speak_func=False):
    api_list = getinfo.apiList(url_path)
    api_info = getinfo.apiInfo(api_list, action)
    if api_info != {}:
        message_mail = message_speak = message_title
        receivers = getinfo.getReceivers(tl_path, api_info, cc)
        for i in list(api_info.values()):
            message_mail += '\n{}:{}:{}:{}'.format(i['assignee'], i['component'], i['key'], i['summary'])
            if action == 4:
                message_speak += '\n任务{key}，请{name}赶紧处理。'.format(key=i['key'].split('-')[1], name=i['assignee'])
            else:
                message_speak += '\n缺陷{key}，请{name}赶紧处理。'.format(key=i['key'].split('-')[1], name=i['assignee'])
        print(message_speak)
        if mail_func:
            sendemail.sendEmail('files\\smtp.txt', receivers, subject=subject, content=message_mail)
        if speak_func:
            speak.txetSpeak(message_speak, loop_time)


if __name__ == '__main__':
    url_path = 'files\\url.txt'
    tl_path = 'files\\TL.txt'
    cc = 'aner.li@wwwarehouse.com'
    action = sys.argv[1]
    if action == '0':
        '''Jenkins每5分钟触发一次'''
        '''严重/致命bug，待修复，创建时间在5分钟内的，语音播报'''
        message_title = '以下致命或严重缺陷，已被创建'
        subject = '[Jenkins]致命或严重缺陷，已被创建'
        jiraSpeak(url_path, tl_path, int(action), message_title, subject, cc, loop_time=2, mail_func=False, speak_func=True)
    elif action == '1':
        '''Jenkins每30分钟触发一次'''
        '''严重/致命bug，待修复，创建时间>30分钟还未确认的，语音播报提醒'''
        message_title = '以下致命或严重缺陷，确认超时'
        subject = '[Jenkins]致命或严重缺陷，确认超时'
        jiraSpeak(url_path, tl_path, int(action), message_title, subject, cc, loop_time=2, mail_func=False, speak_func=True)
    elif action == '2':
        '''Jenkins每2小时触发一次'''
        '''严重/致命bug，已确认，缺陷确定时间>2小时还未修复'''
        message_title = '以下致命或严重缺陷，修复超时'
        subject = '[Jenkins]致命或严重缺陷，修复超时'
        jiraSpeak(url_path, tl_path, int(action), message_title, subject, cc, loop_time=2, mail_func=False, speak_func=True)
    elif action == '3':
        '''Jenkins每天早上10点钟出发一次'''
        '''所有bug，已确认/待修复bug，逾期（超过到期日）'''
        message_title = '以下缺陷，逾期修复'
        subject = '[Jenkins]所有逾期修复的缺陷'
        jiraSpeak(url_path, tl_path, int(action), message_title, subject, cc, loop_time=2, mail_func=False, speak_func=True)
    elif action == '4':
        '''Jenkins每天早上10点钟出发一次'''
        '''所有任务，逾期（超过计划完成时间）'''
        message_title = '以下任务，逾期完成'
        subject = '[Jenkins]所有逾期完成的任务'
        jiraSpeak(url_path, tl_path, int(action), message_title, subject, cc, loop_time=2, mail_func=False, speak_func=True)
    elif action == '6':
        '''中午播歌12:50触发'''
        music_path = 'z:\\'
        speak.playMusic(music_path, loop_time=1)
    else:
        speak.txetSpeak(action, loop_time=1)

