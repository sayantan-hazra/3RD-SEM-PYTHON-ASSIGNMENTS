# Q3: Write a function that takes three string input 
#     and find the common vowels among them.

def common_vowels(s1, s2, s3):
    vowels = "aeiou"
    common = []
    for v in vowels:
        if v in s1.lower() and v in s2.lower() and v in s3.lower():
            common.append(v)
    return common

# Example
print("Common vowels:", common_vowels("education", "reduction", "production"))
