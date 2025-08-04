from django.core.management.base import BaseCommand
import cv2
from confluent_kafka import Producer

class Command(BaseCommand):
    help = 'Captures webcam frames, preprocesses, and sends to Kafka'

    def handle(self, *args, **kwargs):
        producer = Producer({'bootstrap.servers': 'kafka:9092'})
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                continue
            # Preprocess (resize)
            frame = cv2.resize(frame, (640, 480))
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                producer.produce('frames', buffer.tobytes())
                producer.flush()
                print("Frame sent")
        cap.release()