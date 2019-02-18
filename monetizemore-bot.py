import os

import time
import re
from slackclient import SlackClient

# instantiate Slack client
# export SLACK_BOT_TOKEN='YOUR_SLACK_BOT_TOKEN'
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constans
RTM_READ_DELAY = 1 # 1 seconds delay between reading from RTM
help = 'help'
EXAMPLE_COMMAND = help
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

filename = '/home/eko/monetizemore/web_app/adscrape/apps/ans/fetchers/'

list_of_fetcher = []

def readFile(filename):
    with open(filename) as f:
        for line in f:
            for part in line.split():
                if "TITLE=" in part:
                    # print(part)
                    list_of_fetcher.append(part)
            # print(line)
            # break

for filename in os.listdir(os.getcwd()):
    readFile(filename)


def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Find a direct mention (a mention that is at the biginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the seconds group contains the reamaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)



def handle_command(command, channel):
   """
        Executes bot command if the command is known
   """
   # Default response command if the command is known
   default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

   # Find and executes the given command, filling in response
   response = None
   response2 = None


   # This is where you start to implement more commands!
   if command.startswith(EXAMPLE_COMMAND):
       # response = "Sure.. write some more code then I can do that!"
       response2 = 'available command: , ''1. I need more job , 2. ls fetcher , ' \
                   '3. EFS , ' \
                   '4. Kanban Board , ' \
                   '5. Assigned to Me '

   elif command.startswith('I need more job'):
       response2 = 'this feature still on development'
   elif command.startswith('ls fetcher'):
       response2 =  list_of_fetcher
   elif command.startswith('EFS'):
       response2 = 'Untuk sementara masih menggunakan url: https://monetizemore.atlassian.net/secure/RapidBoard.jspa?rapidView=6&projectKey=EFS&view=planning.nodetail'
   elif command.startswith('Kanban Board'):
       response2 = 'Untuk sementara masih menggunakan url: https://monetizemore.atlassian.net/secure/RapidBoard.jspa?rapidView=1&projectKey=ANS'
   elif command.startswith('Assigned to Me'):
       response2 = 'Untuk sementara masih menggunakan url: https://monetizemore.atlassian.net/issues/?jql=assignee%20%3D%20currentUser()%20AND%20resolution%20%3D%20unresolved%20ORDER%20BY%20priority%20DESC%2C%20created%20ASC'
       # I need more job
   # Sends the response back to the channel
   slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response2 or default_response
    )


if __name__  == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method 'auth_test'
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")