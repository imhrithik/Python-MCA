def count_chars_words_lines(filename):
    with open(filename, 'r') as f:
        num_chars = 0
        num_words = 0
        num_lines = 0

        for line in f:
            num_lines += 1
            num_chars += len(line)
            words = line.split()
            num_words += len(words)
    return (num_chars, num_words, num_lines)

filename = 'file.txt'   
counts = count_chars_words_lines(filename)
print("Number of characters : ", counts[0])
print("Number of words : ", counts[1])
print("Number of lines : ", counts[2])