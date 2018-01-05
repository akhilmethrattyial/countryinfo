import sys
import requests

arguments  = sys.argv


if len(arguments) > 1:
  for ip in arguments[1:]:
	  response = requests.get('https://freegeoip.net/json/{}'.format(ip))
		if response:
			print('{}:{}'.format(ip,response.json()['country_code']))
else:
	print('Usage: getccinfo.py  IpAddress')
