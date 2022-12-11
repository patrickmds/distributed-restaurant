import time

from celery import Celery


app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.task_routes = {
    'tasks.make_meal': {'queue': 'chef'},
    'tasks.deliver_meal': {'queue': 'delivery'}
}

@app.task
def make_meal(order):
    for item in order['item']:
        time.sleep(item.preparation_time)
    
    return order

@app.task
def deliver_meal(client_id):
    pass