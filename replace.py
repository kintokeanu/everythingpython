#create a function to replace word
def replace_word():

  # string from which user will select word
    string = "My name is Brian kevu"
    
   #prompt user
    word_to_replace = input("Enter word to replace: ")
    replacement_word = input("Enter word replacement: ")
    print(str.replace(word_to_replace, replacement_word))

    #call the function
replace_word()
