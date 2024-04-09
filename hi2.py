from prefect import flow


@flow(name="hi flow", log_prints=True)
def hi():
    print("hi there!")


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="hi2.py:hi flow",
    ).deploy(name="hi deploy", work_pool_name="m1")
