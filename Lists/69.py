# Q8. Accepts a list of 10 student exam scores. Finds the maximum score and minimum score using a loop and standard comparison operators without using max() or min(). Returns both values.
def find_extremes(scores):
    max_score = scores[0]
    min_score = scores[0]
    for s in scores:
        if s > max_score:
            max_score = s
        if s < min_score:
            min_score = s
    return max_score, min_score

marks = [45, 89, 32, 78, 90, 23, 67, 88, 54, 99]
print("Max and Min:", find_extremes(marks))