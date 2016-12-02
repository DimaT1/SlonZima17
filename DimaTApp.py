#!/usr/bin/env python3

# для vk в конслои набрать
# sudo apt-get install python3-pip
# pip3 install vk

import vk

def vk_login():
  s_id = '5749646'
  s_scope = 'friends'
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


def mykey(a):
  if 'schools' in a:
      if a['schools'] != []:
        return a['schools'][0]['name']
  return ''

api = vk_login()

s = api.friends.get(fields = 'schools')
s = sorted(s, key = mykey)

for i in s:
  print(i['first_name'], ' ', i['last_name'], end = '')
  if 'schools' in i:
    for j in i['schools']:
      print(' ', j['name'], end = '')
  print()
