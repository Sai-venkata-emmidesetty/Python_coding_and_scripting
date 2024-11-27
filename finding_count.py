#you have to repeat letters in s n number of times
#eg: if n=10, _ _ _ _ _ _ _ _ _ _
#in above spcaes we can put abaabaabaa - 10 spaces
#a is repeated 7 times in those 10 dashes.
#so your output should be 7
s="aba"
n=10
length_of_s=len(s)
a_repeated_times_in_s=s.count("a")
#number of elements(word 's') that can fit in 20spaces, // gives int value
finder1=n//length_of_s

#finder 2 will give us the remainder(remaining elements )
finder2=n%length_of_s

#here 2 is number of times "a" was repeated in s
counted=(finder1*a_repeated_times_in_s)+s[:finder2].count("a")

print(counted)

