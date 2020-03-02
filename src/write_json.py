import json

def write_json(data, filename = 'results.json'):
	with open(filename, 'w') as file:
		json.dump(data, file, indent=4)