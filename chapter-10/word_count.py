def count_words(filename):
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = "alice.txt"
count_words(filename)


filenames = ["alice.txt", "pi_digits.txt"]

for filename in filenames:
    count_words(filename)