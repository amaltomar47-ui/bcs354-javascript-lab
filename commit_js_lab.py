import subprocess
from pathlib import Path

LAB_DIR = Path(r"C:\Users\thaku\.gemini\antigravity\scratch\bcs354-javascript-lab")

def run(cmd):
    res = subprocess.run(cmd, cwd=str(LAB_DIR), shell=True, capture_output=True, text=True)
    out = (res.stdout or "") + ("\n" + res.stderr if res.stderr else "")
    return out.strip()

print("Initializing Git repository for JavaScript lab...")
run("git init")
run('git config user.name "Amal Tomar"')
run('git config user.email "amaltomar47@gmail.com"')
run("git branch -M main")

assignments = [
    ("Assignment-01", "Assignment 01: Your First JavaScript Script"),
    ("Assignment-02", "Assignment 02: Operators, Type Conversion and a Calculator"),
    ("Assignment-03", "Assignment 03: Conditions and Loops"),
    ("Assignment-04", "Assignment 04: Writing Functions"),
    ("Assignment-05", "Assignment 05: Arrays, Array Methods and Nested Arrays"),
    ("Assignment-06", "Assignment 06: JSON Text"),
    ("Assignment-07", "Assignment 07: Constructor Functions and Classes"),
    ("Assignment-08", "Assignment 08: Inheritance, Methods and Composition"),
    ("Assignment-09", "Assignment 09: DOM, Validation, Storage and Quiz"),
    ("Assignment-10", "Assignment 10: Objects and Destructuring"),
    ("Assignment-11", "Assignment 11: Scope and Closures"),
    ("Assignment-12", "Assignment 12: Callbacks and Higher-Order Functions"),
    ("Assignment-13", "Assignment 13: Reduce, Some, Every and Map"),
    ("Assignment-14", "Assignment 14: Timers and Intervals"),
    ("Assignment-15", "Assignment 15: Promises and async/await with Local Data"),
]

for folder, msg in assignments:
    run(f"git add {folder}")
    run(f'git commit -m "{msg}"')
    print(f"Committed {folder}")

run("git add index.html README.md package.json")
run('git commit -m "Add Lab Portal, package.json and Documentation"')
print("Committed Documentation")

log_out = run("git log --oneline")
print("\nCommit History:\n" + log_out)
