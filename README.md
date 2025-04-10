
# SlackOps EC2 Bot

A Slack bot that interacts with AWS EC2 instances, checking their status through Slack commands. The bot uses the Slack API and AWS SDK (Boto3) to retrieve and send EC2 instance information.

## Prerequisites
- Python 3.8 or higher
- Slack Workspace and Bot
- AWS CLI configured with the correct permissions to access EC2
- Ngrok (or another tunneling tool) for local testing (if required)

## Setup

1. Clone the repository
   git clone https://github.com/AnimelaD/SlackOps-EC2-Bot
and change directory to 
   cd SlackOps-EC2-Bot
3. Set up a Python virtual environment
   python3 -m venv venv
source venv/bin/activate
4. Install the required dependencies
   pip install -r requirements.txt
5. Set up environment variables

Create a .env file in the root directory and add the following

SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_APP_TOKEN=xapp-your-app-token
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_DEFAULT_REGION=ap-southeast-1

5.** Run the Bot **
python app.py

**How to use and Run the Bot**
In your Slack channel, mention the bot to check EC2 status:
@AIOps check ec2 status
================================================
**** Setting Up the Slack API App****
Follow these steps to set up a Slack API app for your SlackOps EC2 Bot.

**Step 1: Create a New Slack App**
Go to the Slack API Website:

Visit Slack API.
https://api.slack.com/
Create a New App:
Click on Create New App.
Choose From Scratch.
App Name: SlackOps EC2 Bot (or any name you prefer).
Development Slack Workspace: Select your Slack workspace (e.g., SlackOps AI BOT).
Click Create App.

**Step 2: Add Bot Token Scopes**
Go to OAuth & Permissions:

In your app's settings page, click OAuth & Permissions in the left sidebar.

Add Required Scopes:

Scroll down to the Bot Token Scopes section.

Add the following required scopes for your bot:

app_mentions:read – allows the bot to receive messages where it is mentioned (e.g., @AIOps).

chat:write – allows the bot to send messages to Slack channels.

(Optional) channels:read – allows the bot to read the list of channels.

Save Scopes:

Click Save Changes.

**Step 3: Enable Events & Socket Mode**
Enable Socket Mode:

In the Settings section on the left sidebar, click Socket Mode.

Toggle Enable Socket Mode to ON.

Create an App Token: Click Create App Token and save it for later (you will use this token in your Python code). The token will be something like xapp-....

Subscribe to Events:

Go to Event Subscriptions in the sidebar.

Toggle Enable Events to ON.

Under Subscribe to Bot Events, add the following event:

app_mention – allows the bot to respond when it's mentioned in a Slack channel.

Save Changes:

Save the changes.

**Step 4: Install the App to Your Slack Workspace**
1. Install the App:

Go to the Install App section.

Click Install to Workspace.

You will be redirected to Slack to authorize the app.

Once authorized, you will see a Bot User OAuth Token (e.g., xoxb-...). Copy this token for later use in your code.

2. Creating a Slack Channel
Now that your app is ready, you'll need a Slack channel where the bot can receive commands.

Step 1: Create a Slack Channel
Open Slack and go to the Slack workspace where you created the bot (e.g., SlackOps AI BOT).

On the left sidebar, click the "+" button next to Channels to create a new channel.

Channel Name: Choose a name (e.g., #ec2-status or any name you prefer).

Choose whether the channel is private or public.

Click Create.

Step 2: Add the Bot to the Channel
In the Slack channel, click on the channel name at the top to open the channel settings.

Select Add apps.

Search for your SlackOps EC2 Bot and add it to the channel.

Now, the bot will be able to listen to messages and respond in that channel.

3. How to Check EC2 Status Using SlackOps EC2 Bot
Now that your bot is set up and added to the Slack channel, you can use it to check the EC2 status.

Step 1: Mention the Bot in the Channel
Go to the Slack channel where the bot is added (e.g., #ec2-status).

Type the following command to check the EC2 status:

Command: @AIOps check ec2 status

This is the trigger command for your bot. The bot will recognize it and respond with the EC2 status based on the instances available in your AWS account.

Example input:

@AIOps check ec2 status
What Happens Next?
The bot will connect to the AWS EC2 service using the AWS SDK (Boto3).

It will call the describe_instances API to retrieve details about your EC2 instances.

The bot will format and return the instance ID, state (running/stopped), and availability zone of each EC2 instance.

Example bot response:

🖥️ EC2 Status:
i-0123456789abcdef0 is running in ap-southeast-1a
i-0abcdef1234567890 is stopped in ap-southeast-1b

<img width="782" alt="BOT-Success" src="https://github.com/user-attachments/assets/5054d755-e65a-4b08-878f-131f5453e362" />


** Troubleshooting**'

If the bot doesn't respond, check the following:

Check Logs:

If you're running the bot locally, ensure the Python process is running without errors.

Look at the terminal logs for any issues, such as invalid tokens, connection issues with AWS, or Slack API errors.

<img width="509" alt="image" src="https://github.com/user-attachments/assets/9bbbaffa-19e7-49c0-a706-9c1ff4f50c5a" />

Permissions:

Ensure that your Slack bot token has the correct permissions (app_mentions:read, chat:write).

Make sure the bot is added to the Slack channel and that you are mentioning it correctly (@AIOps).

AWS Credentials:

Make sure your AWS credentials (AWS Access Key, Secret Key) are set up properly in the .env file and have the required permissions to describe EC2 instances.

