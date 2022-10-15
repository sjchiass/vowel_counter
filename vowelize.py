def vowelize(word, vowels="AEIOU", handle_y=True):
    word = word.upper()
    v = sum(1 for x in word if x in vowels)
    if "Y" in word:
        # If there are no other vowels, then y is a vowel
        if v == 0:
            v = 1
        # If a y is surrounded by consonents, it is a vowel
        else:
            for l in range(1, len(word)-1):
                if word[l] == "Y" and word[l+1] not in vowels:
                    v += 1
            if word[-1] == "Y":
                v += 1
    return v
