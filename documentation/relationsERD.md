# 📊 Attendance Management System - ERD

## 📌 Opis
Poniższy diagram przedstawia strukturę bazy danych systemu zarządzania frekwencją w szkole (Flask + SQLAlchemy).

---

## 📊 Diagram relacji (Mermaid)

```mermaid
erDiagram

    USER {
        int id PK
        string username
        string password
        string role
        int student_id FK
        int teacher_id FK
    }

    STUDENT {
        int id PK
        string name
        int class_id FK
    }

    TEACHER {
        int id PK
        string name
        int class_id FK
    }

    SCHOOL_CLASS {
        int id PK
        string name
    }

    SUBJECT {
        int id PK
        string name
    }

    LESSON {
        int id PK
        string day
        string hour
        int class_id FK
        int teacher_id FK
        int subject_id FK
    }

    ATTENDANCE {
        int id PK
        int student_id FK
        int lesson_id FK
        boolean present
    }

    SCHOOL_CLASS ||--o{ STUDENT : contains
    SCHOOL_CLASS ||--o{ TEACHER : assigned

    SCHOOL_CLASS ||--o{ LESSON : has
    TEACHER ||--o{ LESSON : conducts
    SUBJECT ||--o{ LESSON : teaches

    LESSON ||--o{ ATTENDANCE : has
    STUDENT ||--o{ ATTENDANCE : marks

    USER ||--o| STUDENT : profile
    USER ||--o| TEACHER : profile