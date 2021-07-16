lines = []
with open("headers.txt") as f:
    lines = f.readlines()
str=""
for line in lines:
 ls=line.split(":")
 str+=("\'"+ls[0]+"\'"+":"+"\'"+ls[1].rstrip("\n").lstrip()+"\',\n")
print(str)
