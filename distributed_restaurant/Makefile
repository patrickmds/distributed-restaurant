
echo "Setting up RabbitMQ (message broker for Celery) as docker image"
echo "Since it's running a Docker image, it may need your sudo password"
sudo docker run -d -p 5672:5672 rabbitmq

echo "Starting celery delivery instance"
celery -A tasks worker --loglevel=INFO -Q deliver_meal
