from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/discdiver/deploys.git",
        entrypoint="flow-code/train_model.py:train_model",
    ).deploy(
        name="train_model",
        work_pool_name="managed2",
    )
