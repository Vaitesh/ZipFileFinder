import os, os.path
#to determine number of files in CWD
print(len[filename for filename in os.listdir('.') if os.path.isfile(filename)])

#to determine the files with naming of other versions
dir = '/tmp'
print(len[filename for filename in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

#to recursively find the files in the subdirectory use os.walk
for (root,dirs,files) in os.walk(dir, topdown=true):
  print(root)
  print(dirs)
  print(files)

  #working code to get the list of files present in zip archive
  import os, os.path

directory = input('Please specify the path: ')
print(directory)
#print(len([filename for filename in os.listdir(directory) if os.path.isfile(directory)]))
print(len([filename for filename in os.listdir(directory)])) #if os.path.isfile(filename)]))

#to determine the files with naming of other versions
#dir = '/tmp'
#print(len[filename for filename in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

from zipfile import ZipFile, is_zipfile, ZipInfo

#file_to_find = input('Please specify the filename')
for filename in os.listdir(directory):
    if is_zipfile(filename):
        with ZipFile(filename, 'r') as zip:
            #if File name = file_to_find:
                #print('Found')
            zip.printdir()
            #class ZipInfo(filename,(1980, 1, 1, 0, 0, 0)):
                #def __init__(self):
                    #list_of_files = infolist()

            #list_of_files = ZipInfo()

#creating class for zipinfo
