text = "We have a package for you. Would you like to find out? Click this link to confirm your delivery address!"

#Given text is splitted into words when encounters white space
whitespace_omitted = text.split(" ")
#print(whitespace_omitted)

#Given text is splitted into words when encounters the word "Click". As a result we are given two seperated and the word 'click' omitted sentences.
#omitted_word = text.split("Click")
#print(omitted_word)

#empty list will store the words 
words = []
#keeps track of the current word, currently processed
current_word = ""
#punctuation marks are stored in a list for the simplicity to check either white space or a delimiter. 
delimiters = [".", "?", "!"]

for char in text:
    if char == " ":
        if not current_word == "":
            words.append(current_word)
            current_word = "" 
    elif char in delimiters:
        if current_word == "":
            words.append(char)
        else:
            words.append(current_word)
            words.append(char)
            current_word = ""
    else:
        current_word += char

print(words)
#it will be problematic when 'i.e' used or U.K. used.

#normalizing the features
