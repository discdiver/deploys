import httpx
from prefect.deployments import run_deployment
from prefect import flow


@flow(log_prints=True)
def fetch_temps(lat: float = 38.9, lon: float = -77.0):
    weather = httpx.get(
        "https://api.open-meteo.com/v1/forecast/",
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][:3])
    print(f"Most recent temp C: {most_recent_temp.sum()} degrees")
    return


if __name__ == "__main__":
    fetch_temps.from_source(source="", entrypoint="run_deploys.py:fetch_temps").deploy(
        name="fetch-data",
        work_pool_name="managed1",
    )
