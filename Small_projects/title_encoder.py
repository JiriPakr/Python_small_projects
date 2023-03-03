file = open("books.txt", "r")

for line in file:
    words = line.split(" ")
    str = ""
    for i in range(0,len(words)):
           str += words[i][0]
    print(str)

#your code goes here

file.close()