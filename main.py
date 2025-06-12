#!/usr/bin/env python3
import requests
import time
import datetime

def ping_backend():
   url = "https://calgentic.onrender.com/ping"
   
   try:
       print(f"{datetime.datetime.now()}: Pinging {url}")
       response = requests.get(url, timeout=30)  # 30 second timeout
       
       # What status code did we get?
       print(f"Response: {response.status_code}")
       
       if response.status_code == 200:
           print("✅ Backend is alive")
       else:
           print(f"⚠️ Unexpected status code: {response.status_code}")
           
   except requests.exceptions.Timeout:
       print("❌ Request timed out - backend might be spinning up")
   except requests.exceptions.ConnectionError:
       print("❌ Connection failed - backend might be down")
   except Exception as e:
       print(f"❌ Unexpected error: {e}")

def main():
   interval_minutes = 10
   interval_seconds = interval_minutes * 60
   
   print(f"Starting keep-alive script...")
   print(f"Will ping every {interval_minutes} minutes")
   print("Press Ctrl+C to stop")
   
   try:
       while True:
           ping_backend()
           print(f"Waiting {interval_minutes} minutes until next ping...\n")
           time.sleep(interval_seconds)
   except KeyboardInterrupt:
       print("\nStopping keep-alive script")

if __name__ == "__main__":
   main()