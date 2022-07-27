import slack
import os


def main():
    channel = "notify-me"
    message = "hello world"
    send_to_slack(channel, message)

def send_to_slack(channel, message):
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    client.chat_postMessage(channel=channel, text=message)

if __name__ == "__main__":
    main()