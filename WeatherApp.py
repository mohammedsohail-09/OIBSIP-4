import requests

params = {
  'access_key': 'b138dfaed1edb38d4229ad1fa793de66',
  'query': ' '
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()
print(api_response)
print('*'*50)
print('name=',api_response['location']['name'])
print('region=',api_response['location']['region'])
print('country=',api_response['location']['country'])
print('lattitude=',api_response['location']['lat'])
print('longitude=',api_response['location']['lon'])
print('time zone=',api_response['location']['timezone_id'])
print('Time=',api_response['location']['localtime'])
print('Temperature=',api_response['current']['temperature'])
print('weather descriptions=',api_response['current']['weather_descriptions'])
print('wind speed=',api_response['current']['wind_speed'])
print('humidity=',api_response['current']['humidity'])
print('wind direction=',api_response['current']['wind_dir'])
print('pressure=',api_response['current']['pressure'])
print('feels like=',api_response['current']['feelslike'])
print('uv index=',api_response['current']['uv_index'])
print('Visibility=',api_response['current']['visibility'])
print('Is day=',api_response['current']['is_day'])
print('Cloud Cover=',api_response['current']['cloudcover'])
print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))
