### 1. Case Conversion Methods
text = "hello world"

print(text.capitalize())  
# Converts first character to uppercase → "Hello world"

print(text.upper())  
# Converts all characters to uppercase → "HELLO WORLD"

print(text.lower())  
# Converts all characters to lowercase → "hello world"

print(text.title())  
# Converts first letter of each word to uppercase → "Hello World"

print(text.swapcase())  
# Swaps uppercase to lowercase and vice versa → "HELLO WORLD"




### 2. Searching & Counting


print(text.count("o"))  
# Counts occurrences of 'o' → 2

print(text.find("world"))  
# Returns index of first occurrence → 6

print(text.index("world"))  
# Same as find(), but raises error if not found → 6

print(text.startswith("hello"))  
# Checks if string starts with "hello" → True

print(text.endswith("world"))  
# Checks if string ends with "world" → True




### 3. Checking String Properties


print("abc123".isalnum())  
# Checks if all characters are alphanumeric → True

print("abc".isalpha())  
# Checks if all are alphabets → True

print("123".isdigit())  
# Checks if all are digits → True

print("hello".islower())  
# Checks if all are lowercase → True

print("HELLO".isupper())  
# Checks if all are uppercase → True

print("Hello World".istitle())  
# Checks if string is title case → True

print("   ".isspace())  
# Checks if only whitespace → True




### 4. Trimming & Removing


text2 = "   hello world   "

print(text2.strip())  
# Removes spaces from both sides → "hello world"

print(text2.lstrip())  
# Removes spaces from left → "hello world   "

print(text2.rstrip())  
# Removes spaces from right → "   hello world"

print("hello.py".removesuffix(".py"))  
# Removes suffix → "hello"

print("unhappy".removeprefix("un"))  
# Removes prefix → "happy"




### 5. Splitting & Joining


print(text.split())  
# Splits string into list → ['hello', 'world']

print("a,b,c".split(","))  
# Split using comma → ['a', 'b', 'c']

print("hello\nworld".splitlines())  
# Splits at line breaks → ['hello', 'world']

print("-".join(["a", "b", "c"]))  
# Joins list into string → "a-b-c"




### 6. Replacing & Formatting


print(text.replace("world", "Python"))  
# Replaces substring → "hello Python"

name = "John"
print("Hello {}".format(name))  
# Formats string → "Hello John"




### 7. Alignment & Padding


print("hi".center(10))  
# Centers text with spaces → "    hi    "

print("hi".ljust(10))  
# Left aligns → "hi        "

print("hi".rjust(10))  
# Right aligns → "        hi"

print("5".zfill(3))  
# Pads with zeros → "005"




### 8. Partitioning


print("hello world".partition(" "))  
# Splits into tuple → ('hello', ' ', 'world')

print("hello world".rpartition(" "))  
# Splits from right → ('hello', ' ', 'world')




### 9. Encoding & Translation


print("hello".encode())  
# Converts string to bytes → b'hello'



table = str.maketrans("h", "H")
print("hello".translate(table))  
# Replaces characters using mapping → "Hello"


### 10. Tabs Handling

print("hello\tworld".expandtabs(4))  
# Replaces tab with spaces → "hello   world"

print("hello".isidentifier())  
# Checks if valid Python variable name → True

print("abc".isascii())  
# Checks if all characters are ASCII → True

print("123".isnumeric())  
# Checks if numeric characters → True

print("abc".isprintable())  
# Checks if printable → True

str1 = "hello"
print(list(str1))