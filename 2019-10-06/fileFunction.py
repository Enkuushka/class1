fileObject = open("my-file.txt", "w")

#fileObject.write("The text")
#fileObject.write("\n")
#fileObject.write(str(123))

# while True:
#     line = fileObject.readline()
#     if(line != ""):
#         print(line)
#     else:
#         break

fileObject.write("Long text %f is value." % 10.0)

fileObject.close()

print(fileObject)