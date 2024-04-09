from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="flow-code/run deployment.py:hi",
    ).deploy(name="test deploy", work_pool_name="m1")
