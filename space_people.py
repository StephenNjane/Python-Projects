import requests
# This script fetches the current number of people in space and their names
poeople = requests.get("http://api.open-notify.org/astros.json")
# Convert the response to JSON format
json = poeople.json()
# Print the JSON response
print(json)

#extracting the names of the people in space
print('The current people in space are:')
for person in json['people']:
    print(person['name'])
# Print the total number of people in space
print(f'The total number of people in space is {json["number"]}.')
   