from segment_anything import sam_model_registry
import os
from dotenv import load_dotenv

load_dotenv()

def import_sam():
    current_dir = os.getcwd()
    SAM_WEIGHTS_PATH = os.getenv("SAM_WEIGHTS_PATH")

    sam_checkpoint = os.path.join(current_dir, SAM_WEIGHTS_PATH)
    
    model_type = "vit_h"
    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)

    return sam

if __name__ == "main":
    import_sam()