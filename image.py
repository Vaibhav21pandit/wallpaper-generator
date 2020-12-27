import requests
import os
import random
import json

def html_to_image(url,user_id,api_key,html_path,css_path):
  with open(html_path,'r') as f:
    html=f.read()
    f.close()

  with open('./default.css','r') as f:
    css=f.read()
    f.close()

  data = { 'html': html,
          'css': css,
          'google_fonts': "Roboto" }

  image = requests.post(url = HCTI_API_ENDPOINT, data = data, auth=(HCTI_API_USER_ID, HCTI_API_KEY))

  print("Your image URL is: %s"%image.json()['url'])

  choice=random.choice(range(0,300,1))

  os.system(f'wget -O ./wallpapers/{choice}.png {image.json()["url"]}')




if __name__=="__main__":
  with open("keys.json","r") as f:
    args=json.load(f)
    print(args["api-key"])
  HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
# Retrieve these from https://htmlcsstoimage.com/dashboard
  HCTI_API_USER_ID = args["user-id"]
  HCTI_API_KEY =args["api-key"]
  html_to_image(url=HCTI_API_ENDPOINT,user_id=HCTI_API_USER_ID,api_key=HCTI_API_KEY,html_path='./index.html',css_path='./default.css')

