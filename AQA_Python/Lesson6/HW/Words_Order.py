
input_sentence = input("Please, enter the sentence using the space as separator: ")
sentence_lst = input_sentence.split()

for i in range(len(sentence_lst)):
    if sentence_lst[i].isdigit():
        sentence_lst[i] = int(sentence_lst[i])

is_sequence = False

for element in sentence_lst:
    idx = (sentence_lst.index(element))
    if type(sentence_lst[idx]) == str:
        if idx < len(sentence_lst)-2:
            if type(sentence_lst[idx+1]) == str and type(sentence_lst[idx+2]) == str:
                print(f'The three words are sequence are: {sentence_lst[idx]}, {sentence_lst[idx + 1]}, {sentence_lst[idx + 2]}')
                is_sequence = True

if not is_sequence:
    print(f"The sentence doesn't have the sequence words")

# ===== This task doesn't need tuple, but if it required:
# converted_sentence = tuple(sentence_lst)
#
# for element in converted_sentence:
#     idx = (converted_sentence.index(element))
#     if type(converted_sentence[idx]) == str:
#         if idx < len(converted_sentence)-2:
#             if type(converted_sentence[idx+1]) == str and type(converted_sentence[idx+2]) == str:
#                 print(f'The three words are sequence are: {converted_sentence[idx]}, {converted_sentence[idx + 1]}, {converted_sentence[idx + 2]}')
#                 is_sequence = True
#
# if not is_sequence:
#     print(f"The sentence doesn't have the sequence words")