import json

data = json.load(open('dashboard.json'))

idea_funnel = {'item': []}
user_funnel = {'item': []}
challenge_funnel = {'item': []}

for company in data:
    idea_funnel['item'].append({'label': company['name'], 'value': company['num_ideas']})
    user_funnel['item'].append({'label': company['name'], 'value': company['num_users']})
    challenge_funnel['item'].append({'label': company['name'], 'value': company['num_challenges']})

json.dump(idea_funnel, open('idea_funnel.json', 'w+'))
json.dump(user_funnel, open('user_funnel.json', 'w+'))
json.dump(challenge_funnel, open('challenge_funnel.json', 'w+'))
