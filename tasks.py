import time

from celery import Celery


app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.task_routes = {
    'tasks.make_meal': {'queue': 'chef'},
    'tasks.deliver_meal': {'queue': 'delivery'}
}

@app.task
def deliver_meal(delivery_time):
    time.sleep(delivery_time)
    return f'Delivery took {delivery_time}s'