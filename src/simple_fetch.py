import json
import urllib3

http = urllib3.PoolManager()
bootstrapStaticUrl = 'https://fantasy.premierleague.com/api/bootstrap-static/'
playerList = http.request('GET', 'http://httpbin.org/robots.txt')
playerList = urllib.request.urlopen(bootstrapStaticUrl)
playersDetailsData = json.loads(playerList.read().decode('utf-8'))
print(playersDetailsData)

events = playersDetailsData['events']
game_settings = playersDetailsData['game_settings']
phases = playersDetailsData['phases']
teams = playersDetailsData['teams']
elements = playersDetailsData['elements']
element_stats = playersDetailsData['element_stats']
element_types = playersDetailsData['element_types']

playersHistoryDetailsUrl = 'https://fantasy.premierleague.com/api/event/1/live/'
playersHistoryDetails = urllib.request.urlopen(playersHistoryDetailsUrl)
playersHistoryDetailsData = json.loads(playersHistoryDetails.read().decode('utf-8'))
playerHistoryStat = playersHistoryDetailsData['elements']

for player in elements:
    if player['element_type'] == 4 and player['now_cost'] == 90 and player['news'] == '':
        for history in playerHistoryStat:
            if player['id'] == history['id'] and history['stats']['minutes'] == 90:

                for team in teams:
                    if player['team_code'] == team['code']:
                        print(player['first_name'] + ' ' + player['second_name'], player['selected_by_percent'], player['now_cost'], team['name'], history['stats']['total_points'])
