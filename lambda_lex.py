import json
from botocore.vendored import requests

def lambda_handler(event, context):
	location = event["currentIntent"]["slots"]["location"]
	response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params={"q": location, "appid":"3e97fa0dab8310f68949f9cdedaba777"})
	data = response.json()
	description = data["weather"][0]["description"]
	temperature = data["main"]["temp"]
	visibility = data["visibility"]
	humidity = data["main"]["humidity"]
	temp_celsius = int(temperature - 273.15)

	answer = 'The weather today in {location} is {description} with {visibility} meters of visibility and {temp_celsius} °C temperature and {humidity}% humidity in the air. '.format(location = location, description = description, visibility = visibility, temp_celsius=temp_celsius, humidity = humidity)
	
	return {
		"sessionAttributes": event["sessionAttributes"],
		"dialogAction": {
		"type": "Close",
		"fulfillmentState": "Fulfilled",
		"message": {
			"contentType": "PlainText",
			"content": answer
		}
	}
}







