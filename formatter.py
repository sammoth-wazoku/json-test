import json
import random

data = json.load(open('dashboard.json'))

## Totals

total_ideas = 0
total_challenges = 0
total_users = 0

for company in data:
    total_ideas += int(company['num_ideas'])
    total_challenges += int(company['num_challenges'])
    total_users += int(company['num_users'])

json.dump(
    {
        'item': total_ideas,
        'min': {'value': 0},
        'max': {'value': (total_ideas * random.uniform(1, 3))},
    },
    open('idea_gekometer.json', 'w+')
)

json.dump(
    {
        'item': total_challenges,
        'min': {'value': 0},
        'max': {'value': (total_challenges * random.uniform(1, 3))}
    },
    open('challenge_gekometer.json', 'w+')
)

json.dump(
    {
        'item': total_users,
        'min': {'value': 0},
        'max': {'value': (total_users * random.uniform(1, 3))}
    },
    open('user_gekometer.json', 'w+')
)


## Ideas

data = sorted(data, key=lambda k: k['num_ideas'], reverse=True)
idea_funnel = {'item': []}
idea_leaderboard = {'items': []}
for company in data:
    idea_funnel['item'].append({'label': company['name'], 'value': company['num_ideas']})
    idea_leaderboard['items'].append({'label': company['name'], 'value': company['num_ideas']})
json.dump(idea_funnel, open('idea_funnel.json', 'w+'))
json.dump(idea_leaderboard, open('idea_leaderboard.json', 'w+'))

## Users

data = sorted(data, key=lambda k: k['num_users'], reverse=True)
user_funnel = {'item': []}
user_leaderboard = {'items': []}
for company in data:
    user_funnel['item'].append({'label': company['name'], 'value': company['num_users']})
    user_leaderboard['items'].append({'label': company['name'], 'value': company['num_users']})
json.dump(user_funnel, open('user_funnel.json', 'w+'))
json.dump(user_leaderboard, open('user_leaderboard.json', 'w+'))

## Challenge

data = sorted(data, key=lambda k: k['num_challenges'], reverse=True)
challenge_funnel = {'item': []}
challenge_leaderboard = {'items': []}
for company in data:
    challenge_funnel['item'].append({'label': company['name'], 'value': company['num_challenges']})
    challenge_leaderboard['items'].append({'label': company['name'], 'value': company['num_challenges']})
json.dump(challenge_funnel, open('challenge_funnel.json', 'w+'))
json.dump(challenge_leaderboard, open('challenge_leaderboard.json', 'w+'))
