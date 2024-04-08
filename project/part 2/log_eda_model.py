import os

import mlflow
from catboost import CatBoostClassifier


TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000
EXPERIMENT_NAME = "churn_nikolaistepanov"
RUN_NAME = "model_eda"
MODEL_PATH = "model_eda.cb"
REGISTRY_MODEL_NAME = "student_model_name"


os.environ["MLFLOW_S3_ENDPOINT_URL"] = "..." # endpoint бакета от YandexCloud
os.environ["AWS_ACCESS_KEY_ID"] = "..." # внесите id ключа бакета, к которому подключен MLFlow
os.environ["AWS_SECRET_ACCESS_KEY"] = "..."  # внесите ключ бакета, к которому подключен MLFlow

mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}")
mlflow.set_registry_uri(f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}")


# model = ... # Тут у каждого студента своя модель, он должен ее сохранить в эту переменную
# В моем примере это модель из catbosot - CatBoostClassifier
model = CatBoostClassifier()
model.load_model(MODEL_PATH)

# тут студент либо считает метрики, либо просто может вбить их
# если он их будет считать, то тогда у него обязательно наличие загрузки данных,
# разбитие их на обучение и/или валидацию и тест
metrics = {"roc_auc": 0.82}

# файл с окружение обязательно, чтобы можно было при необходимости воспроизвести
pip_requirements="../../requirements.txt"

# опционально
# signature = mlflow.models.infer_signature(X_test, prediction)
# input_example = X_test[:10]
# metadata = {"model_type": "monthly"}


experiment_id = mlflow.get_experiment_by_name(EXPERIMENT_NAME).experiment_id


with mlflow.start_run(run_name=RUN_NAME, experiment_id=experiment_id) as run:
    run_id = run.info.run_id
    
    mlflow.log_metrics(metrics)
    model_info = mlflow.catboost.log_model(
        cb_model=model,
        artifact_path="models",
        registered_model_name=REGISTRY_MODEL_NAME,
        await_registration_for=60, # опционально
        pip_requirements=pip_requirements,
        # signature=signature,
        # input_example=input_example,
        # metadata=metadata,
    )