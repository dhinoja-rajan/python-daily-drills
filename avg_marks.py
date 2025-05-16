# 📘 Question: Finding the Student's Average Marks
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# 
# You need to print the average of the marks array for the student name provided, showing 2 decimal places.
# 
# 📥 Input Format
# The first line contains the integer n, the number of students' records.
# 
# The next n lines each contain:
# 
# A student's name, followed by
# 
# Three space-separated marks (floats or integers).
# 
# The final line contains query_name, the name of a student to query.
# 
# 🔒 Constraints
# 2 <= n <= 10
# 
# 0 <= marks <= 100
# 
# 📤 Output Format
# Print one line: the average of the marks obtained by the queried student, correct to 2 decimal places.


# Read the number of students
n = int(input())

# Initialize dictionary to store student records
student_marks = {}

# Read each student record
for i in range(n):
    print(f"Enter details for student {i + 1}: ")
    line = input().split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

# Read the name to query
query_name = input()

# Calculate average
avg = sum(student_marks[query_name]) / len(student_marks[query_name])

if avg == student_marks[1]:
    print(name)
    
