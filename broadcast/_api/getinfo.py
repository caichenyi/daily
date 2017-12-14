# encoding: utf-8
# Author: Cai Chenyi

import requests
import json
'''
url.txt文件存放list，以下为list[n]的含义
    0.致命/严重缺陷响应时效超过半小时的预警功能
    1.致命/严重缺陷处理时效超过2小时的预警功能
    2.常规缺陷未在到期日处理的预警功能；
        条件： 缺陷的严重等级为一般/建议，缺陷状态为待修复或已确认，且已到了到期日
'''
def getReceivers(tl_path, api_info, cc=''):
    receivers = []
    receivers.append(cc)

    with open(tl_path, 'rt', encoding='utf-8') as f:
        devtl_dict = eval(f.readline().strip())
        qatl_dict = eval(f.readline().strip())

    for i in api_info.values():
        receivers.append(i['reporter_email'])
        receivers.append(i['assignee_email'])
        if i['component'] in list(devtl_dict.keys()):
            receivers.append(devtl_dict[i['component']])
        if i['reporter'] in list(qatl_dict.keys()):
            receivers.append(qatl_dict[i['reporter']])
    return list(set(receivers))


def apiList(api_path):
    api_list = []
    with open(api_path, 'rt', encoding='utf-8') as f:
        for i in f:
            api_list.append(i)
    return api_list


def apiInfo(api_list, action):
    api_info = {}
    api = json.loads(requests.get(api_list[action], auth=('admin', 'admin@2016')).text)

    for i in api['issues']:
        key = i.get('key')
        summary = i.get('fields')['summary']
        if i.get('fields').get('assignee'):
            assignee = i.get('fields').get('assignee')['displayName']
            assignee_email = i.get('fields').get('assignee')['emailAddress']
        else:
            assignee, assignee_email = 'NULL', ''
        reporter = i.get('fields').get('reporter')['displayName']
        reporter_email = i.get('fields').get('reporter')['emailAddress']
        if i.get('fields').get('customfield_11300'):
            component = i.get('fields').get('customfield_11300')['value']
        else:
            component = 'NULL'

        api_info[key] = {
            'key': key,
            'summary': summary,
            'assignee': assignee,
            'assignee_email': assignee_email,
            'reporter': reporter,
            'reporter_email': reporter_email,
            'component': component
        }
    return api_info