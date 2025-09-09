# EXERCISE 1
def ways(n):
    """
    Return the number of ways to make change for n cents using only pennies (1¢) and nickels (5¢), with yield.
    """
    def gen():
        for nick in range(n // 5 + 1):
            yield 1
    return sum(gen())


# Test cases
print("ways(12) =", ways(12))  # 3 ways -> (12,0), (7,1), (2,2)
print("ways(20) =", ways(20))  # 5 ways -> (20,0), (15,1), (10,2), (5,3), (0,4)
print("ways(3)  =", ways(3))   # 1 way  -> (3,0)
print("ways(0)  =", ways(0))   # 1 way  -> (0,0)

# EXERCISE 2
import numpy as np

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])


def lowest_score(names, scores):
    """
    Return the name and score of the student with the lowest score.
    """
    idx = np.argmin(scores)
    return names[idx]

print("Student with the lowest score:", lowest_score(names, scores))


import numpy as np

names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
scores = np.array([99, 71, 85, 62, 91])

def sort_names(names, scores):
    """
    Return names and scores sorted in descending order of scores.
    """
    # Get the indices that would sort scores descending
    idx = np.argsort(scores)[::-1]
    
    # Use integer indexing on both arrays
    sorted_names = names[idx]
    sorted_scores = scores[idx]
    
    return sorted_names, sorted_scores

# Use the function
sorted_names, sorted_scores = sort_names(names, scores)

print("Students and their scores in descending order:")
for name, score in zip(sorted_names, sorted_scores):
    print(f"{name}: {score}")
