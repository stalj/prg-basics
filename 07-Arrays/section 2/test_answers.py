test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

question_number = len(test_results)

correct_answers = 0
wrong_answers = 0
for answer in test_results:
    if answer == True:
        correct_answers += 1
    else:
        wrong_answers += 1

percentage_correct = 100*correct_answers / question_number

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', wrong_answers)
print(f'Percentage of correct tasks {percentage_correct:.1f}%')