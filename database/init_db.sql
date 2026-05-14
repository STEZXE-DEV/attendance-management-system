DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS class_groups;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE class_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER,
    teacher_id INTEGER,
    topic TEXT,
    lesson_date TEXT,

    FOREIGN KEY (class_id) REFERENCES class_groups(id),
    FOREIGN KEY (teacher_id) REFERENCES users(id)
);

CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    lesson_id INTEGER,
    status TEXT,
    created_by INTEGER,
    created_at TEXT,

    FOREIGN KEY (student_id) REFERENCES users(id),
    FOREIGN KEY (lesson_id) REFERENCES lessons(id),
    FOREIGN KEY (created_by) REFERENCES users(id)
);

INSERT INTO users (name, surname, email, password, role)
VALUES
('Admin', 'System', 'admin@school.com', 'admin123', 'admin'),
('Jan', 'Nowak', 'teacher@school.com', 'teacher123', 'teacher'),
('Adam', 'Kowalski', 'student@school.com', 'student123', 'student');

INSERT INTO class_groups (name)
VALUES ('1A');

INSERT INTO lessons (class_id, teacher_id, topic, lesson_date)
VALUES (1, 2, 'Matematyka', '2026-05-14');

INSERT INTO attendance (student_id, lesson_id, status, created_by, created_at)
VALUES (3, 1, 'present', 2, '2026-05-14 10:00');