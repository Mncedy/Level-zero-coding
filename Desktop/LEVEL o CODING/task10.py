def vowelCheck(vc):
    vowels = "a","A","e","E","i","I","o","O","u","U"
    val = []
    for i in vc:
        if i in vowels:
            val.append(i)
    return val

vowel_string = input("Enter a wrord(s) or a sentence: ")
print(vowelCheck(vowel_string))