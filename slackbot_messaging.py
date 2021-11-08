import slack
import os
from pathlib  import Path
from dotenv import load_dotenv
#create a bot,create a channel,add bot to channel
#connect with bot app
env_path=Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
client=slack.WebClient(token=os.environ['SLACK_TOKEN'])

#message to channel
client.chat_postMessage(channel='#test',text='Hey')

#message to specific user in channel
response = client.chat_postEphemeral(
  channel="#test",
  text="Hello silently from your app! :tada:",
  user="U02L4G1LEK0"
)
#Block message with image text and link as text
client.chat_postMessage(
  channel="test",
  blocks=[
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Block Message Test"
      }
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room " +
          "237 was far too rowdy, whole place felt stuck in the 1920s."
      },

      "accessory": {
        "type": "image",
        "image_url": "https://images.pexels.com/photos/750319/pexels-photo-750319.jpeg",
        "alt_text": "Haunted hotel image"
      }
    }
  ]
)

#Event handler--Turn on event handler in api.slack,Need to run on websever--run on ngrok
#post url is given to request url in enable event page

