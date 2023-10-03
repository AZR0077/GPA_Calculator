import tkinter as tk

class_grade = ""

high_school_levels = ["freshman", "sophomore", "junior", "senior"]

root = tk.Tk()
root.title('Calculator')
root.geometry('700x750')
root.config(bg = 'Gray81')

font_config = 'Arial'

editor1 = tk.Text()
editor1.place(x=170, y=85, width=350, height=100)
editor1.configure(font=(font_config, 10))

average1 = tk.StringVar()
average1.set("Your Average Is: ")
average1_label = tk.Label(textvariable = average1)
average1_label.place(x = 290, y = 195)

# Grade calculator

def check_average():
  global class_grade
  letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
  points_total = 0
  points_earned = 0
  text1 = editor1.get('1.0', 'end-1c')
  grades_list = text1.split(",")
  for grade in grades_list:
    list = grade.split("/")
    points_earned += int(list[0])
    points_total += int(list[1])
  average = (points_earned / points_total) * 100
  if average >= 96.5 and average <= 100:
    class_grade = letter_grades[0]
  elif average >= 92.5 and average < 96.5:
    class_grade = letter_grades[1]
  elif average >= 89.5 and average < 92.5:
    class_grade = letter_grades[2]
  elif average >= 86.5 and average < 89.5:
    class_grade = letter_grades[3]
  elif average >= 82.5 and average < 86.5:
    class_grade = letter_grades[4]
  elif average >= 79.5 and average < 82.5:
    class_grade = letter_grades[5]
  elif average >= 76.5 and average < 79.5:
    class_grade = letter_grades[6]
  elif average >= 72.5 and average < 76.5:
    class_grade = letter_grades[7]
  elif average >= 69.5 and average < 72.5:
    class_grade = letter_grades[8]
  elif average >= 66.5 and average < 69.5:
    class_grade = letter_grades[9]
  elif average >= 62.5 and average < 66.5:
    class_grade = letter_grades[10]
  elif average >= 59.5 and average < 62.5:
    class_grade = letter_grades[11]
  else:
    class_grade = letter_grades[12]
  average1.set("Your Average Is: " + class_grade) 

calculate_description = tk.Label(text = "Enter In The Format: (Points Earned)/(Points Total), (Points Earned)/(Points Total)")
calculate_description.place(x = 140, y = 55)

calculate_button = tk.Button(text = 'Calculate Letter Grade', command = check_average, bg = 'ORANGE', activebackground='#FFD580')
calculate_button.place(x = 280, y = 20)

#GPA calculator

high_school_gpa1 = [0, 0, 0, 0]
high_school_gpa2 = ["Freshman Year: ", "Sophomore Year: ", "Junior Year: ", "Senior Year: "]

grade1 = tk.StringVar()
grade1.set(high_school_gpa2[0])
grade2 = tk.StringVar()
grade2.set(high_school_gpa2[1])
grade3 = tk.StringVar()
grade3.set(high_school_gpa2[2])
grade4 = tk.StringVar()
grade4.set(high_school_gpa2[3])

grade1_label = tk.Label(textvariable = grade1)
grade1_label.place(x = 300, y = 550)
grade2_label = tk.Label(textvariable = grade2)
grade2_label.place(x = 300, y = 570)
grade3_label = tk.Label(textvariable = grade3)
grade3_label.place(x = 300, y = 590)
grade4_label = tk.Label(textvariable = grade4)
grade4_label.place(x = 300, y = 610)
gpa_info = tk.StringVar()

