import tensorflow as tf
from priority_queue import PriorityQueue
import numpy as np

# Cargar el modelo entrenado
model = tf.keras.models.load_model("priority_model.h5")

# Crear una cola de prioridad
queue = PriorityQueue()

def add_task(queue, task_id, complexity):
    """Predice el tiempo estimado y agrega la tarea a la cola con prioridad dinámica."""
    estimated_time = model.predict(np.array([[task_id, complexity]]))[0][0]
    priority = calculate_priority(estimated_time, complexity)
    queue.insert(priority, task_id, estimated_time)

def calculate_priority(estimated_time, complexity):
    """Calcula la prioridad en función del tiempo estimado y la complejidad."""
    return complexity / (estimated_time + 1)

# Simular la inserción de tareas
tasks = [(1, 5), (2, 8), (3, 3)]
for task_id, complexity in tasks:
    add_task(queue, task_id, complexity)

# Extraer y atender las tareas en orden de prioridad
while not queue.is_empty():
    print("Atendiendo tarea:", queue.pop())
