
# Function to print a 2d list
def print_matrix(l):
    for i in range(len(l)):
        print(f'{l[i]} ')


def is_palindrome(substr, start, end, len_sub_str):
    result = True
    for position in range(0, (len_sub_str // 2) + 1):
        if substr[start + position] != substr[end - position]:
            return False
    return result

# This function prints the
# longest palindrome subString


def rebuild_words(x1, y1, full_word, init_word, palindromes, dp):
    n = len(full_word)
    pal = init_word
    while x1 > 0 and y1 < n and dp[x1][y1] == 1:
        pal = full_word[x1] + pal + full_word[x1]
        if len(pal) > 2:  # 1 and 2 word palindromes already added
            palindromes.append(pal)
        x1 = x1 - 1
        y1 = y1 + 1
    return palindromes


def assert_checking(seqs, string):
    for s in seqs:
        try:
            assert isinstance(string.index(s), int)
        except ValueError as error:
            print(f'not found substring: {s} in {string}')
