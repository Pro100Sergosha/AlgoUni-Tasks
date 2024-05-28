# def main(start, end, divisor):
#     new_list = []
#     for i in range(start, end):
#         if i % divisor == 0:
#            new_list.append(i)
#     return new_list



# print(main(10, 50, 5))


# def is_anagram(word1, word2):
#     return sorted(word1) == sorted(word2)


print((lambda word1, word2: sorted(word1) == sorted(word2)) (input(), input()))

