import os
import subprocess
from pathlib import Path

BASE_DIR = Path(r"C:\Users\thaku\.gemini\antigravity\scratch\bcs354-javascript-lab")
BASE_DIR.mkdir(parents=True, exist_ok=True)

STUDENT_NAME = "Amal Tomar"
ROLL_NO = "2510303070"
INSTITUTION = "INVERTIS UNIVERSITY, BAREILLY"
COURSE = "B.Tech CSE - Second Year | JavaScript Programming Lab (BCS354)"

def make_js_header(asg_num, asg_title, task_num=""):
    t_str = f" - Task {task_num}" if task_num else ""
    return f"""/*
  {INSTITUTION}
  {COURSE}
  Assignment {asg_num}: {asg_title}{t_str}
  Student Name: {STUDENT_NAME}
  Roll Number: {ROLL_NO}
*/\n\n"""

def make_html_header(asg_num, asg_title, task_num=""):
    t_str = f" - Task {task_num}" if task_num else ""
    return f"""<!--
  {INSTITUTION}
  {COURSE}
  Assignment {asg_num}: {asg_title}{t_str}
  Student Name: {STUDENT_NAME}
  Roll Number: {ROLL_NO}
-->\n"""

def run_node(js_file):
    res = subprocess.run(["node", js_file.name], cwd=str(js_file.parent), capture_output=True, text=True)
    out = (res.stdout or "") + (("\n" + res.stderr) if res.stderr else "")
    return out.strip()

# ==============================================================================
# ASSIGNMENT 1: Your First JavaScript Script
# ==============================================================================
def build_asg_01():
    d = BASE_DIR / "Assignment-01"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.html (page with script in body printing Hello from the script)
    t1_html = f"""{make_html_header(1, "Your First JavaScript Script", 1)}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>First JavaScript Script</title>
</head>
<body>
    <h1>JavaScript in Browser</h1>
    <p>Check browser console (F12) to see output.</p>
    <script>
        console.log("Hello from the script");
    </script>
</body>
</html>
"""
    (d / "task1.html").write_text(t1_html, encoding="utf-8")
    out_lines.append("--- Task 1 Output (Browser Console F12) ---")
    out_lines.append("Hello from the script\n")

    # Task 2: task2.js (const schoolName = "Sample College", let year = 2026)
    t2_js = f"""{make_js_header(1, "Your First JavaScript Script", 2)}const schoolName = "Sample College";
let year = 2026;

console.log(schoolName);
console.log(year);
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (typeof "hello", typeof 7, typeof true)
    t3_js = f"""{make_js_header(1, "Your First JavaScript Script", 3)}console.log(typeof "hello");
console.log(typeof 7);
console.log(typeof true);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 2: Operators, Type Conversion and a Calculator
# ==============================================================================
def build_asg_02():
    d = BASE_DIR / "Assignment-02"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (sum, difference, product, quotient of 17 and 5)
    t1_js = f"""{make_js_header(2, "Operators, Type Conversion and a Calculator", 1)}const a = 17;
const b = 5;

console.log(a + b); // Sum
console.log(a - b); // Difference
console.log(a * b); // Product
console.log(a / b); // Quotient
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (convert "12" to number + 5; convert 7 to text + "3")
    t2_js = f"""{make_js_header(2, "Operators, Type Conversion and a Calculator", 2)}// Convert text "12" to number and add 5
const num = Number("12") + 5;
console.log(num);

// Convert number 7 to text and join with "3"
const text = String(7) + "3";
console.log(text);
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (numbers 8 and 4, operator +, change to -)
    t3_js = f"""{make_js_header(2, "Operators, Type Conversion and a Calculator", 3)}function calculate(num1, num2, op) {{
    if (op === "+") {{
        console.log(num1 + num2);
    }} else if (op === "-") {{
        console.log(num1 - num2);
    }}
}}

let num1 = 8;
let num2 = 4;
let op = "+";
calculate(num1, num2, op);

op = "-";
calculate(num1, num2, op);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 3: Conditions and Loops
# ==============================================================================
def build_asg_03():
    d = BASE_DIR / "Assignment-03"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (marks 72: >= 75 Grade A, >= 60 Grade B, else Grade C)
    t1_js = f"""{make_js_header(3, "Conditions and Loops", 1)}let marks = 72;

