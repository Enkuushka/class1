import os
value = os.path.exists("D:/apps/WindowsFormsApp1/no-file.sln")

isFile = os.path.isfile("D:/apps/WindowsFormsApp1/WindowsFormsApp1.sln")
isDir = os.path.isdir("D:/apps/WindowsFormsApp1")

print(isFile)
print(isDir)