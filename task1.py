import requests
import string
import sys
import json
url="http://api.program-o.com/v2/chatbot/?bot_id=6&convo_id=armlabs&format=json&say="

user_input=""

print("Type 'bye' to end the chat")

while user_input!="bye":
	user_input=raw_input("Input: ")
	r=requests.get(url+user_input)
	print ("Output: "+r.json()["botsay"])

print("end of the bot")
