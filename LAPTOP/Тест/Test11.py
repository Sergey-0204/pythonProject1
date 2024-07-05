ef single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word or word in root_word:
            same_words.append(word)
    return same_words

# Пример использования
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)