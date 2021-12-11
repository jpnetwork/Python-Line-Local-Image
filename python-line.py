#!/usr/local/bin/python
import requests

def linenotify(message):
  url = 'https://notify-api.line.me/api/notify'
  token = 'XXXXXXXXXXXXXXXXXXXX' # Line Notify Token
  img = {'imageFile': open('picture.jpg','rb')} #Local picture File
  data = {'message': message}
  headers = {'Authorization':'Bearer ' + token}
  session = requests.Session()
  session_post = session.post(url, headers=headers, files=img, data =data)
  print(session_post.text) 
  
message = 'Hello Python' #Set your message here!
linenotify(message)
