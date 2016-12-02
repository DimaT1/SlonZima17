#!/usr/bin/env python3

# для vk в конслои набрать
# sudo apt-get install python3-pip
# pip3 install vk

import vk
import time

def vk_login():
  s_id = '5749646'
  s_scope = 'groups'
  print('login: ', end = '')
  s_login = input()
  print('password: ', end = '')
  s_password = input()
  

  session = vk.AuthSession(app_id=s_id, user_login=s_login, user_password=s_password, scope=s_scope)

  del s_id
  del s_login
  del s_password
  del s_scope

  api = vk.API(session)
  
  print()
  return api


api = vk_login()

member_arr = api.groups.getMembers(group_id = 'slon_ipm')['users']
group_arr = {}

for i in member_arr:
  print(i)
  time.sleep(0.8)
  _user = api.users.get(user_id = i)[0]
  if not ('deactivated' in _user):
    names = api.groups.get(user_id = i, fields = 'name', extended=1)
    for j in range(1, len(names)):
      buf = names[j]['name']
        
      if buf in group_arr:
        group_arr[buf] += 1
      else:
        group_arr[buf] = 1

mas = sorted(group_arr.items(), key=lambda x: x[1], reverse=True) 
for i in range(10):
  print(mas[i][0])
