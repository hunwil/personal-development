# New Faker Script for Generating relevant demos

import keen
import random
import json
import requests
import os
import pprint
import math
import calendar

#this is a change in this version

#functions...
#cleans up json for viewing
def prettyjson(n):
    parsed = json.loads(n)
    print json.dumps(parsed, indent=4)


#makes sure to use two digits for dates(i.e. XXXX-XX-XX....)
def dblit(x):
    x = str(x)
    if len(x) < 2:
        x = "0"+x
    return x

#need to convert to env variables
keen.project_id = "58d95b0f3d5e15299e648f45"
keen.write_key = "DD2416C5B91D7E60579E32DBFBAC06038F2A08679EC8CA41BDE68EBABF109B3273557FD3D52930F6741B69AC938784CF0DF77A41C22F2C1DA8992CCCCBEE9289A7920663BEA06D491A787AE5AF995B391F2BA48F45EC7C179AC237EDF7EA83D5"
keen.read_key = "339866C7C930F25B140F7742658ADAA34CC939E38A1F711DE3FD477D8D80D7368715BEDA45A7FACD5C44A8104C0C1ABD0FED397FF470BC7054ED8B5C189CF241787B88E5919D73A792704DAEC0CEA89FCBEB542F52B507A43D3F19A7D16F0D67"
keen.master_key = "88AAF48ED82C433BB150A440153DAF5D1B8D7920504762F54CB5C02AECCA4800"

duration = 3 #months
events_per_month = 500 #events
growthrate = 1.1 #per month

#ask customer for 3 meaningful KPIs, determine  simple data model to support them

#interaction1 = []
#interaction2 = []
#interaction3 = []   #rename these logically

prop_names = ["SupportAgent1", "SupportAgent2", "SupportAgent2", "SupportAgent3", "SupportAgent1", "SupportAgent1", "SupportAgent4"]
prop_jobs = ["support", "support", "feedback", "spam", "support"]
prop_ages = list(range(30,99))

p1 = ["product", "pricing", "pricing", "pricing", "downtime"]
p2 = list(range(0,5))
p3 = ["medium", "twitter", "facebook", "twitter", "twitter", "medium"]
p4 = list(range(1000,1020))
p5 = ["American Airlines", "Delta Airlines", "Uber", "American Airlines", "T-Mobile", "T-Mobile", "T-Mobile", "T-Mobile", "T-Mobile", "T-Mobile"]
p6 = [150000, 400000, 90000, 1000000]
p7 = ["inbound", "outbound", "outbound"]

#url = 'https://api.keen.io/3.0/projects/58d95b0f3d5e15299e648f45/events/test_events_json'
#headers = {'content-type': 'application/json'}

events = []
ctr = 1
events_json = {}

yr = 2017
mo = 3

for i in range(1, duration):
    mxdays = calendar.monthrange(yr, mo)
    mxdays = mxdays[1]
    ctr = 0
    while (ctr < events_per_month):

        #Cycle through days and months
        d = random.randint(1,mxdays)
        d = dblit(d)
        m = mo
        m = dblit(m)
        h = random.randint(0,23)
        h = dblit(h)
        t = "2017-"+m+"-"+d+"T"+h+":09:10.141Z"

            #send the event to KeenIO
        keen.add_event("ticket_filed1", {
            "keen": {
                "timestamp": t
            },
            "ticket": {
                "type": random.choice(p7),
                "tags": random.choice(p1),
                "priority": random.choice(p2),
                "channel": random.choice(p3)
            },
            "agent_assigned": {
                "id": random.choice(p4),
                "name": random.choice(prop_names)
            },
            "account": {
                "name": random.choice(p5),
                "nps": random.choice(prop_ages),
                "spend_ytd": random.choice(p6)
            }

        })
        ctr = ctr + 1;
    events_per_month = events_per_month * growthrate
    mo = mo + 1
