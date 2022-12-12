import requests

from distributed_restaurant import __version__


SERVER_URL = 'http://localhost:5000'


def test_version():
    assert __version__ == '0.1.0'

# tests the default order workflow and serves as server demo
def test_create_order():
    # create test user
    fake_email = 'test@test.com'
    r = requests.post(f'{SERVER_URL}/client', json={'email':fake_email})
    assert r.status_code == 200
    print(r.content)

    # create order
    items = [{"id":  "1", "quantity": 2},
		    {"id":  "2", "quantity": 3}]
    r = requests.post(f'{SERVER_URL}/order', json={
        'email': fake_email,
        'items': items,
        'money': 300
    })
    assert r.status_code == 200
    print(r.content)
    # also observe the log of the terminal running the celery worker, it will
    # output the messages on the task queue
    

test_create_order()