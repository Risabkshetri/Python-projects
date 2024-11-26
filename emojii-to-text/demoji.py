import emoji

def emoji_to_text(input_string):
    return emoji.demojize(input_string)


# Example usage
while True:
    text_with_emoji = input(str("Enter the text with emoji: "))
    converted_text = emoji_to_text(text_with_emoji)

    print("Original Text:", text_with_emoji)
    print("Converted Text:", converted_text)

    if input("Do you want to continue? (y/n): ") == 'n':
        break


