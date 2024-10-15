total_task=20
correct_answers = int(input("Number of correct anserws: "))
if total_task/2 <= correct_answers:
    print("Test passed!")
else:
    print("Test failed!")