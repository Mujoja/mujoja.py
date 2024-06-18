def check_vowel_or_consonant(letter):
    vowels = "aeiouAEIOU"

    if letter.isalpha() and len(letter) == 1:
        if letter in vowels:
            return f"The letter '{letter}' is a vowel."
        else:
            return f"The letter '{letter}' is a consonant."
    else:
        return "Please enter a valid single letter."


def main():
    letter = input("Enter a letter: ")
    result = check_vowel_or_consonant(letter)
    print(result)


if __name__ == "__main__":
    main()
