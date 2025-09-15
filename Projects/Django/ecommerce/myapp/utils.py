from django.shortcuts import render, redirect
from django.conf import settings
import requests
'''def send_otp_via_fast2sms(mobile, otp):
    # Use the same endpoint/format you used in forgot_password
    # Put your API key in settings.py as FAST2SMS_API_KEY (recommended)
    api_key = getattr(settings, 'FAST2SMS_API_KEY', None)
    if not api_key:
        # fallback: you may have hardcoded key in other places; but better to add to settings
        return False

    url = "https://www.fast2sms.com/dev/voice"   # matches your existing code
    querystring = {
        "authorization": api_key,
        "variables_values": str(otp),
        "route": "otp",
        "numbers": str(mobile)
    }
    headers = {'cache-control': "no-cache"}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        # You can check response.status_code or response.text for errors
        return True
    except Exception as e:
        print("Fast2SMS send error:", e)
        return False

'''
# accounts/utils.py
import requests

def send_otp_via_fast2sms(mobile, otp):
    url = "https://www.fast2sms.com/dev/bulkV2"
    headers = {
        "authorization": "YOUR_API_KEY_HERE",  # Replace with your actual Fast2SMS API key
        "Content-Type": "application/json"
    }
    payload = {
        "sender_id": "FSTSMS",
        "message": f"Your OTP is {otp}",
        "language": "english",
        "route": "v3",
        "numbers": mobile
    }
    response = requests.post(url, json=payload, headers=headers)
    
    # Optional: print response for debugging
    print(response.status_code, response.text)
    
    return response.status_code == 200
