## Day 1 - 2026-09-02
- [x] Set up Python + VS Code
- [x] Created GitHub repo and fixed Git issues
- [x] Wrote hello.py and day1_test.py
- [x] Learned: git init, add, commit, push, basic Bash navigation

Time spent: ~2–3 hours

What I learned:
- Git basics and workflow (init, add, commit, push, remote, branch)
- Basic Python I/O and simple calculations
- How to resolve a merge issue when local and remote histories differ

What felt hard:
- Git Bash paths
- Understanding the merge process (had to ask multiple times)

Tomorrow’s focus:
- if-else conditions
- for loops
- 4–5 small practice problems in day2_practice.py

THE DAY 1 ENDS HERE ---------------------------

## Day 2 - 2026-09-03
- [x] Learned if-else and for loops
- [x] Solved 4–5 practice problems in day2_practice.py
- [x] Pushed code to GitHub

Time spent: ~2 hours

What I learned:
- if, elif, else conditions
- for loops with range
- Using % operator for divisibility

What felt hard:
- nothing was hard today eveything felt easy

Tomorrow’s focus:
- while loops
- pattern printing (stars/numbers)
- mini-project: number guessing game

## Day 3 - 2026-09-07
- [x] Learned while loops
- [x] Practiced printing numbers and calculating sums with while loops
- [x] Learned why loop-control variables must be updated
- [x] Practiced a password-checking program with limited attempts
- [x] Learned the basic use of break to exit a loop early
- [x] Completed the Day 3 quiz

Time spent: ~2 hours

What I learned:
- A while loop runs as long as its condition is true
- Multiple statements can be written inside a while loop using the same indentation
- A loop variable must change so the loop can eventually stop
- break immediately exits the current loop
- Conditions can be combined using and

What felt hard:
- Keeping track of attempt counts
- Deciding which code should be inside or outside a while loop

Tomorrow’s focus:
- Python lists
- List indexing and len()
- append() and for loops with lists
- A mini-project: marks analyzer

## Day 4 – Lists and Marks Analyzer (Python)

**Date:** 07-09-2026  
**Time spent:** ~2 hours  
**Resources used:**
- Python basics notes
- VS Code
- GitHub

### Topics covered
- Python lists:
  - Creating lists
  - Indexing (`list[0]`, `list[-1]`)
  - `len(list)`
  - `list.append()`
- `for` loops with lists:
  - Iterating over elements
  - Accumulating totals
  - Counting items that satisfy a condition
- Using `max()` and `min()` on lists

### Tasks completed
- Created `day4_lists.py` with:
  - Basic list examples (languages, skills, colleges)
  - Task: add a skill using `append()`
  - Task: loop through a list of colleges
  - Task: calculate total and average marks using a loop
- Created `marks_analyzer.py` that:
  - Prints each mark
  - Calculates total marks
  - Calculates average marks
  - Finds highest and lowest marks
  - Counts how many marks are ≥ 75

### Key learnings
- Lists store multiple values in one variable.
- Indexing starts at `0`; negative indexes count from the end.
- `append()` adds an item at the end of the list.
- `for` loops can:
  - Print all items
  - Compute totals
  - Count items based on a condition
- Git workflow practiced again:
  - `git add .`
  - `git commit -m "Day 4: lists and marks analyzer"`
  - `git push`

### Challenges
- Initially confused how to count marks ≥ 75 (used index instead of a separate counter).
- Fixed by introducing `count_75_or_more` and updating it only when `mark >= 75`.

### Next steps (Day 5 plan)
- Learn `if-elif-else` in more depth.
- Practice more problems combining lists + conditions.
- Start simple mini-projects (e.g., grade calculator, number filter).