if (marks >= 75) {{
    console.log("Grade A");
}} else if (marks >= 60) {{
    console.log("Grade B");
}} else {{
    console.log("Grade C");
}}
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (for loop 1 to 5)
    t2_js = f"""{make_js_header(3, "Conditions and Loops", 2)}for (let i = 1; i <= 5; i++) {{
    console.log(i);
}}
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (while loop add 1, 2, 3 until total > 20)
    t3_js = f"""{make_js_header(3, "Conditions and Loops", 3)}let total = 0;
let num = 1;

while (total <= 20) {{
    total += num;
    num++;
}}

console.log(total);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 4: Writing Functions
# ==============================================================================
def build_asg_04():
    d = BASE_DIR / "Assignment-04"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (function greet, greet("Asha"))
    t1_js = f"""{make_js_header(4, "Writing Functions", 1)}function greet(name) {{
    return "Hello, " + name;
}}

console.log(greet("Asha"));
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (arrow function square, square(6))
    t2_js = f"""{make_js_header(4, "Writing Functions", 2)}const square = (n) => n * n;

console.log(square(6));
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (function billWithTax(amount, taxRate = 0.18))
    t3_js = f"""{make_js_header(4, "Writing Functions", 3)}function billWithTax(amount, taxRate = 0.18) {{
    return amount + (amount * taxRate);
}}

console.log(billWithTax(100));
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 5: Arrays, Array Methods and Nested Arrays
# ==============================================================================
def build_asg_05():
    d = BASE_DIR / "Assignment-05"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (marks = [72, 85, 64, 90], print length and marks[0])
    t1_js = f"""{make_js_header(5, "Arrays, Array Methods and Nested Arrays", 1)}const marks = [72, 85, 64, 90];

console.log(marks.length);
console.log(marks[0]);
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (subjects forEach)
    t2_js = f"""{make_js_header(5, "Arrays, Array Methods and Nested Arrays", 2)}const subjects = ["Maths", "Science", "English"];

subjects.forEach(subject => {{
    console.log(subject);
}});
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (filter marks >= 60)
    t3_js = f"""{make_js_header(5, "Arrays, Array Methods and Nested Arrays", 3)}const marks = [72, 85, 45, 90];

