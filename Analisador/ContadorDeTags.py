

file = open("Z:\Playgroud\TCC\MacTags.txt", "r", encoding="utf8")

for line in file:
    line = line.strip().upper()
    filereviews = open("Z:\Playgroud\TCC\Photomath.csv", "r", encoding="utf8")
    cont = 0
    for liner in filereviews:
        #print(liner)
        #review = liner.split(",")[1]
        #print(liner.find(line))
        if line in liner.upper():
            cont = cont + 1
    print(line + " :" + str(cont))
    filereviews.close()