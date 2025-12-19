# Check if a string is a **palindrome

text = input("Enter the word: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("Palindrome")
else: 
    print("Not Palindrome")