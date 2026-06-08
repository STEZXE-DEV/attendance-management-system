# Attendance Management System

## Opis projektu

Attendance Management System to aplikacja webowa stworzona przy użyciu frameworka Flask, służąca do zarządzania frekwencją uczniów. System umożliwia administratorowi zarządzanie klasami, użytkownikami i lekcjami, nauczycielowi zaznaczanie obecności uczniów, a uczniowi podgląd własnej frekwencji.

Projekt został wykonany jako aplikacja klient-serwer z wykorzystaniem bazy danych SQLite oraz biblioteki SQLAlchemy ORM.

---

## Funkcjonalności

### Administrator

* logowanie do systemu,
* dodawanie i usuwanie klas,
* dodawanie i usuwanie uczniów,
* dodawanie i usuwanie nauczycieli,
* dodawanie przedmiotów,
* tworzenie lekcji,
* przypisywanie nauczycieli i klas do lekcji,
* podgląd wszystkich danych systemu.

### Nauczyciel

* logowanie do systemu,
* przegląd własnych lekcji,
* wyświetlanie listy uczniów przypisanej klasy,
* zaznaczanie obecności lub nieobecności uczniów,
* edycja zapisanej frekwencji.

### Uczeń

* logowanie do systemu,
* podgląd własnej historii frekwencji,
* wyświetlanie informacji o lekcji, której dotyczy wpis frekwencji.

---

## Technologie

* Python 3
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* Bootstrap 5

---

## Instalacja

### 1. Klonowanie projektu

```bash
git clone <adres_repozytorium>
cd attendance-management-system
```

### 2. Instalacja zależności

```bash
pip install flask flask-sqlalchemy pytest
```

### 3. Inicjalizacja bazy danych

```bash
python db_init.py
```

### 4. Uruchomienie aplikacji

```bash
python app.py
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:5000
```

---

## Przykładowe konta

### Administrator

```text
login: admin
hasło: admin
```

### Nauczyciel

```text
login: t1
hasło: t1
```

### Uczeń

```text
login: s1
hasło: s1
```

---

## Baza danych

System wykorzystuje relacyjną bazę danych SQLite.

Główne tabele:

* User
* Student
* Teacher
* SchoolClass
* Subject
* Lesson
* Attendance

Relacje zostały opisane w diagramie ERD znajdującym się w dokumentacji projektu.

---

## Testy

Projekt zawiera testy jednostkowe oraz integracyjne.

Uruchomienie testów:

```bash
pytest
```

Przykładowy wynik:

```text
6 passed in 3 seconds
```

Testy obejmują:

* logowanie użytkowników,
* autoryzację dostępu,
* działanie panelu administratora,
* operacje na bazie danych,
* poprawność routingu aplikacji.

---

## Architektura

Projekt został zrealizowany w architekturze klient-serwer.

### Klient

Przeglądarka internetowa użytkownika.

### Serwer

Aplikacja Flask odpowiedzialna za logikę biznesową.

### Baza danych

SQLite obsługiwana przez SQLAlchemy ORM.

```text
Przeglądarka
      ↓ HTTP
     Flask
      ↓ ORM
    SQLite
```

---

## Autor

Projekt wykonany w ramach zaliczenia przedmiotu programistycznego.
