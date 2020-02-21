'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_all(word):
#     return word.count('th')


def count_th(word):
    # TBC
    occurence = 'th'
    word_len = len(word)
    occurence_len = len(occurence)
    # base case - word is empty or word length is less than occurence length
    if (word_len == 0 or word_len < occurence_len):
        return 0
    # check if occurence exists in the first part of word to the end of occurence length
    if (word[0:occurence_len] == occurence):
        return count_th(word[occurence_len - 1:]) + 1

    return count_th(word[occurence_len - 1:])


print(count_th('wothjdhjfth'))
