# -*- coding: utf-8 -*-
import calendar
import json
import time
from idlelib.multicall import r

import requests
def callLegalApi(day):
    url = r'http://api.goseek.cn/Tools/holiday?date=20170528'
    requests.get(url,)
    time.sleep(1)
    r.encoding = 'utf-8'
    d = json.loads(r.text)
    answer = d['data']
    # ws.Range('B' + str(i)).Value = answer
    print('{}:{}'.format(answer))

callLegalApi(1)