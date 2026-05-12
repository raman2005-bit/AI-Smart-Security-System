from twilio.rest import Client
import requests,base64,os

status_file = "status.txt"
account_sid = "YOUR TWILIO SID HERE"
auth_token = "YOUR TWILIO AUTH TOKEN HERE"
client = Client(account_sid, auth_token)

def check_if_open(status_file):
    if not os.path.exists(status_file):
        return True
    with open(status_file, "r") as f:
        return f.read().strip() == "open"
    
def set_system_status(status):
    with open(status_file, "w") as f:
        f.write(status)
                
    
def upload_image(image_path):
    api_key = "imgBB API KEY HERE"
    with open(image_path, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": api_key,
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        return res.json()['data']['url']
    
def call_sms(image_path):
    img_url = upload_image(image_path)
    try:
        msg = client.messages.create(body=f"ALERT: Boss koi persion dikha hai! photo check karo: {img_url}",media_url=[img_url], from_='+18508009110',to='+918252641527')
        call = client.calls.create(twiml='<Response><Say>Boss system Aleart, Someone has entered your room!</Say></Response>', from_='+18508009110',to='+918252641527')
        print("Alert Sent Successfully!")
    except Exception as e:
        print(f"error: {e}")


