import os
import boto3
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load from environment
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_app_token = os.environ["SLACK_APP_TOKEN"]

app = App(token=slack_bot_token)

@app.event("app_mention")
def handle_mention(event, say):
    text = event["text"]
    if "ec2 status" in text.lower():
        ec2 = boto3.client("ec2")
        response = ec2.describe_instances()
        instances = []
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                state = instance["State"]["Name"]
                inst_id = instance["InstanceId"]
                zone = instance["Placement"]["AvailabilityZone"]
                instances.append(f"{inst_id} is {state} in {zone}")

        result = "\n".join(instances)
        say(f"🖥️ EC2 Status:\n{result}")
    else:
        say("Hi there! You can say: `@bot check ec2 status`")

if __name__ == "__main__":
    handler = SocketModeHandler(app, slack_app_token)
    handler.start()
