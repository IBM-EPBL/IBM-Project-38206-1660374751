import brain

myLocation = "Madurai,IN"
APIKEY = "7a547a97f79ee73629edd98723ab36fe"

localityInfo = {
    "schools" : {
        "schoolZone" : True,
        "activeTime" : ["7:45","17:30"] # schools active from 7 AM till 5:30 PM
        },
    "hospitalsNearby" : False,
    "usualSpeedLimit" : 45 # in km/hr
}

print(brain.processConditions(myLocation,APIKEY,localityInfo))
