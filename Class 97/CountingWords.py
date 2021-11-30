CountingWords=input("enter string:")
CharacterCount=0
WordCount=1

for i in CountingWords:
    CharacterCount=CharacterCount+1
    if(i==' '):
        WordCount=WordCount+1

print("Number of word in the string:")
print(WordCount)
print("Number of character in the string:")
print(CharacterCount)