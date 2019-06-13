#Listing the files/folders present in zipfile
from zipfile import Zipfile
file_name = input('Please enter the folder/file name: ')

with Zipfile(file_name, 'r') as zip:
    zip.printdir()
    
