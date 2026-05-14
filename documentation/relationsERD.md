# 📊 Attendance Management System - ERD

## Diagram relacji (Mermaid)

```mermaid
erDiagram

    USERS {
        int id PK
        string name
        string surname
        string email
        string password
        string role
    }

    CLASS_GROUPS {
        int id PK
        string name
    }

    LESSONS {
        int id PK
        int class_id FK
        int teacher_id FK
        string topic
        string lesson_date
    }

    STUDENT_CLASS {
        int student_id FK
        int class_id FK
    }

    ATTENDANCE {
        int id PK
        int student_id FK
        int lesson_id FK
        string status
        int created_by FK
        string created_at
    }

    USERS ||--o{ LESSONS : teaches
    CLASS_GROUPS ||--o{ LESSONS : has
    USERS ||--o{ ATTENDANCE : marks
    LESSONS ||--o{ ATTENDANCE : contains

    USERS ||--o{ STUDENT_CLASS : assigned
    CLASS_GROUPS ||--o{ STUDENT_CLASS : contains