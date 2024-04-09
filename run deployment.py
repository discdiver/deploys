import httpx
from prefect import flow
from prefect.deployments import run_deployment


@flow(log_prints=True)
def hi1():
    print("hi1")

    run_deployment(
        name="hi flow/hi deploy",
    )


if __name__ == "__main__":
    hi1()
