

---

### 📄 README.md

```markdown
# Flask Exam Result Checker

A simple Flask-based web application that allows users to check exam results by providing a course name and matriculation number. This project uses **CSV files** as the data source, making it lightweight and easy to set up without requiring a database.

---

## 🚀 Overview

This app serves a single endpoint `/examresult` where students can input their **matriculation number** and **course name** via URL query parameters to retrieve their exam result and a remark based on the score.

- Fetches student name from `studentsregister.csv`
- Fetches exam score from `examscores.csv`
- Returns a formatted result message with a promotion remark if score > 50

---

## 🧾 Example Request

```
http://<your-server>/examresult?course=maths&matricno=1001
```

### ✅ Expected Response:

```
The result in maths for John Doe (1001) is 78. The student is promoted
```

---

## 🗂️ Required CSV Files

Make sure the following CSV files exist in the root directory of the app:

### `studentsregister.csv`

| name         | matricno |
|--------------|----------|
| John Doe     | 1001     |
| Jane Smith   | 1002     |

### `examscores.csv`

| matricno | course | score |
|----------|--------|-------|
| 1001     | maths  | 78    |
| 1001     | eng    | 65    |
| 1002     | maths  | 49    |

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas (for CSV handling)
- Socket (to fetch hostname and IP)

---

## 📦 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/flask-exam-result-checker.git
   ```

2. Navigate into the directory:

   ```bash
   cd flask-exam-result-checker
   ```

3. Install dependencies:

   ```bash
   pip install flask pandas
   ```

4. Run the app:

   ```bash
   python app.py
   ```

5. Access the app at:  
   `http://localhost/examresult?course=<course>&matricno=<matricno>`

---

## 📁 Project Structure

```
.
├── app.py                  # Main Flask application
├── studentsregister.csv    # Student registration data
└── examscores.csv          # Exam scores data
```

---

## 📬 Contact

If you have any questions or suggestions:

- 📧 Email: [jamiuabdulazeez689@gmail.com](mailto:jamiuabdulazeez689@gmail.com)
- 💼 Twitter/X: [@JamiuOladi55000](https://x.com/JamiuOladi55000?t=AfyCwGxAg0OnFC0EBw1nqw&s=09)

---

## 📜 License

MIT License – see [`LICENSE`](LICENSE) for details.
```

---
