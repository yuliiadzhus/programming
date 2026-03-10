#1
text = "PyTHon"
print(text[0])
print(text[-1])
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text[2:4])

#2
text = "Hello world"
print(len(text))
print(text.count("l"))

#3
text = "Never gonna give you up, never gonna let you down Never gonna run around and desert you Never gonna make you cry, never gonna say goodbye Never gonna tell a lie and hurt you"
print(text.count("never"))

#4
text = "Text"
number = "1320"
print(text.isalpha())
print(text.isdigit())

#5
text = "I like cats"
print(text.replace("cats", "dogs"))

#6
print(len(text))
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.replace(" ", "_"))

#7
number = "123-456-789"
print(number.find("-"))

#8
text = "email: user@example.com"
print(text.split(":") [1].strip())

#9
text ="Hello, your id number is 32"
print(any(char.isdigit() for char in text))

#10
text = "qwertyagentbondqazwsx"
name = text[text.find("agent") : text.find("agent") + len("agent")].capitalize()
surname = text[text.find("bond") : text.find("bond") + len("bond")].capitalize()
print(name, surname)









