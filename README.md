# College Attendance Analyzer

## 1. Project Overview

The **College Attendance Analyzer** is a Python-based data analysis project that processes student attendance records from a CSV file.

It validates raw records, calculates subject-wise and overall student attendance percentages, flags students below the required 75% eligibility threshold, computes subject-wise averages, and generates visual reports using charts.

The project uses Python libraries like Pandas and Matplotlib to automate attendance tracking and make analysis faster and error-free.

## 2. Features

- **Data Validation:** Identifies and skips invalid records (zero/negative classes held, negative attendance, or attendance exceeding classes held) before calculations run.
- **Attendance Percentage:** Calculates the attendance percentage of each student in each subject.
- **Shortage List:** Identifies student-subject records where attendance falls below 75%.
- **Subject-wise Average:** Calculates the mean attendance percentage for each subject.
- **Student-wise Summary:** Aggregates total classes held, total classes attended, and overall percentage per student across all valid subjects.
- **Bar Chart:** Displays subject-wise average attendance graphically.
- **Pie Chart:** Shows the overall distribution of eligible (≥ 75%) and shortage (< 75%) records.
- **Interactive Menu:** Allows users to select different reports through a simple command-line menu.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Pandas | Reading, validating, and analyzing CSV data |
| Matplotlib | Creating bar and pie charts |
| CSV | Storing raw attendance records |
| VS Code | Code editor |

## 4. Project Structure

```text
CollegeAttendanceAnalyzer/
│
├── codebase/
│   ├── attendance_data.csv
│   └── attendance_analyzer.py
└── README.md
```

### File Description

- `codebase/attendance_data.csv` – Contains student names, subjects, classes held, and classes attended.
- `codebase/attendance_analyzer.py` – Contains the Python code for validation, analysis, and visualization.
- `README.md` – Provides documentation and instructions for running the project.

## 5. Installation and Setup

### Step 1: Install Python

Download and install Python 3 from:

https://python.org

### Step 2: Install Required Libraries

Open the terminal in VS Code and execute:

```bash
python -m pip install pandas matplotlib
```

### Step 3: Open the Project

Open the `CollegeAttendanceAnalyzer` folder in VS Code.

Make sure that both `attendance_data.csv` and `attendance_analyzer.py` are present inside the `code/` folder.

## 6. How to Run the Project

Open the VS Code terminal, navigate into the `code` directory, and execute the script:

```bash
cd codebase
python attendance_analyzer.py
```

The program will validate the CSV records on startup and display an interactive menu.

## 7. Menu Options

The program provides the following options:

| Option | Function |
|---|---|
| 1 | Display subject-wise attendance percentages |
| 2 | Display the shortage list (below 75%) |
| 3 | Display subject-wise average and charts (bar & pie) |
| 4 | Display student-wise cumulative attendance summary |
| 5 | Exit the program |

### Attendance Calculation

The attendance percentage is calculated using the formula:

**Attendance Percentage = (Classes Attended / Classes Held) × 100**

### Attendance Criteria

- **75% or above:** Eligible
- **Below 75%:** Shortage

## 8. Data Validation

The program checks every row in `code/attendance_data.csv` before performing calculations.

A record is skipped if any of the following conditions occur:

- Classes held are zero or negative (`Classes_Held <= 0`).
- Classes attended are negative (`Classes_Attended < 0`).
- Classes attended exceed classes held (`Classes_Attended > Classes_Held`).

Invalid records are reported in the console and excluded so they do not distort averages or percentages.

## 9. Sample Dataset

The project uses `codebase/attendance_data.csv`, containing **40 student-subject records** (10 students across 4 subjects: Python, Maths, DBMS, and CN). Out of these 40 records, **31 are valid** and **9 are invalid** entries designed to test data validation.

Example:

| Name | Subject | Classes_Held | Classes_Attended |
|---|---|---:|---:|
| Aarav | Python | 40 | 36 |
| Priya | Python | 40 | 28 |
| Rahul | Python | 40 | 30 |
| Sneha | Maths | 50 | 50 |

The dataset covers regular attendance, shortage cases, 100% attendance, 0% attendance, and invalid rows.

## 10. Expected Output

The project generates:

1. A startup validation summary showing total, valid, and skipped records.
2. A table displaying subject-wise student attendance percentages.
3. A shortage list of student-subject records below 75%.
4. Subject-wise average attendance percentages.
5. A bar chart of subject-wise averages and a pie chart of eligible vs. shortage records.
6. A student-wise summary table showing total classes held, total attended, and overall percentage per student.

## 11. Conclusion

The College Attendance Analyzer demonstrates how Python can automate attendance tracking and student eligibility checks.

Using Pandas and Matplotlib, it cleans raw CSV data, detects attendance shortages, summarizes student performance across courses, and turns tabular records into clear visual reports.

---

**Project Name:** College Attendance Analyzer  
**Language:** Python 3  
**Libraries:** Pandas, Matplotlib  
**Data Format:** CSV