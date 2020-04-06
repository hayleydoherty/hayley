fname = input("Enter file name: ")
l=input("Enter letter to be counted:")
count = 0
 
with open(fname, 'r') as f:             # with open- opens the file and ensures it is closed again 
    for line in f:                      # reading through each line of the text and splitting the lines into words
        words = line.split()
        for i in words:                 # splitting words down to letters
            for letter in i:
                if(letter==l):          # determining if the letter currently being read is the same as the letter input by the user
                    count= count+1      # if it is the same then 1 is added to the count (running total)    
print("Occurrences of the letter:")
print(count)