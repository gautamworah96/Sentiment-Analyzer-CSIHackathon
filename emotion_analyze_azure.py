import httplib, urllib, base64  
import requests
import json
# Image to analyse (body of the request)

body ='{\'URL\': \'https://images.pexels.com/photos/6413/people-eyes-playing-young.jpg?h=350&auto=compress\'}'

# API request for Emotion Detection
account_key='2xxx....xxxxx2'
headers = {
   'Content-type': 'application/json',
   'Ocp-Apim-Subscription-Key':account_key
}

params = urllib.urlencode({
   'subscription-key': '2xxxx.......xxxx2',  # Enter EMOTION API key
   #'faceRectangles': '',
})

try:
   conn = httplib.HTTPSConnection('api.projectoxford.ai')
   conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body , headers)
   response = conn.getresponse()
   data = response.read()
   print(data)
   '''print("Send request")
   print(type(response))
   
   
   
   
   string1=response.read().decode('utf-8')
   print(string1)
   
   json_obj=json.loads(string1)
   print('json object created')
   
   print(json_obj["scores"])
   #print(json_obj[{'scores':{'anger'}}])
   
   print('printing complete for json obj')
   data = response.read()
   print(data)'''
   conn.close()
except Exception as e:
   print('error occurred')