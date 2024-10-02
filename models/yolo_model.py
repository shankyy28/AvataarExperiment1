from ultralytics import YOLO
from dotenv import load_dotenv
import os

load_dotenv()

def import_yolo():
    current_dir = os.getcwd()
    YOLO_MODEL_PATH = os.path.join(current_dir, os.getenv('YOLO_MODEL_PATH'))

    yolo = YOLO(YOLO_MODEL_PATH)
    
    return yolo

if __name__ == "main":
    import_yolo()