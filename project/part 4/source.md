### **Этап 4. Отбор признаков и обучение новой версии модели**

На этом этапе вы будете использовать ранее обогащённые данные и примените методы отбора признаков, чтобы определить наиболее важные — так вы повысите производительность модели. Для этого: 

1. Используйте как минимум два метода отбора из библиотеки `mlxtend`, например `backward feature selection` и `forward feature selection`, чтобы определить наиболее значимые признаки для вашей модели.
2. Обучите новую версию модели на основе отобранных признаков, а затем оцените её метрики на тестовой выборке. 
3. Используйте MLflow Python API, чтобы залогировать процесс отбора признаков, окружение, обученную модель, её параметры, метрики качества и другие артефакты. Сюда также должны входить графики важности признаков и метрики модели после отбора признаков на тестовой выборке. 
4. Сохраните новую версию модели в MLflow Model Registry.

**Результаты этапа:**

1. Код для отбора признаков и обучения модели, оформленный и сохраненный на GitHub. Убедитесь, что код включает подробные комментарии к каждому шагу.
2. Залогированные артефакты в MLflow. 
3. Новая версия модели в MLflow Model Registry.