def calculate_gpa():
  letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
  
  qualitypoints_cp = [4.33, 4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 1.00, 0.67, 0.00]
  
  qualitypoints_honors = [5.00, 4.67, 4.33, 4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 1.33, 0.00]
  
  qualitypoints_ap = [5.33, 5.00, 4.67, 4.33, 4.00, 3.67, 3.33, 3.00, 2.67, 2.33, 2.00, 1.67, 0.00]
  
  num_subjects = 7
  total_qualitypoints = 0
  
  index = letter_grades.index(letter_grade1.get()) 
  if subject_level1.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level1.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level1.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index]

  index = letter_grades.index(letter_grade2.get()) 
  if subject_level2.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level2.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level2.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index] 

  index = letter_grades.index(letter_grade3.get()) 
  if subject_level3.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level3.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level3.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index] 

  index = letter_grades.index(letter_grade4.get()) 
  if subject_level4.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level4.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level4.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index] 

  index = letter_grades.index(letter_grade5.get()) 
  if subject_level5.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level5.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level5.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index] 

  index = letter_grades.index(letter_grade6.get()) 
  if subject_level6.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level6.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level6.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index]   
    
  index = letter_grades.index(letter_grade7.get()) 
  if subject_level7.get().lower() == "cp":
    total_qualitypoints += qualitypoints_cp[index]
  elif subject_level7.get().lower() == "honors":
    total_qualitypoints += qualitypoints_honors[index]
  elif subject_level7.get().lower() == "ap":
    total_qualitypoints += qualitypoints_ap[index]   
    
  gpa = total_qualitypoints / num_subjects

  high_school_levels = ["Freshman", "Sophomore", "Junior", "Senior"]
  
  index = high_school_levels.index(high_school_level.get()) 
  if high_school_level.get() == "Freshman":
    high_school_gpa1[0] = gpa
    high_school_gpa2[0] = "Freshman Year: " + str(gpa)
  elif high_school_level.get() == "Sophomore":
    high_school_gpa1[1] = gpa
    high_school_gpa2[1] = "Sophomore Year: " + str(gpa)
  elif high_school_level.get() == "Junior":
    high_school_gpa1[2] = gpa
    high_school_gpa2[2] = "Junior Year: " + str(gpa)
  elif high_school_level.get() == "Senior":
    high_school_gpa1[3] = gpa
    high_school_gpa2[3] = "Senior Year: " + str(gpa)
    
  grade1.set(high_school_gpa2[0])
  grade2.set(high_school_gpa2[1])
  grade3.set(high_school_gpa2[2])
  grade4.set(high_school_gpa2[3])
  
  overall_gpa = 0
  if len(high_school_gpa1) > 0:
    for i in range(0, len(high_school_gpa1)):
      overall_gpa += high_school_gpa1[i]
    overall_gpa = overall_gpa / len(high_school_gpa1)
    gpa_info.set("Your overall gpa is " + str(round(overall_gpa, 2)))
  
calculate_gpa_button = tk.Button(text = 'Calculate GPA', command = calculate_gpa, bg = 'ORANGE', activebackground='#FFD580')
calculate_gpa_button.place(x = 292, y = 240)

letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]

grades_label = tk.Label(text = "Letter grade")
grades_label.place(x = 480, y = 290)

letter_grade1 = tk.StringVar(root)
letter_grade1.set(letter_grades[1]) # default value
grades1_dropdown = tk.OptionMenu(root, letter_grade1, *letter_grades)
grades1_dropdown.place(x = 490, y =320)
grades1_dropdown.config(bg="GREEN", fg="WHITE")
grades1_dropdown["menu"].config(bg="#D0F0C0")

letter_grade2 = tk.StringVar(root)
letter_grade2.set(letter_grades[1]) # default value
grades2_dropdown = tk.OptionMenu(root, letter_grade2, *letter_grades)
grades2_dropdown.place(x = 490, y = 350)
grades2_dropdown.config(bg="GREEN", fg="WHITE")
grades2_dropdown["menu"].config(bg="#D0F0C0")

letter_grade3 = tk.StringVar(root)
letter_grade3.set(letter_grades[1]) # default value
grades3_dropdown = tk.OptionMenu(root, letter_grade3, *letter_grades)
grades3_dropdown.place(x = 490, y = 380)
grades3_dropdown.config(bg="GREEN", fg="WHITE")
grades3_dropdown["menu"].config(bg="#D0F0C0")