const filteredMarks = marks.filter(mark => mark >= 60);
console.log(filteredMarks);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    # Task 4: task4.js (grid nested array row 2 col 3)
    t4_js = f"""{make_js_header(5, "Arrays, Array Methods and Nested Arrays", 4)}const grid = [
    [1, 2, 3],
    [4, 5, 6]
];

// Row 2, Column 3 (index 1, 2)
console.log(grid[1][2]);
"""
    (d / "task4.js").write_text(t4_js, encoding="utf-8")
    out_lines.append("--- Task 4 Output ($ node task4.js) ---")
    out_lines.append(run_node(d / "task4.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 6: JSON Text
# ==============================================================================
def build_asg_06():
    d = BASE_DIR / "Assignment-06"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (JSON.stringify Rohan object)
    t1_js = f"""{make_js_header(6, "JSON Text", 1)}const student = {{
    name: "Rohan",
    marks: [70, 80]
}};

const jsonText = JSON.stringify(student);
console.log(jsonText);
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (JSON.parse city & pin)
    t2_js = f"""{make_js_header(6, "JSON Text", 2)}const jsonStr = '{{"city":"Pune","pin":411001}}';

const obj = JSON.parse(jsonStr);
console.log(obj.city);
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (try-catch invalid JSON)
    t3_js = f"""{make_js_header(6, "JSON Text", 3)}const invalidJson = "{{name: Rohan}}";

try {{
    JSON.parse(invalidJson);
}} catch (error) {{
    console.log("Invalid JSON");
}}
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 7: Constructor Functions and Classes
# ==============================================================================
def build_asg_07():
    d = BASE_DIR / "Assignment-07"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (constructor Student, Asha 88)
    t1_js = f"""{make_js_header(7, "Constructor Functions and Classes", 1)}function Student(name, marks) {{
    this.name = name;
    this.marks = marks;
}}

const s1 = new Student("Asha", 88);
console.log(s1.name);
console.log(s1.marks);
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (class Book, summary)
    t2_js = f"""{make_js_header(7, "Constructor Functions and Classes", 2)}class Book {{
    constructor(title, pages) {{
        this.title = title;
        this.pages = pages;
    }}

    summary() {{
        return `${{this.title}} has ${{this.pages}} pages`;
    }}
}}

const book = new Book("Algorithms", 320);
console.log(book.summary());
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (Student.prototype.result)
    t3_js = f"""{make_js_header(7, "Constructor Functions and Classes", 3)}function Student(name, marks) {{
    this.name = name;
    this.marks = marks;
}}

Student.prototype.result = function() {{
    return this.marks >= 40 ? "Pass" : "Fail";
}};

const s2 = new Student("Asha", 88);
console.log(s2.result());
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 8: Inheritance, Methods and Composition
# ==============================================================================
def build_asg_08():
    d = BASE_DIR / "Assignment-08"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (Person and Teacher extends Person)
    t1_js = f"""{make_js_header(8, "Inheritance, Methods and Composition", 1)}class Person {{
    constructor(name) {{
        this.name = name;
    }}

    greet() {{
        return "Hi, I am " + this.name;
    }}
}}

class Teacher extends Person {{
    constructor(name, subject) {{
        super(name);
        this.subject = subject;
    }}
}}

const teacher = new Teacher("Anita", "Maths");
console.log(teacher.greet());
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (class Locker pin 1234, checkPin)
    t2_js = f"""{make_js_header(8, "Inheritance, Methods and Composition", 2)}class Locker {{
    constructor() {{
        this.pin = 1234;
    }}

    checkPin(number) {{
        return number === this.pin;
    }}
}}

const myLocker = new Locker();
console.log(myLocker.checkPin(1111));
console.log(myLocker.checkPin(1234));
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (class Engine, class Car composition)
    t3_js = f"""{make_js_header(8, "Inheritance, Methods and Composition", 3)}class Engine {{
    constructor(power) {{
        this.power = power;
    }}
}}

class Car {{
    constructor(power) {{
        this.engine = new Engine(power);
    }}

    start() {{
        return `Car starts with ${{this.engine.power}} HP`;
    }}
}}

const car = new Car(150);
console.log(car.start());
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 9: DOM, Validation, Storage and Quiz
# ==============================================================================
def build_asg_09():
    d = BASE_DIR / "Assignment-09"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.html (Click button to change heading Welcome -> Button clicked)
    t1_html = f"""{make_html_header(9, "DOM, Validation, Storage and Quiz", 1)}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DOM Click Event</title>
</head>
<body>
    <h1 id="heading">Welcome</h1>
    <button id="btn">Change text</button>

    <script>
        document.getElementById("btn").addEventListener("click", function() {{
            document.getElementById("heading").textContent = "Button clicked";
        }});
    </script>
</body>
</html>
"""
    (d / "task1.html").write_text(t1_html, encoding="utf-8")
    out_lines.append("--- Task 1 (task1.html) ---")
    out_lines.append("Interactive page: Clicking 'Change text' updates heading from 'Welcome' to 'Button clicked'.\n")

    # Task 2: task2.js (validateForm(name))
    t2_js = f"""{make_js_header(9, "DOM, Validation, Storage and Quiz", 2)}function validateForm(name) {{
    const errors = [];
    if (!name || name.trim() === "") {{
        errors.push("Name is required");
    }}
    return errors;
}}

console.log(validateForm("Asha"));
console.log(validateForm(""));
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.html (localStorage note)
    t3_html = f"""{make_html_header(9, "DOM, Validation, Storage and Quiz", 3)}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>LocalStorage Note</title>
</head>
<body>
    <h1>Persistent Note</h1>
    <input type="text" id="noteInput" placeholder="Enter note">
    <button id="saveBtn">Save</button>

    <script>
        const input = document.getElementById("noteInput");
        const saveBtn = document.getElementById("saveBtn");

        // Load saved text on page open
        const savedNote = localStorage.getItem("note");
        if (savedNote !== null) {{
            input.value = savedNote;
        }}

        // Save on click
        saveBtn.addEventListener("click", function() {{
            localStorage.setItem("note", input.value);
            alert("Note saved successfully!");
        }});
    </script>
</body>
</html>
"""
    (d / "task3.html").write_text(t3_html, encoding="utf-8")
    out_lines.append("--- Task 3 (task3.html) ---")
    out_lines.append("Stores input text into localStorage under key 'note' and retrieves it upon reload.\n")

    # Task 4: task4.html (Quiz 2 + 3)
    t4_html = f"""{make_html_header(9, "DOM, Validation, Storage and Quiz", 4)}<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Math Quiz</title>
</head>
<body>
    <h2>What is 2 + 3?</h2>
    <form id="quizForm">
        <label><input type="radio" name="answer" value="4"> 4</label><br>
        <label><input type="radio" name="answer" value="5"> 5</label><br>
        <label><input type="radio" name="answer" value="6"> 6</label><br><br>
        <button type="button" id="checkBtn">Check answer</button>
    </form>
    <p id="resultMsg" style="font-weight: bold; margin-top: 10px;"></p>

    <script>
        document.getElementById("checkBtn").addEventListener("click", function() {{
            const selected = document.querySelector('input[name="answer"]:checked');
            const msg = document.getElementById("resultMsg");
            if (selected && selected.value === "5") {{
                msg.textContent = "Correct";
                msg.style.color = "green";
            }} else {{
                msg.textContent = "Try again";
                msg.style.color = "red";
            }}
        }});
    </script>
</body>
</html>
"""
    (d / "task4.html").write_text(t4_html, encoding="utf-8")
    out_lines.append("--- Task 4 (task4.html) ---")
    out_lines.append("Quiz: Selecting 5 shows 'Correct', otherwise shows 'Try again'.\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 10: Objects and Destructuring
# ==============================================================================
def build_asg_10():
    d = BASE_DIR / "Assignment-10"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (object student, modify marks)
    t1_js = f"""{make_js_header(10, "Objects and Destructuring", 1)}const student = {{
    name: "Rohan",
    roll: 12,
    marks: 78
}};

console.log(student.name);
student.marks = 81;
console.log(student.marks);
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (array destructuring)
    t2_js = f"""{make_js_header(10, "Objects and Destructuring", 2)}const subjects = ["Maths", "Science", "English"];

const [first, second] = subjects;
console.log(first);
console.log(second);
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (object destructuring)
    t3_js = f"""{make_js_header(10, "Objects and Destructuring", 3)}const student = {{
    name: "Rohan",
    roll: 12,
    marks: 81
}};

const {{ name, roll }} = student;
console.log(name);
console.log(roll);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 11: Scope and Closures
# ==============================================================================
def build_asg_11():
    d = BASE_DIR / "Assignment-11"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (block scope level)
    t1_js = f"""{make_js_header(11, "Scope and Closures", 1)}let level = "outer";

{{
    let level = "inner";
    console.log(level);
}}

console.log(level);
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (closure makeCounter)
    t2_js = f"""{make_js_header(11, "Scope and Closures", 2)}function makeCounter() {{
    let count = 0;
    return function() {{
        count += 1;
        return count;
    }};
}}

const counter = makeCounter();
console.log(counter());
console.log(counter());
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (global school, showSchool)
    t3_js = f"""{make_js_header(11, "Scope and Closures", 3)}let school = "Sample College";

function showSchool() {{
    console.log("Welcome to " + school);
}}

showSchool();
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 12: Callbacks and Higher-Order Functions
# ==============================================================================
def build_asg_012():
    d = BASE_DIR / "Assignment-12"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (applyTwice, addTen)
    t1_js = f"""{make_js_header(12, "Callbacks and Higher-Order Functions", 1)}function applyTwice(fn, value) {{
    return fn(fn(value));
}}

function addTen(num) {{
    return num + 10;
}}

console.log(applyTwice(addTen, 5));
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (formatMarks)
    t2_js = f"""{make_js_header(12, "Callbacks and Higher-Order Functions", 2)}function formatMarks(marks, callback) {{
    return callback(marks);
}}

console.log(formatMarks(76, (marks) => `Marks: ${{marks}}/100`));
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (repeatAction)
    t3_js = f"""{make_js_header(12, "Callbacks and Higher-Order Functions", 3)}function repeatAction(times, action) {{
    for (let i = 1; i <= times; i++) {{
        action(i);
    }}
}}

repeatAction(3, (round) => {{
    console.log("Round " + round);
}});
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 13: Reduce, Some, Every and Map
# ==============================================================================
def build_asg_013():
    d = BASE_DIR / "Assignment-13"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (reduce total prices)
    t1_js = f"""{make_js_header(13, "Reduce, Some, Every and Map", 1)}const prices = [120, 45, 300];

const total = prices.reduce((acc, curr) => acc + curr, 0);
console.log(total);
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (some and every)
    t2_js = f"""{make_js_header(13, "Reduce, Some, Every and Map", 2)}const marks = [72, 85, 30, 90];

const anyBelow40 = marks.some(mark => mark < 40);
console.log(anyBelow40);

const allAtLeast35 = marks.every(mark => mark >= 35);
console.log(allAtLeast35);
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (map + original unchanged)
    t3_js = f"""{make_js_header(13, "Reduce, Some, Every and Map", 3)}const marks = [72, 85, 64, 90];

const increasedMarks = marks.map(mark => mark + 5);
console.log(increasedMarks);
console.log(marks);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 14: Timers and Intervals
# ==============================================================================
def build_asg_014():
    d = BASE_DIR / "Assignment-14"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (setTimeout 0 order)
    t1_js = f"""{make_js_header(14, "Timers and Intervals", 1)}console.log("Start");

setTimeout(() => {{
    console.log("Timer done");
}}, 0);

console.log("End");
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (clearTimeout)
    t2_js = f"""{make_js_header(14, "Timers and Intervals", 2)}const timerId = setTimeout(() => {{
    console.log("Not shown");
}}, 1000);

clearTimeout(timerId);
console.log("Cancelled");
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (setInterval stopped at 3)
    t3_js = f"""{make_js_header(14, "Timers and Intervals", 3)}let count = 1;

const intervalId = setInterval(() => {{
    console.log("Tick " + count);
    if (count === 3) {{
        clearInterval(intervalId);
    }}
    count++;
}}, 200);
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    # Run with timeout to be safe
    res = subprocess.run(["node", str(d / "task3.js")], capture_output=True, text=True, timeout=5)
    out_lines.append(res.stdout.strip() + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

# ==============================================================================
# ASSIGNMENT 15: Promises and async/await with Local Data
# ==============================================================================
def build_asg_015():
    d = BASE_DIR / "Assignment-15"
    d.mkdir(parents=True, exist_ok=True)
    out_lines = []

    # Task 1: task1.js (checkMarks resolve 80)
    t1_js = f"""{make_js_header(15, "Promises and async/await with Local Data", 1)}function checkMarks(marks) {{
    return new Promise((resolve, reject) => {{
        if (marks >= 0 && marks <= 100) {{
            resolve(marks);
        }} else {{
            reject(new Error("Marks out of range"));
        }}
    }});
}}

checkMarks(80)
    .then(value => console.log(value))
    .catch(err => console.log(err.message));
"""
    (d / "task1.js").write_text(t1_js, encoding="utf-8")
    out_lines.append("--- Task 1 Output ($ node task1.js) ---")
    out_lines.append(run_node(d / "task1.js") + "\n")

    # Task 2: task2.js (checkMarks reject 120)
    t2_js = f"""{make_js_header(15, "Promises and async/await with Local Data", 2)}function checkMarks(marks) {{
    return new Promise((resolve, reject) => {{
        if (marks >= 0 && marks <= 100) {{
            resolve(marks);
        }} else {{
            reject(new Error("Marks out of range"));
        }}
    }});
}}

checkMarks(120)
    .then(value => console.log(value))
    .catch(err => console.log(err.message));
"""
    (d / "task2.js").write_text(t2_js, encoding="utf-8")
    out_lines.append("--- Task 2 Output ($ node task2.js) ---")
    out_lines.append(run_node(d / "task2.js") + "\n")

    # Task 3: task3.js (async run with try-catch 65 & -5)
    t3_js = f"""{make_js_header(15, "Promises and async/await with Local Data", 3)}function checkMarks(marks) {{
    return new Promise((resolve, reject) => {{
        if (marks >= 0 && marks <= 100) {{
            resolve(marks);
        }} else {{
            reject(new Error("Marks out of range"));
        }}
    }});
}}

async function run() {{
    try {{
        const m1 = await checkMarks(65);
        console.log(m1);
        const m2 = await checkMarks(-5);
        console.log(m2);
    }} catch (error) {{
        console.log("Caught: " + error.message);
    }}
}}

run();
"""
    (d / "task3.js").write_text(t3_js, encoding="utf-8")
    out_lines.append("--- Task 3 Output ($ node task3.js) ---")
    out_lines.append(run_node(d / "task3.js") + "\n")

    # Task 4: task4.js (getUsers Promise 100ms Asha, Rohan, Meera)
    t4_js = f"""{make_js_header(15, "Promises and async/await with Local Data", 4)}function getUsers() {{
    return new Promise((resolve) => {{
        setTimeout(() => {{
            const users = [
                {{ id: 1, name: "Asha" }},
                {{ id: 2, name: "Rohan" }},
                {{ id: 3, name: "Meera" }}
            ];
            resolve(users);
        }}, 100);
    }});
}}

async function displayUsers() {{
    const users = await getUsers();
    users.forEach(user => {{
        console.log(user.name);
    }});
}}

displayUsers();
"""
    (d / "task4.js").write_text(t4_js, encoding="utf-8")
    out_lines.append("--- Task 4 Output ($ node task4.js) ---")
    res = subprocess.run(["node", str(d / "task4.js")], capture_output=True, text=True, timeout=5)
    out_lines.append(res.stdout.strip() + "\n")

    (d / "output.txt").write_text("\n".join(out_lines), encoding="utf-8")

def main():
    print(f"Building JavaScript Programming Lab (BCS354) for {STUDENT_NAME} ({ROLL_NO})...")
    build_asg_01()
    build_asg_02()
    build_asg_03()
    build_asg_04()
    build_asg_05()
    build_asg_06()
    build_asg_07()
    build_asg_08()
    build_asg_09()
    build_asg_10()
    build_asg_11()
    build_asg_012()
    build_asg_013()
    build_asg_014()
    build_asg_015()
    print("All 15 JavaScript assignments built and executed successfully!")

if __name__ == "__main__":
    main()
