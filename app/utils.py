# utils.py
import requests
from config import API_BASE_URL, API_KEY

def fetch_trail_data(start_index=1, end_index=10):
    url = f"{API_BASE_URL}/{API_KEY}/json/viewGil/{start_index}/{end_index}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API 호출 실패: {response.status_code}")

def process_trail_data(raw_data):
    trails = []
    for row in raw_data["viewGil"]["row"]:
        trails.append({
            "name": row["GIL_NM"],
            "length": row["GIL_LEN"],
            "difficulty": row["LV_CD"],
            "description": row["GIL_EXPLN"],
            "start": row["STRT_PSTN"],
            "end": row["END_PSTN"],
            "map_url": row["SEOUL_MAP_URL"]
        })
    return trails
