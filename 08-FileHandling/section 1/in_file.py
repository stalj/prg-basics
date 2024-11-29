file_name = 'it_company.csv'

job_title = 'Software Engineer'

count = 0
with open(file_name, "r") as myfile:
    for line in myfile:
      if job_title in line:
        count += 1

print(f"{job_title} appears in the text {count} times")