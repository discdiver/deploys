import httpx
from prefect.deployments import run_deployment
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


# create deployment from code in GitHub repo
if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="fetch_data.py:fetch_temps",
    ).deploy(
        name="fetch-data",
        work_pool_name="managed1",
    )
