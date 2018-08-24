# -*- coding: utf-8 -*-
import requests
import json
import datetime

def apiCall(siteId):
    url = "https://api.sl.se/api2/realtimedeparturesV4.json"
    querystring = {"key":"05261ccaad7347a18a8960a4f57b4b91","timeWindow":60,"siteid":siteId,"bus":"false","metro":"false","tram":["false","false"]}
    
    headers = {
    'Cache-Control': "no-cache",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonresponse = json.loads(response.text)
    return jsonresponse

def clearJsonData(jsonObject):

    trainInfo = []

    for n in jsonObject["ResponseData"]["Trains"]:
        if n["LineNumber"] == "40": #and n["Destination"] == "Uppsala C":
            ExpectedDateTime = n["ExpectedDateTime"]
            TimeTabledDateTime = n["TimeTabledDateTime"]
            Destination = n["Destination"]
            StopAreaName = n["StopAreaName"]

            if ExpectedDateTime == TimeTabledDateTime:
                onTime = "Yes"
            else:
                onTime = "No"

            result = {'TrainOnTime': onTime,'TimeTabledDateTime': TimeTabledDateTime, 'ExpectedDepartureTime': ExpectedDateTime,'StopAreaName': StopAreaName, 'Destination': Destination}
            trainInfo.append(result.copy())
    return trainInfo