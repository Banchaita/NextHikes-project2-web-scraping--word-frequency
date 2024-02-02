def calculate_word_frequency(file_path):
    # Step 1: Open and read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Step 2: Tokenize the text into words
    words = text.split()

    # Step 3: Count the frequency of each word
    word_frequency = {}
    for word in words:
        # Convert the word to lowercase to ensure case-insensitivity
        word = word.lower()
        # Remove punctuation and special characters
        word = word.strip('.,!?"\'()-_')

        # Update the word frequency dictionary
        if word:
            word_frequency[word] = word_frequency.get(word, 0) + 1

    # Step 4: Display or save the word frequencies
    for word, frequency in word_frequency.items():
        print(f'{word}: {frequency} times')

calculate_word_frequency('demo.txt')





