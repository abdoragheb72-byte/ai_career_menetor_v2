import sqlite3

DATABASE_NAME = "career_mentor.db"


def get_connection():
    """إنشاء اتصال بقاعدة البيانات."""
    return sqlite3.connect(DATABASE_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cv_evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        cv_text TEXT,
        score REAL,
        feedback TEXT,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cover_letters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        letter_text TEXT,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question TEXT,
        answer TEXT,
        date TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


# ---------------------- Users ----------------------

def add_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    conn.close()

    return rows


# ---------------------- CV ----------------------

def save_cv_evaluation(user_id, cv_text, score, feedback, date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO cv_evaluations
    (user_id, cv_text, score, feedback, date)
    VALUES (?, ?, ?, ?, ?)
    """, (user_id, cv_text, score, feedback, date))

    conn.commit()
    conn.close()


def get_all_cv_evaluations():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cv_evaluations")

    rows = cursor.fetchall()

    conn.close()

    return rows


# ---------------------- Cover Letter ----------------------

def save_cover_letter(user_id, letter_text, date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO cover_letters
    (user_id, letter_text, date)
    VALUES (?, ?, ?)
    """, (user_id, letter_text, date))

    conn.commit()
    conn.close()


def get_all_cover_letters():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cover_letters")

    rows = cursor.fetchall()

    conn.close()

    return rows


# ---------------------- Interview ----------------------

def save_interview(user_id, question, answer, date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews
    (user_id, question, answer, date)
    VALUES (?, ?, ?, ?)
    """, (user_id, question, answer, date))

    conn.commit()
    conn.close()


def get_all_interviews():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interviews")

    rows = cursor.fetchall()

    conn.close()

    return rows


# ---------------------- Test ----------------------

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")