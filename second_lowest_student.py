# ### 📘 **Question: Students with the Second Lowest score**
#
# You are given the names and scores for each student in a class. Store them in a nested list and **print the name(s) of any student(s) having the second lowest score**.
#
# If multiple students have the same second lowest score, **sort their names alphabetically** and print each one on a new line.
#
# ---
#
# ### 📥 Input Format:
#
# * The **first line** contains an integer `n`, the number of students.
# * The **next 2×n lines** describe each student:
#
#   * A student's **name** (string).
#   * A student's **score** (float).
#
# ---
#
# ### 🔒 Constraints:
#
# * There will always be **at least one** student with the second lowest score.
#
# ---
#
# ### 📤 Output Format:
#
# Print the name(s) of student(s) having the second lowest score. If more than one student qualifies, sort their names alphabetically. Print each name on a **new line**.
#
# ---
#
# ### ✨ Sample Input:
#
# ```
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# ```
#
# ### ✅ Sample Output:
#
# ```
# Berry
# Harry
# ```


### ✅ Python Solution:

students = []

n = int(input())
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

# Extract all unique scores and sort them
scores = sorted(set([score for name, score in students]))

# Get all students with the second lowest score
second_lowest_students = [name for name, score in students if score == scores[1]]

# Sort names alphabetically and print
print("\n Names with Second Lowest Scores are:")
for name in sorted(second_lowest_students):
    print(name)
