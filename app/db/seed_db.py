from app.db.session import SessionLocal
from app.models.problem import Problem

# Define your 20 problems
problems = [
    {
        "id": 1,
        "title": "A",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "examples": [{"input": "6\n2 7 11 15 3 6\n9", "output": "0 1"}],
        "difficulty": "Easy",
        "rating": 3,
    },
    {
        "id": 2,
        "title": "B",
        "description": "Implement binary search on a sorted array. Return the index of the target element, or -1 if not found.",
        "examples": [{"input": "5\n1 2 3 4 5\n3", "output": "2"}],
        "difficulty": "Normal",
        "rating": 4,
    },
    {
        "id": 3,
        "title": "C",
        "description": "Check whether a given string is a palindrome. Ignore non-alphanumeric characters and case.",
        "examples": [{"input": "A man, a plan, a canal: Panama", "output": "true"}],
        "difficulty": "Easy",
        "rating": 2,
    },
    {
        "id": 4,
        "title": "D",
        "description": "Given a collection of intervals, merge all overlapping intervals.",
        "examples": [{"input": "4\n1 3\n2 6\n8 10\n15 18", "output": "1 6\n8 10\n15 18"}],
        "difficulty": "Normal",
        "rating": 5,
    },
    {
        "id": 5,
        "title": "E",
        "description": "Given a string, find the length of the longest substring without repeating characters.",
        "examples": [{"input": "abcabcbb", "output": "3"}],
        "difficulty": "Normal",
        "rating": 4,
    },
    {
        "id": 6,
        "title": "F",
        "description": "Reverse a singly linked list.",
        "examples": [{"input": "5\n1 2 3 4 5", "output": "5 4 3 2 1"}],
        "difficulty": "Easy",
        "rating": 3,
    },
    {
        "id": 7,
        "title": "G",
        "description": "Given a string containing just the characters (), {}, [], determine if the input is valid.",
        "examples": [{"input": "()[]{}", "output": "true"}],
        "difficulty": "Easy",
        "rating": 2,
    },
    {
        "id": 8,
        "title": "H",
        "description": "Find the length of the shortest transformation sequence from beginWord to endWord, changing one letter at a time.",
        "examples": [{"input": "6\nhot\ndot\ndog\nlot\nlog\ncog\nhit\ncog", "output": "5"}],
        "difficulty": "Master",
        "rating": 5,
    },
    {
        "id": 9,
        "title": "I",
        "description": "Compute how much water can be trapped after raining given an elevation map.",
        "examples": [{"input": "12\n0 1 0 2 1 0 1 3 2 1 2 1", "output": "6"}],
        "difficulty": "Master",
        "rating": 5,
    },
    {
        "id": 10,
        "title": "J",
        "description": "You are climbing a staircase. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?",
        "examples": [{"input": "2", "output": "2"}],
        "difficulty": "Easy",
        "rating": 1,
    },
    {
        "id": 11,
        "title": "K",
        "description": "There are a total of numCourses courses. Check if you can finish all courses given their prerequisites.",
        "examples": [{"input": "2\n1 0", "output": "true"}],
        "difficulty": "Normal",
        "rating": 4,
    },
    {
        "id": 12,
        "title": "L",
        "description": "Implement a trie with insert, search, and startsWith methods.",
        "examples": [{"input": "insert apple\nsearch apple\nstartsWith app", "output": "true\ntrue"}],
        "difficulty": "Normal",
        "rating": 3,
    },
    {
        "id": 13,
        "title": "M",
        "description": "Find the contiguous subarray with the largest sum.",
        "examples": [{"input": "9\n-2 1 -3 4 -1 2 1 -5 4", "output": "6"}],
        "difficulty": "Easy",
        "rating": 3,
    },
    {
        "id": 14,
        "title": "N",
        "description": "Find the kth largest element in an unsorted array.",
        "examples": [{"input": "6\n3 2 1 5 6 4\n2", "output": "5"}],
        "difficulty": "Normal",
        "rating": 4,
    },
    {
        "id": 15,
        "title": "O",
        "description": "Find the median of two sorted arrays.",
        "examples": [{"input": "2\n1 3\n1\n2", "output": "2.0"}],
        "difficulty": "Master",
        "rating": 5,
    },
    {
        "id": 16,
        "title": "P",
        "description": "Write a program to solve a Sudoku puzzle by filling the empty cells.",
        "examples": [{"input": "9x9 sudoku board representation (use '.' for empty)", "output": "solved board"}],
        "difficulty": "Master",
        "rating": 5,
    },
    {
        "id": 17,
        "title": "Q",
        "description": "Design and implement a data structure for Least Recently Used (LRU) cache.",
        "examples": [{"input": "LRUCache 2\nput 1 1\nput 2 2\nget 1", "output": "1"}],
        "difficulty": "Master",
        "rating": 4,
    },
    {
        "id": 18,
        "title": "R",
        "description": "Given a 2D grid map of \"1\"s (land) and \"0\"s (water), count the number of islands.",
        "examples": [{"input": "4 4\n1 1 0 0\n1 1 0 0\n0 0 1 0\n0 0 0 1", "output": "3"}],
        "difficulty": "Normal",
        "rating": 4,
    },
    {
        "id": 19,
        "title": "S",
        "description": "Perform a flood fill on a 2D image starting from a given pixel.",
        "examples": [{"input": "3 3\n1 1 1\n1 1 0\n1 0 1\n1 1 2", "output": "2 2 2\n2 2 0\n2 0 1"}],
        "difficulty": "Easy",
        "rating": 2,
    },
    {
        "id": 20,
        "title": "T",
        "description": "Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.",
        "examples": [{"input": "horse\nros", "output": "3"}],
        "difficulty": "Master",
        "rating": 5,
    },
]
# Seed the database
def seed_problems():
    db = SessionLocal()
    try:
        for prob in problems:
            db.merge(Problem(**prob))  # Safe for re-run
        db.commit()
        print("✅ Seeded 20 problems!")
    except Exception as e:
        db.rollback()
        print("❌ Error seeding problems:", e)
    finally:
        db.close()

# Run seeding
if __name__ == "__main__":
    seed_problems()
