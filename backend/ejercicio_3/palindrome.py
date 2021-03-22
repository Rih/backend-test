

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


def palindrome_subsequences(word):
    # precalculate dinamic programming N x N of characters coicidences
    n = len(word)
    # length 1
    dp = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        dp[i][i] = 1
    palindromes = list(word)
    # length 2
    pos = 0
    while pos < n - 1:
        if word[pos] == word[pos + 1]:
            for i in range(n):
                dp[pos][pos + 1] = 1
                dp[pos + 1][pos] = 1
            palindromes.append(word[pos] + word[pos + 1])
        pos = pos + 1

    # print_matrix(dp)
    # check words greater > 2
    for k in range(3, n + 1):
        for i in range(n):
            for j in range(i, n):
                # check
                if is_palindrome(word, i, j, j - i):
                    dp[i][j] = 1
                    dp[j][i] = 1
    # print_matrix(dp)
    # reconstruct words
    for i in range(1, n - 1):
        if dp[i][i + 1] == 1:  # even words
            x1 = i
            y1 = i + 1
            palindromes = rebuild_words(x1, y1, word, '', palindromes, dp)
        if i - 1 > 0 and dp[i - 1][i + 1] == 1:  # odd words
            x1 = i - 1
            y1 = i + 1
            palindromes = rebuild_words(x1, y1, word, word[i], palindromes, dp)
    return palindromes


def assert_checking_substr_found(seqs, string):
    for s in seqs:
        try:
            assert isinstance(string.index(s), int)
        except ValueError as error:
            print(f'not found substring: {s} in {string}')


if __name__ == '__main__':
    exit_condition = "!e"
    string = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'
    print(f"\n*********************************************")
    print(f"Executing exercise 3. ")
    print(f"The result will be an array with all ")
    print(f"string subsequences palindromes.")
    print(f"\nExecuting algorithm with input: \"{string}\"")
    print("Please wait...")
    subseq = palindrome_subsequences(string)
    print("\nAll subsequences found: ", subseq)
    assert_checking_substr_found(subseq, string)
    str_input = input(f"Enter other example, be gentle ;), I think recommended less than 600 chrs (Type \"{exit_condition}\" to exit): ")
    while str_input != exit_condition:
        subseq = palindrome_subsequences(str_input)
        print("\nAll subsequences found: ", subseq)
        str_input = input(f"Enter other example, be gentle ;), I think recommended less than 600 chrs (Type \"{exit_condition}\" to exit): ")
    print("Finish.")



