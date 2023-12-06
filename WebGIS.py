import requests
import json

# Replace with the actual latitude, longitude, and radius values
latitude = 57.2037  # London Heathrow Airport latitude
longitude = 2.2002  # London Heathrow Airport longitude
radius = 200  # 200-mile radius

# Replace with the actual API endpoint you want to use
api_url = f'http://api.airplanes.live/v2/point/{latitude}/{longitude}/{radius}'

# Make the GET request
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    aircraft_data = response.json()
    print(aircraft_data)

    # Create a GeoJSON FeatureCollection
    features = []
    for aircraft in aircraft_data['ac']:
        # Check if the key is present in the aircraft data
        altitude = aircraft.get('alt_baro', None)

        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [aircraft['lon'], aircraft['lat']]
            },
            "properties": {
                "hex": aircraft['hex'],
                "flight": aircraft['flight'],
                "ownOp": aircraft.get('ownOp', None),
                "desc": aircraft.get('desc', None),
                "altitude": altitude
            }
        }
        features.append(feature)

    feature_collection = {
        "type": "FeatureCollection",
        "features": features
    }

    # Convert to GeoJSON string
    geojson_string = json.dumps(feature_collection, indent=2)

    # Specify the file path
    file_path = r'C:\Users\DELL\OneDrive\Desktop\WEBGIS2\aircraft_data1.geojson'

    # Save the GeoJSON string to a file
    with open(file_path, 'w') as file:
        file.write(geojson_string)

    print(f"GeoJSON data saved to: {file_path}")

else:
    print(f"Error: {response.status_code}")
    print(response.text)
