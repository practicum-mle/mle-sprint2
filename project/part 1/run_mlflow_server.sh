export MLFLOW_S3_ENDPOINT_URL=https://storage.yandexcloud.net
export AWS_ACCESS_KEY_ID= # здесь должен быть ваш AWS_ACCESS_KEY_ID
export AWS_SECRET_ACCESS_KEY= # здесь должен быть ваш AWS_SECRET_ACCESS_KEY

mlflow server \
    --backend-store-uri postgresql: # здесь должен быть написа connection для подключение к базе данных Postgres \
	--registry-store-uri postgresql: # аналогично строчке выше \
	--default-artifact-root s3:// # здесь должен быть написано название бакета в Object Sotrage \
	--no-serve-artifacts # флаг для доступа к артефактам без proxy Из документации - In some cases, you may want to directly access remote storage without proxying through the tracking server. In this case, you can start the server with --no-serve-artifacts flag, and setting --default-artifact-root to the remote storage URI you want to redirect the request to.)