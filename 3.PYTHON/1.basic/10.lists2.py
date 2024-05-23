# 2. 문자열의 글자 수 세기
words = ["apple", "banana", "cherry", "dragonfruit"]
words_lengths = [len(lst) for lst in words]
# 출력: [5, 6, 6, 11]
print(words_lengths)

# 4. 문자열 리스트에서 길이가 3 이하인 단어들만 선택하기
words = ["apple", "banana", "cherry", "dragonfruit", "egg"]
short_words = [lst for lst in words if len(lst) < 4]
# 출력: ["egg"]
print(short_words)

# 5. 중첩 리스트 펼치기
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list1 = [y for y in x for x in nested_list]
flattened_list1 = [x for x in y for  in len(nested_list)]
# 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flattened_list1)
print(flattened_list2)

# 6. 특정 조건(5보다 큰것)을 만족하는 요소 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = [x for x in numbers if x > 4]
# 출력: [6, 7, 8, 9, 10]
print(greater_than_five)

# 7. 문자열 리스트에서 첫 글자가 모음인 단어들 선택하기
words = ["apple", "banana", "cherry", "apricot", "egg"]
vowel_starting_words = [x for x in words if x[0] in ("a", "e", "i", "u", "o")]
# 출력: ["apple", "apricot", "egg"]
print(vowel_starting_words)

