def is_isogram(isogram):
    isogram = isogram.strip()
    isogram = isogram.lower()
    length = len(isogram)
    is_isogram = True
    for i in range(0, length):
        for j in range(i + 1, length):
            if isogram[i] == isogram[j]:
                is_isogram = False
                break
    return is_isogram


print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
