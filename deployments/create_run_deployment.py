from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="flow_code/run deployment.py:fetch_temps",
    ).deploy()
