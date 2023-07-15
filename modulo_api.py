import requests

def make_request():
    response = requests.get("https://blaze.com/api/roulette_games/recent")
    data = response.json()
    sorted_data = sorted(data, key=lambda x: x['created_at'], reverse=True)
    return sorted_data
