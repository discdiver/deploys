import httpx
from prefect import flow


@flow(log_prints=True)
def fetch_temps(lat: float = 38.9, lon: float = -77.0):
    weather = httpx.get(
        "https://api.open-meteo.com/v1/forecast/",
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    forecasted_temps = weather.json()["hourly"]["temperature_2m"][:12]
    print(f"Max expected value in the next 12 hours: {max(forecasted_temps)} degrees C")
    return