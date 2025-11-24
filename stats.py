def get_num_words(string):
    return len(string.split())

def get_count_of_each_letter(string):
    letters = {}
    text_lowercase = string.lower()
    for w in text_lowercase.split():
        for l in w:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
    return letters