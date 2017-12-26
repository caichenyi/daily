# encoding: utf-8
# Author: Cai Chenyi

import json
users = [{'name': 'kk', 'age': '29'}]
s = json.dumps(users)
print(s)
print(json.loads(s))