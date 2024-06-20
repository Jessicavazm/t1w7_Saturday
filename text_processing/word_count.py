def count_words(text):
    words = text.split()
    return len(words)

# You can use two methods/ modules in one variable. Another point in the code bellow is once you print unique words you can see the set is not ordered, that's the reason why you cannot use index with sets.

def unique_words(text):
    words = text.lower().split()
    return set(words)

print(count_words("Good Morning everybody, welcome to the session."))
print(unique_words("Good Morning everybody, welcome to the session."))


