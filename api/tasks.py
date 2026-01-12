import time

from celery import shared_task


@shared_task
def notify_item_added(item_id, item_name, item_description):
    timestamp = time.time()
    print(
        f"Item added at {timestamp} -> {{ Id: {item_id}, Name: {item_name}, Description: {item_description} }}"
    )
    time.sleep(15)
    return timestamp


@shared_task
def log():
    print("Logging task executed.")
    return "Logged"
