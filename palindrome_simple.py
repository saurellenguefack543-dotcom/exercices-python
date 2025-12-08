t = input("Texte : ").lower()

if t == t[::-1]:
    print("Palindrome")
else:
    print("Pas palindrome")
