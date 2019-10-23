#This program was written by Connor Crowe

print("Remember, do no put a space before you answer!\n")
word1 = input("Type an action.")
word2 = input("Type a place.")
word3 = input("Type a color followed by a plural noun.")
word4 = input("Type a plural noun.")
word5 = input("Type a noun.")
word6 = input("Type an adjective.")
word7 = input("Type a noun.")
word8 = input("Type an adjective.")
word9 = input("Type a plural noun.")

text = str.format("One does not simply {} into {}.\
Its {} are guarded by more than just {}.\
There is evil there that does not sleep,\
and the {} is ever watchful. It is a {} wasteland,\
riddled with fire and {} and dust,\
the very air your breathe is\
a {} fume. Not with ten thousand {} could\
you do this. It is folly.",word1,word2,word3,word4,word5,word6,word7,word8,word9)

print(text)
