import json
import glob
from tqdm import tqdm
import base64
import numpy as np
from PIL import Image
import io

for index,file in enumerate(tqdm(glob.glob("data/dataset_661/*.json"))):
    with open(file) as f:
        val = json.load(f)
        image_data = base64.b64decode(val['imageData'])
        image = Image.open(io.BytesIO(image_data))
        data = val['shapes']

        with open(f"data/dataset/annotations/{index}.json","w") as f:
            json.dump(data,f)
        image.save(f"data/dataset/images/{index}.jpg")

pass