from django.core.management.base import BaseCommand
from confluent_kafka import Consumer
import numpy as np
import cv2
from ultralytics import YOLO

class Command(BaseCommand):
    help = 'Consumes frames from Kafka and runs YOLOv8 inference'

    def handle(self, *args, **kwargs):
        consumer = Consumer({
            'bootstrap.servers': 'kafka:9092',
            'group.id': 'inference-group',
            'auto.offset.reset': 'earliest'
        })
        consumer.subscribe(['frames'])
        model = YOLO('yolov8n.pt')  # Or another YOLOv8 model for speed

        while True:
            msg = consumer.poll(1.0)
            if msg is None or msg.error():
                continue
            npimg = np.frombuffer(msg.value(), np.uint8)
            frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            results = model(frame)
            annotated_frame = results[0].plot()
            cv2.imwrite('/output/inferenced_frame.jpg', annotated_frame)
            print("Frame processed and saved")