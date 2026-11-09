def main():
    filename = input("Enter the name of the input file: ").strip()
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    words_list = text.split()
    unique_words = set(words_list)
    
    word_counts = {}
    for word in unique_words:
        word_counts[word] = words_list.count(word)
        
    print(f"{'Word':<15} {'Occurrences'}")
    print("-" * 45)
    
    for word, count in word_counts.items():
        print(f"{word:<15} {count}")

if __name__ == '__main__':
    main()