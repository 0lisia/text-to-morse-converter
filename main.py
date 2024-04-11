
import pandas

data = pandas.read_csv("morse.csv")

#Creating a dictionary from the morse.csv
morse_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(morse_dict)

#Keeping the program running as long as user wants to keep inputing words
is_running = True
while is_running:
    #Creating a list of morse code based on input
    word = input("Enter a word or a sentence: \n").upper()
    morse_result = [morse_dict[letter] for letter in word]
    #Converting the code into a tring
    morse_code = ' '.join(morse_result)
    print(morse_code)
    #Giving the user ability to continue
    another_word = input("Do you want to convert another word? Input Y or N \n").upper()
    if another_word == "Y":
        is_running = True
    elif another_word == "N":
        is_running = False
    else:
        print("You input a wrong character")
        another_word = input("Do you want to convert another word? Input Y or N \n").upper()
        if another_word == "Y":
            is_running = True
        elif another_word == "N":
            is_running = False


