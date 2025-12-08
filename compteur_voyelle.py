t = input("Texte : ").lower()

voy = "aeiouyàáâäãéèêëìíîïòóôöùúûüÿ"
c = 0

for x in t:
    if x in voy:
        c += 1

print(c)
