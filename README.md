
# SlackOps EC2 Bot

A Slack bot that interacts with AWS EC2 instances, checking their status through Slack commands. The bot uses the Slack API and AWS SDK (Boto3) to retrieve and send EC2 instance information.

## Prerequisites
- Python 3.8 or higher
- Slack Workspace and Bot
- AWS CLI configured with the correct permissions to access EC2
- Ngrok (or another tunneling tool) for local testing (if required)

## Setup

1. Clone the repository
   git clone https://github.com/<your-username>/SlackOps-EC2-Bot.git
   cd SlackOps-EC2-Bot
2. Set up a Python virtual environment
   python3 -m venv venv
source venv/bin/activate
3. Install the required dependencies
   pip install -r requirements.txt
4. Set up environment variables

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

