def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'demo.txt'
result = count_words(file_path)

if result is not None:
    print(f"The word count of '{file_path}' is: {result}")