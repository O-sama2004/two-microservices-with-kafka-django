# Webcam YOLOv8 Microservice Demo

This project demonstrates a simple microservices architecture using Docker Compose, Django, and Kafka to stream webcam frames, run YOLOv8 object detection, and view the results in your browser.

## How it Works

- **capture_service**: Captures webcam frames and sends them to a Kafka topic.
- **inference_consumer**: Listens to Kafka, runs YOLOv8 inference, and saves the result image.
- **inference_web**: Django web server that shows the latest inference image in your browser.
- **Kafka & Zookeeper**: Messaging backbone for the services.

## Quick Start

1. **Clone this repo:**
    ```sh
    git clone https://github.com/O-sama2004/two-microservices-with-kafka-django.git
    cd two-microservices-with-kafka-django
    ```

2. **Launch all services:**
    ```sh
    docker compose up --build
    ```

3. **View live results:**
    Open [http://localhost:8000/webcam/](http://localhost:8000/webcam/) in your browser to see live detections!

## Requirements

- Docker and Docker Compose
- (Linux only: a webcam at `/dev/video0`; otherwise, adjust/remove device mapping)

## Typical Folder Structure
```
project-root/
│
├── capture_service/
│   ├── capture_service/            # Django project for capture_service
│   ├── capture_app/                # Django app
│   │   └── management/
│   │       └── commands/
│   │           └── capture_send.py
│   ├── Dockerfile
│   ├── manage.py
│   └── requirements.txt
│
├── inference_service/
│   ├── inference_service/          # Django project for inference_service
│   ├── inference_app/              # Django app
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── consume_infer.py
│   │   └── templates/
│   │       └── webcam.html
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   └── yolov8n.pt                  # YOLOv8 model file
│
├── output/                         # Shared by inference_consumer and inference_web
│   └── inferenced_frame.jpg        # The latest inference result (auto-generated)
│
├── docker-compose.yml
└── README.md
```

## Stopping Services

```sh
docker compose down
```
### Troubleshooting
Try ```sh docker compose down -v ```to clean up Docker volumes and try again
If you can’t connect to Kafka, make sure all containers are running: docker compose ps
If no image appears on the webpage, confirm inferenced_frame.jpg is being created in output/
If on Mac or Windows, you may need to remove/edit the devices: key in capture_service in docker-compose.yml
