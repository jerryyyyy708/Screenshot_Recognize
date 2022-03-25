from PIL import Image
import os
import imghdr

def skip():
    return

loadpath='pictures/'#path of original image
savepath='screenshots/'#path to save image
filelist=os.listdir(loadpath)
index=0

for file in filelist:
    try:
        file_open=loadpath+file
        img=Image.open(file_open)
        new_img = img.resize((64, 64))
        file_save=savepath+str(index)+'.jpg'
        new_img.save(file_save)
        index+=1
    except IOError:
        skip()





