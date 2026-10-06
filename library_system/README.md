# Library Resource Management System

Coursework: Fundamentals of Data Science (UFCFK1-15-0) - Portfolio

## Requirements
- Python 3.8+
- `matplotlib` (for the bonus analytics feature): `pip install matplotlib`

## Running the program
```bash
cd library_system
python3 main.py
```

## Sample login credentials (seeded in data/passwords.txt)
| Username | Password  | Role      | Member ID |
|----------|-----------|-----------|-----------|
| krimal   | admin123  | Librarian | M001      |
| alice    | pass123   | Student   | M002      |
| brian    | pass123   | Student   | M003      |
| chloe    | pass123   | Student   | M004      |
| david    | pass123   | Student   | M005      |

## Project structure
```
library_system/
├── main.py              # CLI entry point / menus
├── auth.py               # Login logic
├── book.py                # Book class
├── member.py              # User base class + Librarian/Student subclasses
├── exceptions.py           # Custom exception hierarchy
├── storage[books.txt](../../../Desktop/FODS%20PROJECT/books.txt).py              # All file I/O (the only module that touches data/)
├── librarian_ops.py        # Admin-only operations
├── student_ops.py          # Student operations + shared borrow/return logic
├── analytics.py             # Bonus: Borrowing Analytics (Matplotlib)
├── data/
│   ├── books.txt
│   ├── members.txt
│   ├── loans.txt
│   └── passwords.txt
├── sample_io_demo.txt        # Captured sample input/output log
├── architecture_diagram.png   # System architecture flowchart
├── login_flowchart.png         # Login / role-based access flowchart
├── genre_popularity.png         # Bonus analytics chart
├── borrowing_trend.png           # Bonus analytics chart
├── sample_output_terminal.png     # Styled excerpt of console output
└── Library_System_Report.docx      # Full written report
