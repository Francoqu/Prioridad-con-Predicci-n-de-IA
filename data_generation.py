import numpy as np
import pandas as pd

def generate_data(num_samples=1000):
    task_ids = np.arange(num_samples)
    complexities = np.random.randint(1, 10, size=num_samples)
    real_times = complexities * np.random.uniform(0.5, 1.5, size=num_samples)

    data = pd.DataFrame({
        'task_id': task_ids,
        'complexity': complexities,
        'real_time': real_times
    })
    return data

if __name__ == "__main__":
    data = generate_data()
    data.to_csv("training_data.csv", index=False)
