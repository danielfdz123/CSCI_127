#Daniel Andres Fernandez
#daniel.fernandez16@myhunter.cuny.edu
#March 6, 2022
#This program outputs the total number of plural nouns

gi = input("Enter nouns: ")
word= gi.count(" ")
word1= word + 1
print("There are", word1, "words")

word2= gi.count("s ")

for i in gi:
    if gi[-1] == 's':
        word3 = word2 + 1
        fraction= word3 / word1
        print("Fraction of your list that is plural:", fraction)
    else:
        fraction11 = words2 / words1
        print("Fraction of your list that is plural:", fraction1)
        
