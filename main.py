import os
import random
import requests
import time
import schedule
from twilio.rest import Client

# Replace with your API key
API_KEY = os.environ['YOUTUBE_API_KEY']

# Replace with your Twilio information
TWILIO_PHONE_NUMBER = '***REMOVED***'
TO_PHONE_NUMBER = '***REMOVED***'
TWILIO_ACCOUNT_SID = '***REMOVED***'
TWILIO_AUTH_TOKEN = '***REMOVED***'

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Replace with your public playlist ID
PUBLIC_PLAYLIST_ID = 'PLkfVDaIADDXlJVxbBEP8pajyngsTO55O0'

# Get a random video from the public playlist
def get_random_video(playlist_id):
  url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&key={API_KEY}"
  response = requests.get(url).json()
  if 'items' in response and len(response['items']) > 0:
    random_video = random.choice(response['items'])
    return random_video['snippet']['title'], random_video['snippet']['resourceId']['videoId']
  else:
    return None, None

# Send SMS with video link
def send_sms(video_title, video_id):
  message = twilio_client.messages.create(
    body=f"Today's video from your public playlist is:\n\n{video_title}\nhttps://www.youtube.com/watch?v={video_id}",
    from_=TWILIO_PHONE_NUMBER,
    to=TO_PHONE_NUMBER)

def job():
  video_title, video_id = get_random_video(PUBLIC_PLAYLIST_ID)

  if video_title and video_id:
    send_sms(video_title, video_id)
    print(f"SMS sent with video: {video_title}")
  else:
    print("No videos found in the public playlist.")

if __name__ == '__main__':
  # Schedule the job to run every day at 8 pm
  schedule.every().day.at("20:00").do(job)

  # Keep the script running and check for scheduled tasks
  while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 60 seconds before checking again
