import matplotlib.pyplot as plt
import os


fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.


def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum


def average(list):
    return sum(list) / len(list)

def weighted_grade(grade_list, weight_list):
    weighted_grade_sum = 0
    weight_sum = 0
    for i in range(len(grade_list)):
        weighted_grade_sum += grade_list[i] * weight_list[i]
        weight_sum += weight_list[i]
    return weighted_grade_sum/weight_sum


def min_in_list(list):
    least = 0
    for num in list:
        if num < least:
            least = num
    return least


def max_in_list(list):
    most = 0
    for num in list:
        if num < most:
            most = num
    return most


def student_exists(name_or_id):
    if isinstance(name_or_id, str) and name_or_id in student_ids:
        return True
    elif isinstance(name_or_id, int) and name_or_id in student_names:
        return True
    return False


def assignment_exists(assignment_name):
    if isinstance(assignment_name, str) and assignment_name in assignment_ids:
        return True
    return False


def get_scores(assignment):
    grades = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r") as file:
                content = file.read()
                content = content.split('|')
                if content[1] == assignment_ids[assignment]:
                    grades.append(int(content[2]))
    return grades

folder_path = 'data/submissions'

# Make dictionaries of student IDs and names
student_names = {}
student_ids = {}
student_data = open("data/students.txt", "r")
for line in student_data:
    student_names[int(line[:3])] = line[3:-2]
    student_ids[line[3:-1]] = line[:3]

# Make dictionaries of assignment IDs and weights
assignment_ids = {}
assignment_names = {}
assignment_weights = {}
assignment_data = open("data/assignments.txt", "r")
i = 0
for line in assignment_data:
    if i % 3 == 0:
        assignment_name = line[:-1]
    elif i % 3 == 1:
        assignment_id = line[:-1]
    elif i % 3 == 2:
        assignment_weight = int(line[:-1])
        assignment_weights[assignment_id] = assignment_weight
        assignment_ids[assignment_name] = assignment_id
        assignment_names[assignment_id] = assignment_name
    i += 1
    


while True:
    print('1. Student grade')
    print('2. Assignment statistics')
    print('3. Assignment graph\n')

    option = input('Enter your selection: ')

    match (option):
        case '1':
            name = input('What is the student\'s name: ')
            if not student_exists(name):
                print("Student not found")
                break

            grades = []
            weights = []
            for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
                if os.path.isfile(filepath):
                    with open(filepath, "r") as file:
                        content = file.read()
                        content = content.split('|')
                        if content[0] == student_ids[name]:
                            grades.append(int(content[2]))
                            weights.append(assignment_weights[content[1]])

            # Get students overall grade
            print(str(weighted_grade(grades, weights)) + '%')

        case '2':
            assignment = input('What is the assignment: ')
            if not assignment_exists(assignment):
                print("Assignment not found")
                break

            grades = get_scores(assignment)

            print("min: " + str(min(grades)) + "%")
            print("avg: " + str(average(grades)) + "%")
            print("max: " + str(max(grades)) + "%")

        case '3':
            assignment = input('What is the assignment: ')
            scores = get_scores(assignment)
            plt.hist(scores, bins=[0,25,50,75,100])
            plt.show()

        case _:
            print('Invalid input!')
            break

