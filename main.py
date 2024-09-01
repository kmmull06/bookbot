def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Count words
    word_count = count_words(text)
    
    # Count character frequencies
    char_freq = char_freqs(text)
    
    # Print the text (optional, but useful for debugging)
    # print(text)
    
    # Print the word count
    print("Number of words in the book:", word_count)
    
    # Print the character frequencies
    print("\nCharacter frequencies:")
    print(char_freq)

    # Print Report
    print_report(word_count, char_freq)

def get_book_text(path):
    with open(path, 'r') as f:  # Ensure the file is opened in read mode
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def char_freqs(text):
    text = text.lower()  # Convert text to lowercase
    freq_dict = {}
    
    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    
    return freq_dict

def print_report(word_count, char_freq):
    freq_list = [{"char": char, "count": count} for char, count in char_freq.items()]
    freq_list.sort(key=lambda x: x["count"], reverse=True)

    # Print the Report
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in document:")
    print()

    for entry in freq_list:
        print(f"The '{entry['char']}' character was found {entry['count']} times")

    print ("--- End Report ---")

# Call the main function
if __name__ == '__main__':
    main()
