import os
folders = input ("Please provide folder name with space between: ").split()

for folder in folders:
   
   try:
     files = os.listdir(folder)

   except FileNotFoundError:
     print("please provide valid folders: looks like is invalid folders")
     continue

   except PermissionError:
      print("No acess to this folder:"+ folder)
      continue


print("-- listing a files for folders:" + folder)

for file in files:
     print(file)
