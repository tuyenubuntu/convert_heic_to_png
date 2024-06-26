# -*- coding: utf-8 -*-
"""convert_heic_to_png.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14wL_FXJ8YXkcntCvwhDXMpdlOZ1GD4Cg
"""

#command conect to your google Drive
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
#go to folder work
# %cd /content/drive/MyDrive/HcP/folder_1                #input your path

# Commented out IPython magic to ensure Python compatibility.
#install lib for program convert
# %pip install heic2png

#Funct for covert heic to png
import os
from os import path
import glob
import shutil
from PIL import Image
from heic2png import HEIC2PNG
path =''
#os.listdir(os.path.expanduser('*.heic'))
lst = glob.glob(os.path.join(path,'*heic'))
print (type(lst))
for i in lst:
  if os.path.exists('Convert') == False:
    name_folder = 'Convert'
    os.mkdir(name_folder)
  else:
    pass
  try:
    shutil.copy(os.path.join(path,i),os.path.join(path,f'{name_folder}/{i}'))
    #print("File copied successfully.")
    img = HEIC2PNG(os.path.join(path,f'{name_folder}/{i}'), quality = 90)
    img.save()
    os.remove(os.path.join(path,f'{name_folder}/{i}'))
    print(f"File {i} converted successfully to *.png.")
  # If source and destination are same
  except shutil.SameFileError:
    print("Source and destination represents the same file.")
  # If there is any permission issue
  except PermissionError:
    print("Permission denied.")
  # For other errors
  except:
    print("Error occurred while copying file.")

print ('Finish ALL!')


lst2 = glob.glob(os.path.join(path,'*jpg'))
for i in lst2:
  shutil.copy(os.path.join(path,i),os.path.join(path,f'{name_folder}/{i}'))
len(lst2 + lst)
print ('Done')