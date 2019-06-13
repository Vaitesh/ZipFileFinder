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
