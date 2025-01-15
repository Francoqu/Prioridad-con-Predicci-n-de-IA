import matplotlib.pyplot as plt
import pandas as pd

# Cargar los resultados simulados
before_ia = pd.read_csv("results_before_ia.csv")
after_ia = pd.read_csv("results_after_ia.csv")

# Comparar tiempos de espera
plt.figure()
plt.plot(before_ia['task_id'], before_ia['wait_time'], label='Antes de IA')
plt.plot(after_ia['task_id'], after_ia['wait_time'], label='Después de IA')
plt.xlabel('ID de Tarea')
plt.ylabel('Tiempo de Espera')
plt.title('Comparación de Tiempos de Espera')
plt.legend()
plt.show()
