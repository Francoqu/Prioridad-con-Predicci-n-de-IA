import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

# Cargar los datos
data = pd.read_csv("training_data.csv")
X = data[['task_id', 'complexity']].values
y = data['real_time'].values

# Dividir los datos en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el modelo
model = Sequential([
    Dense(16, activation='relu', input_shape=(2,)),
    Dense(8, activation='relu'),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, validation_data=(X_val, y_val))

# Guardar el modelo entrenado
model.save("priority_model.h5")
