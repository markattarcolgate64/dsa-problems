# You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern. 

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.
# – Where there is a 0 in the pattern, there is a vowel in the substring. 
# – Where there is a 1 in the pattern, there is a consonant in the substring. 

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

# Example

# For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
# – “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
# – “010” doesn’t match source[1..3] = "maz" 
# – “010” matches source[2..4] = "azi" 
# – “010” doesn’t match source[3..5] = "zin" 
# – “010” doesn’t match source[4..6] = "ing"

# So, there are 2 matches. For a visual demonstration, see the example video. 

# For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
# – There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

# Guaranteed constraints:
# 1 ≤ source.length ≤ 103
# 1 ≤ pattern.length ≤ 103

#Solution to this is to create a sliding window that is the size of the pattern and iterate through the string to match the pattern
#We can check whether something is a vowel in constant time because fixed length arr of vowels
# 
def pattern_match(pattern: str, source: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    #Construct the window 
    patternLen = len(pattern)
    count = 0 
    for i in range(len(source)):
        if i + patternLen <= len(source):
            pattern_match = True
            for j in range(i, patternLen+i):
                patternLet = pattern[j-i]
                compareLet = source[j]
                vowel = compareLet in vowels 
                if (patternLet == '0' and not vowel) or (patternLet == '1' and vowel):
                    pattern_match = False
                    break
            if pattern_match == True:
                count += 1
            print()

            
        #Check the size of the window
        
            
    return count 


def main():
    testStr1 = "amazing"
    pattern = "010"
    print(pattern_match(pattern,testStr1))




if __name__ == "__main__":
    main()

