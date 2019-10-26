import json
dataString = "{ \
                \"ner\": \"Bat\", \
                \"nas\": 90,\"hayag\": {\
                    \"hot\": \"UB\",\
                    \"duureg\": \"BZD\"\
                },\
                \"toonuud\": [\
                    1, 2, 3\
                ]\
            }"

dataObject = json.loads(dataString)
print(dataObject)
print(dataObject["hayag"]["hot"])
print(dataObject["toonuud"][0])

myValue = {
    "key": "value",
    "number": 200,
    "arrayyy" : (0, 2, 4)
}
strVal = json.dumps(myValue)
writingFile = open("json_out.txt", "w")
writingFile.write(strVal)
writingFile.close()