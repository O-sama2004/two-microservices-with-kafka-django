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
