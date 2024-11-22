distances_traveled = [120, 150, 180, 90, 200, 175, 160]
print(distances_traveled)

distances_traveled.sort() 
print('Sort in increasing order', distances_traveled)

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
daily_temperatures.sort(reverse=True)
print('Sort in decreasing order', daily_temperatures)

file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

file_names.sort()
print('Sorting in ascending order:', file_names)