# 2 strings that made with the same Characters


""" 

def check_the_string(s1, s2):
    if sorted(s1) == sorted(s2):
        print("They are anagram")
    else:
        print("They are not anagram ")


s1 = "listen"
s2 = "silent"
check_the_string(s1,s2) 

"""


def are_anagrams(s1, s2):
    # here we check the word by its length 
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}
    #These dictionaries will be used to store the frequency of characters in strings
    for ch in s1:
        
#This loop iterates over each character ch in the string s1
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
#checks the ch of 2 freq so if they are not same they are not anagram if they are same so it means they are anagram 
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True

print(are_anagrams('dadddd','silent'))
