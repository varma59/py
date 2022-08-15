file = open("file.txt" , 'r')
count = 0
for line in file:
    word = line.split(" ")
    count += len(word)
file.close()
print('no of words in file : ', count)

#file.txt 
#hello abhishek varma how are you
#Python program to count number of words in a Text File
