#!/usr/bin/env python3

# для vk в конслои набрать
# sudo apt-get install python3-pip
# pip3 install vk

import vk
import time

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



api = vk_login()


#s = api.users.get(user_ids=1)[0]
#print(s['first_name'])

#print(api.friends.get(user_ids = 'landspeeder'))
s = api.friends.get(fields = 'schools')

for i in s:
  print(i['first_name'], ' ', i['last_name'], end = '')
  if 'schools' in i:
    for j in i['schools']:
      print(' ', j['name'], end = '')
  print()
    
  

'''
mas = api.friends.get(user_ids = 'landspeeder')
for i in mas:
  print(api.users.get(user_ids=i))
  time.sleep(0.4)
  print(i)
  
'''
#print(api.users.get(user_ids=mas[1]))
