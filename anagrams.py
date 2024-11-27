def check_anagrams(word1,word2):
    return sorted(word1)==sorted(word2)

word1=input("enter the word1 to check")
word2=input("enter the word2 to check")
print(check_anagrams(word1,word2))