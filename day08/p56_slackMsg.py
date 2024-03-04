# file: p56_slackMsg.py
# desc: 슬랙으로 스마트폰 메세지 보내기
'''
1. https://api.slack.com/ >> Your apps >> Create your first app
2. From Scratch 클릭 > 앱 이름은 영어로
3. 워크스페이스 선택
4. Incomming Webhooks > On > Add New Webhook to Workspace 클릭 > 채널선택 > 허용    
'''

# https://hooks.slack.com/services/T*****/B****/********

import requests 
import json

slack_url = 'https://hooks.slack.com/services/T*****/B****/********' 

headers = {'Content-type':'application/json'}
data = { 'text': 'Python에서 보내는 메세지'}

res = requests.post(slack_url, headers=headers, data=json.dumps(data))
if res.status_code == 200:
    print('메세지 전송성공')
else:
    print('실패')