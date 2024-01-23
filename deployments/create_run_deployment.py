from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="flow-code/run_deployment.py:fetch_temps",
    ).deploy(
        name="run-deploy-example",
        work_pool_name="managed1",
    )
