import pandas as pd
import wandb
import numpy as np

# df = pd.read_csv("C:\\Users\\qid\\Downloads\\hdvila\\sample_frame_list.txt")
# print(df.shape[0])
# print(df.iloc[1])

wandb.init()

pixels = np.random.randint(low=0, high=256, size=(48, 3, 224, 224))
t = pixels[0,:]
t=t.reshape((224,224,3))
print(t.shape)


image = wandb.Image(t)

