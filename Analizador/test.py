

file = open("/home/douglas/Documentos/TCC/MecTags.txt", "r")

for line in file:
    line = line.strip().upper()
    filereviews = open("/home/douglas/Documentos/TCC/Photomath.csv", "r")
    cont = 0
    for liner in filereviews:
        #print(liner)
        #review = liner.split(",")[1]
        #print(liner.find(line))
        if line in liner.upper():
            cont = cont + 1
    print(line + " :" + str(cont))
    filereviews.close()