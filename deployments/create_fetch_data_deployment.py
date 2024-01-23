from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="flow-code/fetch_data.py:fetch_temps",
    ).deploy(
        name="fetch-data",
        work_pool_name="managed1",
    )
