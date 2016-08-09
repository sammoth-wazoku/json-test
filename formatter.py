import json

data = json.load(open('dashboard.json'))

idea_funnel = {'item': []}
user_funnel = {'item': []}
challenge_funnel = {'item': []}
idea_leaderboard = {'items': []}
user_leaderboard = {'items': []}
challenge_leaderboard = {'items': []}

data = sorted(data, key=lambda k: k['num_ideas'], reverse=True)
for company in data:
    idea_funnel['item'].append({'label': company['name'], 'value': company['num_ideas']})
    idea_leaderboard['items'].append({'label': company['name'], 'value': company['num_ideas']})

data = sorted(data, key=lambda k: k['num_users'], reverse=True)
for company in data:
    user_funnel['item'].append({'label': company['name'], 'value': company['num_users']})
    user_leaderboard['items'].append({'label': company['name'], 'value': company['num_users']})

data = sorted(data, key=lambda k: k['num_challenges'], reverse=True)
for company in data:
    challenge_funnel['item'].append({'label': company['name'], 'value': company['num_challenges']})
    challenge_leaderboard['items'].append({'label': company['name'], 'value': company['num_challenges']})

sorted(idea_leaderboard['items'])


json.dump(idea_funnel, open('idea_funnel.json', 'w+'))
json.dump(user_funnel, open('user_funnel.json', 'w+'))
json.dump(challenge_funnel, open('challenge_funnel.json', 'w+'))
json.dump(idea_leaderboard, open('idea_leaderboard.json', 'w+'))
json.dump(user_leaderboard, open('user_leaderboard.json', 'w+'))
json.dump(challenge_leaderboard, open('challenge_leaderboard.json', 'w+'))
