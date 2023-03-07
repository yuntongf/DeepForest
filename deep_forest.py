# from albumentations.pytorch import ToTensorV2
from io import BytesIO
import torch
from deepforest import main 
from deepforest import get_data
from deepforest import main
from deepforest import get_data
import matplotlib.pyplot as plt
import base64

model = main.deepforest()
model.use_release()
model = main.deepforest()

def deep_forest(): 
    model_path='./model/70epchs.pth'  #path to pretrained model 
    model.model.load_state_dict(torch.load(model_path, map_location ='cpu')) #load the save model, trained on boston dataset

    raster_path = get_data("/Users/omgitsmonday/Desktop/094.jpeg")
    # Window size of 300px with an overlap of 25% among windows for this small tile.
    predicted_raster = model.predict_tile(raster_path, return_plot = True, patch_size=300,patch_overlap=0.25)
    plt.imshow(predicted_raster[:,:,::-1])

    # save image in base64 and render img component
    image_buf = BytesIO()
    plt.savefig(image_buf, format='png')
    data = base64.encodestring(image_buf.getbuffer()).decode("ascii")
    return data

print(deep_forest())