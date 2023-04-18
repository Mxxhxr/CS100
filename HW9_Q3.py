import string


def repeat_words(in_file, out_file):
    inF = open(in_file, 'r')
    outF = open(out_file, 'a')
    for line in inF:
        words = line.lower().strip().translate(
            str.maketrans('', '', string.punctuation)).split()
        repeatedWords = set()
        repeated = []
        for word in set(words):
            if words.count(word) > 1 and word not in repeatedWords:
                repeated.append(word)
                repeatedWords.add(word)
        outF.write(' '.join(repeated) + '\n')
