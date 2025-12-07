from queue import Queue
import time
import random
import uuid

"""import Queue

Створити чергу заявок
queue = Queue()

Функція generate_request():
    Створити нову заявку
    Додати заявку до черги

Функція process_request():
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста

Головний цикл програми:
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
"""

queue = Queue()


def generate_request(request_data: str = "Sample Data"):
    request_id = str(uuid.uuid4())
    request = {"id": request_id, "data": request_data}
    queue.put(request)
    print(f"Generated request: {request_id}")


def process_request():
    if not queue.empty():
        time.sleep(random.uniform(0.1, 1.0))
        request = queue.get()
        print(f"Processing request: {request['id']} with data: {request['data']}")
    else:
        print("The request queue is empty.")


def main():
    print("Generating requests. Press Ctrl+C to stop.")

    try:
        while True:
            for i in random.sample(
                range(1, 6), k=random.randint(1, 3)
            ):  # Generate 1-3 requests at a time
                generate_request(f"Data {i+1}")

            for _ in range(
                random.randint(1, 5)
            ):  # Attempt to process one more than generated
                process_request()

    except KeyboardInterrupt:
        print(f"\nExiting program. The queue has {queue.qsize()} unprocessed requests.")


if __name__ == "__main__":
    main()