letter_grade4 = tk.StringVar(root)
letter_grade4.set(letter_grades[1]) # default value
grades4_dropdown = tk.OptionMenu(root, letter_grade4, *letter_grades)
grades4_dropdown.place(x = 490, y = 410)
grades4_dropdown.config(bg="GREEN", fg="WHITE")
grades4_dropdown["menu"].config(bg="#D0F0C0")

letter_grade5 = tk.StringVar(root)
letter_grade5.set(letter_grades[1]) # default value
grades5_dropdown = tk.OptionMenu(root, letter_grade5, *letter_grades)
grades5_dropdown.place(x = 490, y = 440)
grades5_dropdown.config(bg="GREEN", fg="WHITE")
grades5_dropdown["menu"].config(bg="#D0F0C0")

letter_grade6 = tk.StringVar(root)
letter_grade6.set(letter_grades[1]) # default value
grades6_dropdown = tk.OptionMenu(root, letter_grade6, *letter_grades)
grades6_dropdown.place(x = 490, y = 470)
grades6_dropdown.config(bg="GREEN", fg="WHITE")
grades6_dropdown["menu"].config(bg="#D0F0C0")

letter_grade7 = tk.StringVar(root)
letter_grade7.set(letter_grades[1]) # default value
grades7_dropdown = tk.OptionMenu(root, letter_grade7, *letter_grades)
grades7_dropdown.place(x = 490, y = 500)
grades7_dropdown.config(bg="GREEN", fg="WHITE")
grades7_dropdown["menu"].config(bg="#D0F0C0")

high_school_levels = ["Freshman", "Sophomore", "Junior", "Senior"]

levels_label = tk.Label(text = "Level")
levels_label.place(x = 130, y = 290)

high_school_level = tk.StringVar(root)
high_school_level.set(high_school_levels[0]) # default value
levels_dropdown = tk.OptionMenu(root, high_school_level, *high_school_levels)
levels_dropdown.place(x = 100, y = 320)
levels_dropdown.config(bg="GREEN", fg="WHITE")
levels_dropdown["menu"].config(bg="#D0F0C0")

subject_levels = ["CP", "Honors", "AP"]

subject_levels_label = tk.Label(text = "Subject level")
subject_levels_label.place(x = 380, y = 290)

subject_level1 = tk.StringVar(root)
subject_level1.set(subject_levels[0]) # default value
subject_level1_dropdown = tk.OptionMenu(root, subject_level1, *subject_levels)
subject_level1_dropdown.place(x = 390, y = 320)
subject_level1_dropdown.config(bg="GREEN", fg="WHITE")
subject_level1_dropdown["menu"].config(bg="#D0F0C0")

subject_level2 = tk.StringVar(root)
subject_level2.set(subject_levels[0]) # default value
subject_level2_dropdown = tk.OptionMenu(root, subject_level2, *subject_levels)
subject_level2_dropdown.place(x = 390, y = 350)
subject_level2_dropdown.config(bg="GREEN", fg="WHITE")
subject_level2_dropdown["menu"].config(bg="#D0F0C0")

subject_level3 = tk.StringVar(root)
subject_level3.set(subject_levels[0]) # default value
subject_level3_dropdown = tk.OptionMenu(root, subject_level3, *subject_levels)
subject_level3_dropdown.place(x = 390, y = 380)
subject_level3_dropdown.config(bg="GREEN", fg="WHITE")
subject_level3_dropdown["menu"].config(bg="#D0F0C0")

subject_level4 = tk.StringVar(root)
subject_level4.set(subject_levels[0]) # default value
subject_level4_dropdown = tk.OptionMenu(root, subject_level4, *subject_levels)
subject_level4_dropdown.place(x = 390, y = 410)
subject_level4_dropdown.config(bg="GREEN", fg="WHITE")
subject_level4_dropdown["menu"].config(bg="#D0F0C0")

