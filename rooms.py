import re

room_intents = {
    '1' : ['Pradeep', '(.*) Pradeep(.*)', '(.*) pradeep', '(.*) pradeep(.*)','(.*)Pradeep','pradeep'],
    '2' : ['Vignesh', '(.*) Vignesh(.*)', '(.*) vignesh', '(.*) vignesh (.*)','vignesh'],
    '3' : ['Lokesh', '(.*) Lokesh (.*)', '(.*) lokesh', '(.*) lokesh (.*)','(.*) lokesh',' lokesh (.*)','lokesh'],
    '4' : ['Nishant', '(.*)  Nishant(.*)', '(.*) nishant', '(.*)nishant(.*)', 'nishant',' (.*) nishant','nishant']
}

room_pattern = {}
for intent, values in room_intents.items():
    room_pattern[intent] = re.compile(r'|'.join(values))

