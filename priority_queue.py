import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, priority, task_id, estimated_time):
        """Inserta una nueva tarea en la cola con prioridad."""
        heapq.heappush(self.heap, (priority, task_id, estimated_time))

    def pop(self):
        """Extrae la tarea con la mayor prioridad."""
        return heapq.heappop(self.heap)

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self.heap) == 0
