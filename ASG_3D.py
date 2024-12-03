c = input("Enter character: ")
match c:
    case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
        print("Vowel")
    case _ if len(c) == 1 and c.isalpha():
        print("Consonant")
    case _:
        print("Invalid input")