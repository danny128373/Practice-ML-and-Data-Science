# ** What is 7 to the power of 4?**
print(7 ** 4)

# ** Split this string:**

# s = "Hi there Sam!"
# *into a list. *
s = "Hi there Sam!"
s = s.split()
print(s)

# ** Given the variables:**

planet = "Earth"
diameter = 12742
# ** Use .format() to print the following string: **
# The diameter of Earth is 12742 kilometers.
print("The diameter of {} is {} kilometers.".format(planet, diameter))

# ** Given this nested list, use indexing to grab the word "hello" **
lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
print(lst[3][1][2][0])

# ** Given this nested dictionary grab the word "hello".
d = {
    'k1':
    [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]
}
print(d['k1'][3]['tricky'][3]['target'][3])

# ** Create a function that grabs the email website domain from a string in the form: **

# user@domain.com
# So for example, passing "user@domain.com" would return: domain.com


def turn_to_url(email):
    return email.split('@')[1]


print(turn_to_url("user@domain.com"))

# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **


def if_dog(string):
    if 'dog' in string.lower():
        return True
    else:
        return False


print(if_dog("My dog is here."))
print(if_dog("My Dog is here"))
print(if_dog("My cat is here"))

# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **


def count_dog(string):
    count = string.lower().count('dog')
    return count


print(count_dog("Dog dog dog dog Dog cat!"))

# ** Create a function to filter out words from a list that don't start with the letter 's'. For example:**


def starts_with_s_words(lst):
    s_words = []
    for word in lst:
        if word[0].lower() == 's':
            s_words.append(word)
    return s_words


print(starts_with_s_words(['soup', 'dog', 'salad', 'cat', 'great']))
