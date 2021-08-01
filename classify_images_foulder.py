import os
import pandas as pd

## Our directory is not classified images properly
## So Here we would create a python script to classify dataset directory
csvFile = pd.read_csv('images.csv')

## Create foulder
os.system('mkdir dataset')

classes_tuple = csvFile.drop_duplicates(subset=["label"])
## create class sub-directories
for label in classes_tuple.label:
    ## If the label contains space replace it with underline
    os.system('mkdir dataset\\' + label.replace(' ','_'))

## copy images to new dataset directory
for image_name in csvFile.image:
    ## get the value of image selected from dataframe
    ## If the label contains space replace it with underline
    image_label = csvFile.loc[ csvFile.image == image_name].label.values[0].replace(' ','_')

    ## Note copy command is for windows users
    ## If your a linux user change it to cp
    command = 'copy images_compressed\\' + image_name + '.jpg dataset\\'  + image_label
    print(command)
    ## Execute command and create new dataset directory
    os.system(command = command)
