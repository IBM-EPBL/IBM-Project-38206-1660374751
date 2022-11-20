

import wiotp.sdk.device 
import time



myConfig = {
    "identity" : {
        "orgId" : "k7hwfa",
        "typeId" : "NodeMcu",
        "deviceId" : "123456"
    },
    "auth" : {
        "token" : "12345678"
    }
}



def myCommandCallback(cmd):
    print("recieved cmd : ",cmd)


def logData2Cloud(location,temperature,visibility):
    client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
    client.connect()
    client.publishEvent(eventId="status",msgFormat="json",data={
        "temperature" : temperature,
        "visibility" : visibility,
        "location" : location
    },qos=0,onPublish=None)
    client.commandCallback = myCommandCallback
    client.disconnect()
    time.sleep(1)