subject_level5 = tk.StringVar(root)
subject_level5.set(subject_levels[0]) # default value
subject_level5_dropdown = tk.OptionMenu(root, subject_level5, *subject_levels)
subject_level5_dropdown.place(x = 390, y = 440)
subject_level5_dropdown.config(bg="GREEN", fg="WHITE")
subject_level5_dropdown["menu"].config(bg="#D0F0C0")

subject_level6 = tk.StringVar(root)
subject_level6.set(subject_levels[0]) # default value
subject_level6_dropdown = tk.OptionMenu(root, subject_level6, *subject_levels)
subject_level6_dropdown.place(x = 390, y = 470)
subject_level6_dropdown.config(bg="GREEN", fg="WHITE")
subject_level6_dropdown["menu"].config(bg="#D0F0C0")

subject_level7 = tk.StringVar(root)
subject_level7.set(subject_levels[0]) # default value
subject_level7_dropdown = tk.OptionMenu(root, subject_level7, *subject_levels)
subject_level7_dropdown.place(x = 390, y = 500)
subject_level7_dropdown.config(bg="GREEN", fg="WHITE")
subject_level7_dropdown["menu"].config(bg="#D0F0C0")

subjects = ["Social Studies", "Science", "Foreign Language", "Math", "English", "Elective", "Physical Education"]

subjects_label = tk.Label(text = "Subject")
subjects_label.place(x = 268, y = 290)

subject1 = tk.StringVar(root)
subject1.set(subjects[0]) # default value
subject1_dropdown = tk.OptionMenu(root, subject1, *subjects)
subject1_dropdown.place(x = 230, y = 320)
subject1_dropdown.config(bg="GREEN", fg="WHITE")
subject1_dropdown["menu"].config(bg="#D0F0C0")

subject2 = tk.StringVar(root)
subject2.set(subjects[1]) # default value
subject2_dropdown = tk.OptionMenu(root, subject2, *subjects)
subject2_dropdown.place(x = 230, y = 350)
subject2_dropdown.config(bg="GREEN", fg="WHITE")
subject2_dropdown["menu"].config(bg="#D0F0C0")

subject3 = tk.StringVar(root)
subject3.set(subjects[2]) # default value
subject3_dropdown = tk.OptionMenu(root, subject3, *subjects)
subject3_dropdown.place(x = 230, y = 380)
subject3_dropdown.config(bg="GREEN", fg="WHITE")
subject3_dropdown["menu"].config(bg="#D0F0C0")

subject4 = tk.StringVar(root)
subject4.set(subjects[3]) # default value
subject4_dropdown = tk.OptionMenu(root, subject4, *subjects)
subject4_dropdown.place(x = 230, y = 410)
subject4_dropdown.config(bg="GREEN", fg="WHITE")
subject4_dropdown["menu"].config(bg="#D0F0C0")

subject5 = tk.StringVar(root)
subject5.set(subjects[4]) # default value
subject5_dropdown = tk.OptionMenu(root, subject5, *subjects)
subject5_dropdown.place(x = 230, y = 440)
subject5_dropdown.config(bg="GREEN", fg="WHITE")
subject5_dropdown["menu"].config(bg="#D0F0C0")

subject6 = tk.StringVar(root)
subject6.set(subjects[5]) # default value
subject6_dropdown = tk.OptionMenu(root, subject6, *subjects)
subject6_dropdown.place(x = 230, y = 470)
subject6_dropdown.config(bg="GREEN", fg="WHITE")
subject6_dropdown["menu"].config(bg="#D0F0C0")

subject7 = tk.StringVar(root)
subject7.set(subjects[6]) # default value
subject7_dropdown = tk.OptionMenu(root, subject7, *subjects)
subject7_dropdown.place(x = 230, y = 500)
subject7_dropdown.config(bg="GREEN", fg="WHITE")
subject7_dropdown["menu"].config(bg="#D0F0C0")

gpa_info.set("No GPA calculated yet")
gpa_info_label = tk.Label(textvariable = gpa_info)
gpa_info_label.place(x = 280, y = 650)

tk.mainloop()