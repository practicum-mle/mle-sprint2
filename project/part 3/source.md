### **Этап 3. Генерация признаков и обучение модели**

На этом этапе вы будете улучшать вашу модель с помощью генерации новых признаков. Для этого: 

1. Займитесь предобработкой данных. Используйте подходящие методы из `sklearn.preprocessing` для нормализации, масштабирования или кодирования признаков в ваших данных.
2. Сгенерируйте признаки, ****используя ****`sklearn.preprocessing`**.** Примените как минимум два метода: `PolynomialFeatures` — для создания полиномиальных признаков, `KBinsDiscretizer` — для дискретизации числовых признаков. Соберите все преобразования в объект `ColumnTransformer`.
3. Создайте ****`sklearn`-пайплайн**.** Интегрируйте ваш `ColumnTransformer` в объект `Pipeline`, чтобы обеспечить последовательную предобработку данных.
4. Настройте автоматическую генерацию признаков с помощью библиотеки ****`autofeat`**.** 
5. Обучите новую версию модели на обогащённом наборе признаков. Затем оцените её качество и производительность (скорость обучения и предсказаний). Результаты залогируйте в MLflow.
6. Сохраните новую версию модели в MLflow Model Registry.

**Результаты этапа:**

1. Код для предобработки данных, генерации признаков и создания пайплайна, оформленный и сохраненный на GitHub. Убедитесь, что код включает подробные комментарии к каждому шагу.
2. Jupyter Notebook с примерами использования `autofeat` для автоматической генерации признаков.
3. Залогированные в MLflow: `Pipeline`, код для генерации признаков, окружение, сигнатура модели и сама обученная модель.
4. Новая версия модели в MLflow Model Registry.