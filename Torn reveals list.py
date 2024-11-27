import requests
import json

apikey = input("Enter your api key of at least limited access")
spiesurl="https://api.torn.com/user/?selections=reports&key="
userprofileurl1="https://api.torn.com/user/"
userprofileurl2="?selections=profile&key="

response_spies=requests.get(spiesurl+apikey)

if response_spies.status_code == 200:
    spies_data = response_spies.json()
else:
    print(f"Request failed with status code {response_spies.status_code}")

for report in spies_data['reports']:
    response_profile=requests.get(userprofileurl1+str(report['target'])+userprofileurl2+apikey)
    if response_profile.status_code == 200:
        profile_data = response_profile.json()
    else:
        print(f"Request failed with status code {response_spies.status_code}")
    print(profile_data['name']+'['+str(report['target'])+']')
    if 'strength' in report['report']:
        print('  Strength: '+ str(report['report']['strength']))
    if 'speed' in report['report']:
        print('  Speed: '+ str(report['report']['speed']))
    if 'dexterity' in report['report']:
        print('  Dexterity: '+ str(report['report']['dexterity']))
    if 'defense' in report['report']:
        print('  Defense: '+ str(report['report']['defense']))
    if 'total_battlestats' in report['report']:
        print('  Total: '+ str(report['report']['total_battlestats']))
    print()