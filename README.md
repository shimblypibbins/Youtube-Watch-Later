# Daily Video SMS

A Python script that sends a daily SMS containing a random video link from a specified YouTube playlist at 8 pm using the YouTube Data API and Twilio SMS API.

## Prerequisites

- A YouTube Data API key
- A Twilio account with a verified phone number, account SID, and auth token

## Setup

1. Clone this repository to your local machine or Replit.
2. Replace the following placeholders in the script with your own API keys and credentials:
   - `API_KEY`: Your YouTube Data API key
   - `TWILIO_PHONE_NUMBER`: Your Twilio phone number
   - `TO_PHONE_NUMBER`: The recipient's phone number
   - `TWILIO_ACCOUNT_SID`: Your Twilio account SID
   - `TWILIO_AUTH_TOKEN`: Your Twilio auth token
3. Replace `PUBLIC_PLAYLIST_ID` with the ID of the YouTube playlist you want to fetch videos from.

## Usage

Run the script, and it will send an SMS with a random video link from the specified YouTube playlist daily at 8 pm.

## Notes

- This script uses the `schedule` library to schedule the SMS sending task. Make sure the script is running continuously for the scheduling to work.
- The phone numbers in the script should be in E.164 format (e.g., +1234567890).

## Acknowledgments

- [YouTube Data API](https://developers.google.com/youtube/v3)
- [Twilio SMS API](https://www.twilio.com/docs/quickstart/python/sms)
- [schedule](https://schedule.readthedocs.io/en/stable/)
