from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')