# 🏅 Question: Find the Runner-Up Score:-
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the second highest (i.e., runner-up) score.
# 
# 📥 Input Format:-
# The first line contains an integer n, the number of participants.
# The second line contains n space-separated integers — the scores of each participant.
# 
# 🔒 Constraints:-
# 2 ≤ n ≤ 100
# -100 ≤ score ≤ 100
# 
# 📤 Output Format:-
# Print the runner-up score (second highest score) on a single line.
# 
# ✨ Sample Input:-
# 5
# 2 3 6 6 5
# 
# ✅ Sample Output:-
# 5




n = int(input())  # Number of scores


scores = list(map(int, input().split()))  # Read scores as integers

# Remove duplicates and sort the scores in descending order
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

# The second item is the runner-up score
print(unique_scores[1])
