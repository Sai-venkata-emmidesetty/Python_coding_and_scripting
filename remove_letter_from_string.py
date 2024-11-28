def remove_letter(word,letter_to_remove):
        if letter_to_remove in word:
            word=word.replace(letter_to_remove,"")
        else:
            print("the entered letter is not in word")
        return word

word="chennai"
letter_to_remove=input(f"enter the letter to remoave from {word}: ")
print(remove_letter(word,letter_to_remove))


