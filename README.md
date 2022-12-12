# Final project - Distributed Computing
**Students**: Alexandre Müller Júnior & Patrick Machado da Silva

## Distributed Restaurant
Our goal with this project was abstracting a simple delivery-oriented application, simulating behaviours of famous options on the market. We thus developed a **REST API** using Python Flask that allows a remote client to send requests to a restaurant's server, registering itself by its email (`POST /client`) and then creating a new order object (`POST /order`).

To make things more interesting and improve on **scalability**, we also built a basic **Task Queue** implementation over Celery with the RabbitMQ message broker, modeling the delivery process of the order: after finishing the preparation of the order, it puts a new task on the queue, and one of the worker threads sleeps for `delivery_time` seconds abstracting the travel process.

As we have many different roles in our system, **heterogeneity** should be quite evident. Over time the project could be ported to many different platforms and thus run on many different devices with little changes on code. **Replicability** is easily obtained through running the `celery -A` command on multiple instances in a single our multiple machines; once again more of a infrastructure problem than a coding one. With replicability also comes **tolerance to failure**, as we can have as many instances as allowed by hardware and costs running on many different locations if needed be.

The implementation details of both the queue and the meal creation logic are known only to the `Restaurant` server and, in the queue's case, also the delivery workers, so we have `transparency` on the client side. This could allow changes in architecture going to a thin client if needed be, or a backend that doesn't rely on a specific front-end to work out (we don't even expose a front-end on this work, only a demo script, but as long as it has HTTP support we could virtually run any language or framework on the client front-end and still have a functioning application. Porting Restaurant and delivery code would be much harder)

## Running
The project mainly depends on Docker (runs the RabbitMQ image), Celery and Flask. Setup can be done via Makefile but basically we need to have a RabbitMQ instance running:

```sudo docker run -d -p 5672:5672 rabbitmq```

Then run one or more Celery instances (usually background is recommended, but the foreground will be better for verifying the Task Queue):

```celery -A tasks worker --loglevel=INFO -Q deliver_meal```

Finally, you can run our small demo that walks through the basic flow of the app without the hassle of all the ideas we had for the API over the past few days:

```python demo.py```


## Implementation notes
The Celery usage is really simple (once we figured it out) and goes over `tasks.py`. Flask logic involves most of the `distributed_restaurant/routes` folder and we encourage going through it to see all available routes on our system. 
