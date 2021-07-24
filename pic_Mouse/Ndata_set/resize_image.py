import os,sys
import numpy as np
from skimage.transform import rescale, resize
from skimage.io import imread, imsave

def rename_file(folder,N):
    
    for idx,filename in enumerate(os.listdir(folder)):
        if os.path.isfile(folder+"/"+str(N)+f"_0{idx}_"+"AD11.png"):
            continue
        os.rename(folder+"/"+filename,folder+"/"+str(N)+f"_0{idx}_"+"AD11.png")

def main(folder,N):
    for filename in os.listdir(folder):
        image = imread(folder+"/"+filename)
        image_resized = resize(image, (28, 28),anti_aliasing=True)
        imsave(folder+"/"+filename,image_resized)        
    rename_file(folder,N)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Please input directory name followed by image number")
    main(str(sys.argv[1]),sys.argv[2])

