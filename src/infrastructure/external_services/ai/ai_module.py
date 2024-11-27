import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('Agg')

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Загрузите датасет и обучите модель один раз
avocado_data = pd.read_csv('infrastructure/external_services/ai/avocado.csv')
avocado_data['Date'] = pd.to_datetime(avocado_data['Date'])
avocado_data['month'] = avocado_data['Date'].dt.month
avocado_data_cleaned = avocado_data.drop(columns=['Unnamed: 0', 'Date'])

# Подготовьте признаки и целевую переменную
X = pd.get_dummies(avocado_data_cleaned.drop(columns=['AveragePrice']), drop_first=True)
y = avocado_data_cleaned['AveragePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучите модель и сохраните ее
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
joblib.dump(rf_model, 'rf_model.pkl')

# Функция для загрузки модели и предсказания
def predict_price(new_data):
    print(3333333)
    print(new_data)
    if not isinstance(new_data, dict):
        raise ValueError("new_data must be a dictionary with valid feature keys and values.")

    # Загрузка модели
    rf_model = joblib.load('rf_model.pkl')

    # Обработка новых данных
    new_df = pd.DataFrame([new_data])
    new_df_encoded = pd.get_dummies(new_df, columns=['category'], drop_first=True)
    for col in X.columns:
        if col not in new_df_encoded.columns:
            new_df_encoded[col] = 0
    new_df_encoded = new_df_encoded[X.columns]

    # Предсказание
    predicted_price = rf_model.predict(new_df_encoded)[0]
    adjusted_predicted_price = predicted_price * 97  # Умножаем на 97
    print(f'Predicted price: {adjusted_predicted_price}')

    # Предсказание цен на следующий месяц
    future_months = pd.DataFrame({
        'month': [new_data['month'] + i for i in range(1, 4)],  # Предсказание на следующие 3 месяца
        'category': [new_data['category']] * 3,
        'competition': [new_data['competition']] * 3,
        'new_product': [new_data['new_product']] * 3,
        'popularity': [new_data['popularity']] * 3
    })

    # Кодирование категориальных переменных
    future_df_encoded = pd.get_dummies(future_months, columns=['category'], drop_first=True)
    for col in X.columns:
        if col not in future_df_encoded.columns:
            future_df_encoded[col] = 0
    future_df_encoded = future_df_encoded[X.columns]

    # Получаем предсказания
    predicted_future_prices = rf_model.predict(future_df_encoded) * 97  # Умножаем на 97

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(future_months['month'], predicted_future_prices, marker='o', label='Predicted Price')
    plt.xlabel('Month')
    plt.ylabel('Predicted Price')
    plt.title('Predicted Price for the Next Months (x97)')
    plt.xticks(future_months['month'])  # Убедитесь, что на графике отображаются правильные метки месяцев
    plt.legend()
    plt.show()

    return round(adjusted_predicted_price, 2)

# Пример использования
new_data_example = {
    'month': 6,
    'category': 'Avocado',
    'competition': 0.2,
    'new_product': 0,
    'popularity': 0.8
}

predict_price(new_data_example)
