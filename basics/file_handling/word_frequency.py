def count_word_frequency(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()

            for word in words:
                word = word.lower().strip('.,!?;:"')
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


if __name__ == "__main__":
    filepath = "../../data/sample.txt"
    result = count_word_frequency(filepath)
    print(result)
