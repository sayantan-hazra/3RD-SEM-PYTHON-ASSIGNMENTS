# Q6: Write a function that will reverse the individual words of a string.
# Example: "WELCOME TO TECHNO INDIA" → "EMOCLEW OT ONHCET AIDNI"

def reverse_words(sentence):
    words = sentence.split(" ")
    result = []
    for word in words:
        rev = ""
        for char in word:
            rev = char + rev
        result.append(rev)
    return " ".join(result)

# Example
print("Reversed words:", reverse_words("WELCOME TO TECHNO INDIA"))
