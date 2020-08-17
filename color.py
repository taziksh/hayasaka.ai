from PIL import Image
from pathlib import Path
import os 
from time import sleep
from colorthief import ColorThief

for root, dirs, files in os.walk('/home/tazik/Nextcloud/code/lbpcascade_animeface/examples/datasets/hand_tuned_larger_2x/'):
    #print(root, dirs, files)
    for name in files:
        print(name)
        color_thief = ColorThief(os.path.join(root, name))
        palette = color_thief.get_palette(color_count=2, quality=1)
        rgb = palette[0]
        delta_E = pow(rgb[0]-255, 2) + pow(rgb[1]-255,2) + pow(rgb[2], 2)
        print(delta_E)
        new_name = os.path.join(root, str(delta_E) + ".png")
        #print(new_name)
        os.rename(os.path.join(root, name), new_name)
