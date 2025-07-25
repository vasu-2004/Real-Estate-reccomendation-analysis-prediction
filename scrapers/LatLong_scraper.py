import requests
import pandas as pd
import time

def get_coordinates_osm(sector):
    search_term = f"Sector {sector}, Gurgaon, India"
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": search_term,
        "format": "json"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return f"{data[0]['lat']}, {data[0]['lon']}"
    return None

data = []
for sector in range(1, 116):
    coordinates = get_coordinates_osm(sector)
    print(f"Fetched Sector {sector}: {coordinates}")
    data.append({"Sector": f"Sector {sector}", "Coordinates": coordinates})
    time.sleep(1)  # Sleep to avoid rate-limiting

df = pd.DataFrame(data)
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)
print("Coordinates saved to gurgaon_sectors_coordinates.csv")
