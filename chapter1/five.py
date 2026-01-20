s = input("enter any words:").lower()  # this lower() is the method that will conver the string into lower case.
vowels = "aeiou"  # i have predefined the vowels 
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(f"Number of vowels: {count}")
