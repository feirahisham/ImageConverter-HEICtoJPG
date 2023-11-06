# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 07:59:51 2023

@author: feiramoh
"""

import os
from pathlib import Path

from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

targetDir = Path(input('Enter your file directory: '))

if os.path.isdir(targetDir):
    print(f'Target Directory:\n{targetDir}')
    os.chdir(targetDir)
else:
    print('Inserted path is not a directory')

for filename in os.listdir(os.getcwd()):
    currFile = os.path.join(os.getcwd(), filename)
    isCurrFileIsDir = os.path.isdir(currFile)
    if not isCurrFileIsDir:
        extensionHEIC = os.path.splitext(currFile)
        if extensionHEIC[1] == '.HEIC':
            convertedFolder = os.path.join(os.getcwd(), 'ConvertedImages')
            isConvertedFolderReady = os.path.exists(convertedFolder)
            if not isConvertedFolderReady:
                os.makedirs(convertedFolder)
                print("The new directory is created!")
            
            with Image.open(currFile) as img:
                targetFile = os.path.join(os.getcwd(), f'ConvertedImages/{filename.split(".")[0]}.jpg')
                isTargetFileExist = os.path.exists(targetFile)
                
                if not isTargetFileExist:
                    img.save(f'ConvertedImages/{filename.split(".")[0]}.jpg')
                    print(f'Done convert image {filename} to JPG format')
                else:
                    print(f'Image {filename.split(".")[0]} already exists in JPG format! -- I\'m not converting it again!')

print('All .HEIC files found in given folder have successfully converted to JPG format!')
