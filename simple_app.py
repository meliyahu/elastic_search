import requests
import json


def print_plays(result):
    if len(result['hits']['hits']) > 0:
       print('')
       print(f'Found {result["hits"]["total"]["value"]} plays!')
       print('')
       for play in result['hits']['hits']:
          print(f'Play Name: {play["_source"].get("play_name", "No name")}'),
          print(f'Speech Number: {play["_source"].get("speech_number", "No number")}'),
          print(f'Line Number: {play["_source"].get("line_number", "No line Numb")}'),
          print(f'Speaker: {play["_source"].get("speaker", "No speaker")}'),
          print(f'Entry Text: {play["_source"].get("text_entry", "No entry text")}'),
          print('------------------')
          print('')
    else:
        print('No plays found')

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))


URL = 'http://localhost:9000/shakespeare/_search?q=*&size=20'
# URL = 'http://localhost:9000/shakespeare/_search?q=play_name:Mosheh'

result = requests.get(url=URL)

# extract data
data = result.json()
# pp_json(data['hits'])
print_plays(data)
