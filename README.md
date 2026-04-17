# Student Score Management System

This is a course project for **HKMU COMP2090SEF**

A simple student score management system, support class filtering, auto ID generation, score ranking and statistics.

---

## Features
- Student information management (Add/Delete/Update/Query)
- Score ranking: support total score or single subject ranking
- Score statistics: Max/Min/Avg score, and pass rate for each subject
- Data persistence: save/load data from files
- Compatible with Traditional Chinese Windows: force UTF-8 encoding, no cp950 decode error

---

## Task 1: OOP-based Application Development
- **OOP Concepts**: Used encapsulation, private attributes, getter/setter methods as required.
- **Modular Design**: Split into 3 independent modules:
  - `student.py`: Student data class
  - `student_manager.py`: Core business logic
  - `main.py`: User interaction and main loop

---

## Task 2: Self-study Content
> These are NOT covered in the course, self-studied for this project.

### 1. Self-studied Data Structure: Heap
Used MaxHeap and MinHeap to efficiently get max/min score, with **O(logn)** time complexity for insert and get operation, much faster than O(n) traverse.

### 2. Self-studied Algorithm: Merge Sort
Used Merge Sort for student ranking, with **O(nlogn)** time complexity, much faster than the bubble sort taught in course.

---

## How to Run
Download the file name Program and run main.py

---

## Introduction video
https://youtu.be/Tg69ZSWtuLs

---

## Contribution
- So Tsz Tsun (14268617)
  - Design overall code framework
  - Write student_manager.py
  - Beautify program output
  - Write README.md
  - Introduction video
  - Debug
- WU Hao (14006039)
  - Write main.py
  - Write task1 Report
  - Debug
  - write testing document
- Cheng Xiang Wei (14175935)
  - Write student.py
  - Write task2 Report
  - Debug
  - write testing document
