import cv2
from segment_anything import SamPredictor
from models.sam_model import import_sam
from models.yolo_model import import_yolo
from parse_input import parse_input

try:
    yolo = import_yolo()
    print("YOLO MODEL LOADED!")
except Exception as e:
    print("YOLO model couldn't be loaded")

try:
    sam = import_sam()
    print("SAM MODEL LOADED!")
except Exception as e:
    print("SAM model couldn't be loaded")

def fetch_class(image, class_name):
    predictions = yolo.predict(image)
    result = []

    # Fetching the bouning boxes of required class
    for prediction in predictions:
        names = prediction.names
        for box in prediction.boxes:
            name = names[int(box.cls[0])]
            if name == class_name:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                result = [x1, y1, x2, y2]
    return result

def main():
    # Fetching the inputs
    input_image_path, class_name, output_image_path = parse_input()

    image = cv2.imread(input_image_path)

    # Fetching the required class in the image 
    box = fetch_class(image, class_name)

    if box == []:
        print("The required class could not be predicted by the model")
        return

    # Making a SAM model to segment the bounding box
    mask_predictor = SamPredictor(sam)
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mask_predictor.set_image(image_rgb)

    masks, scores, logits = mask_predictor.predict(
        box=box,
        multimask_output = False
    )
    
if __name__ == "__main__":
    main()