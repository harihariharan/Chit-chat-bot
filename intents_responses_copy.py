import re

def match_intent(msg, patterns):
    msg = msg.lower()
    matched_intent = None
    for intent, pattern in patterns.items():
        if re.search(pattern, msg):
            matched_intent = intent

    return matched_intent

intents = {
    'greet': ['hi','hello','hey','bot','hai', 'hay'],
    'fine': ['how are you (.*)','how do you do (.*)','how are you','how do you do'],
    'stop': ['quit', 'exit', ' stop', 'close', 'thank you (.*)', 'thank', 'bye', 'goodbye'],
    'news': ['news', 'headline', 'tell (.*) news', 'tell (.*) headline', '(.*) news', '(.*) headline'],
    'read': ['read mail', 'read message', 'read mail (.*)', 'read message (.*)',' (.*) read inbox (.*)'
            '(.*) read mail', 'read (.*) mail (.*)', '(.*) read message',
            'read (.*) mail', 'read (.*) message', '(.*) read (.*) mail', '(.*) read (.*) message'],
    'send': ['send mail', 'send message', 'send mail (.*)', 'send message (.*)',
            '(.*) send mail', 'send (.*) mail (.*)', '(.*) send message',
            'send (.*) mail', 'send (.*) message', '(.*) send (.*) mail', '(.*) send (.*) message'],
    'emergency': ['emergency', '(.*) emergency', 'emergency (.*)', '(.*) emergency (.*)'],
    'intro':['intro'],
    'self_intro':['(.*) about you','who are you?','what can you do','what can you do (.*)'],
    'stress_test':['(.*) stress test','stress test','stress test (.*)'],
    'room_number':['rooom number','(.*)room number'],
    'time': ['time'],
    'date': ['date'],
    'remainder' : ['reminder'],
    'mail' : ['mail']

}


responses = {
    'default': ['Sorry, it is beyond my ability.'],
    'greet': ['Hi! ,what can I do for you?', 'Good to see you, how can I help you?'],
    'fine': ['I am fine. Thank you so much for asking!'],
    'stop': ['Bye. Take care. Get well soon.'],
    'read': ['Reading in progress. Please wait...'],
    'send': ['Sending in progress. Please wait...'],
    'news': ["Todays news"],
    'time': ['The time is'],
    'date': ['The date is'],
    'emergency': ['Emergency.'],
    'self_intro':['Self introduction.'],
    'stress_test':['stress test'],
    'room_number':['your room number is:'],
    'remainder': ['reminder'],
    'mail': ['mail'],
    'intro':['intro']
}


patterns = {}
for intent, values in intents.items():
    patterns[intent] = re.compile(r'|'.join(values))
# while True:
#     msg=input()
#     print(match_intent(msg, patterns))