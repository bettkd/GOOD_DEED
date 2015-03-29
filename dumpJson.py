import json

data1 = {"User_Name":"Dominic Bett", "Current_Location":"Orangeburg,SC","Recent_Charities":{"Charity_Name":"NewLife Charity", "Location":"Anaheim,CA", "Phone":"(843) 422-1331"}}
with open('userProfile.json', 'w') as outfile:
	json.dump(data1, outfile, indent=4)