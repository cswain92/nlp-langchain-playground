def count_text_file(file_path):
    line_count = 0
    word_count = 0
    char_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    return line_count, word_count, char_count


if __name__ == "__main__":
    file_path = "../../data/sample.txt"
    lines, words, characters = count_text_file(file_path)

    print(f"Lines: {lines}, Words: {words}, Characters: {characters}")
