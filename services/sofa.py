import requests, time
from common import headers

BASE_URL = "https://api.sofascore.com/api/v1/"

def get_season_details(tournament_id, season_id):
    time.sleep(1.2)
    url = f"https://www.sofascore.com/u-tournament/{tournament_id}/season/{season_id}/json"
    r = requests.get(url, headers = headers)
    return r.json()

def get_current_round(tournament_id, season_id):
    time.sleep(1.2)
    url = f"{BASE_URL}unique-tournament/{tournament_id}/season/{season_id}/rounds"
    r = requests.get(url, headers = headers)
    print(r.content)
    return r.json().get("currentRound").get("round")

def get_round_events(tournament_id, season_id, round_id):
    time.sleep(1.2)
    url = f"{BASE_URL}unique-tournament/{tournament_id}/season/{season_id}/events/round/{round_id}"
    r = requests.get(url, headers = headers)
    print(r.content)
    return r.json().get("events")

if __name__ == "__main__":
    tournament_id = "238"
    season_id = "24150"
    round_id = get_current_round(tournament_id, season_id)
    print(round_id)
    events = get_round_events(tournament_id, season_id, round_id)
    print(events)