# 📚 Bookstore Management System

A Django-based Bookstore Management System built with Class-Based Views, custom admin panel, manual form handling, and session-based cart logic. The project is containerized with Docker and includes a Jenkins pipeline for CI/CD.

---

## 🚀 Project Overview

This application allows users to register, log in, browse books, view book details, and add books to a session-based cart. Admin users (through a **custom admin panel**) can manage book inventory (add/edit/delete books). Built strictly using Class-Based Views (CBV), with no use of Django forms or the default admin panel.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django (CBVs only)
- **Frontend**: HTML, CSS (manual forms)
- **Database**: SQLite (dev), PostgreSQL (optional for production)
- **DevOps**: Docker, Docker Compose, Jenkins (CI/CD)
- **Version Control**: Git & GitHub

---

## 🧩 Features

### 👥 Authentication
- User Registration
- User Login/Logout

### 📘 Book Features
- View list of books
- Book details page

### 🛒 Cart (Session-based)
- Add to cart using Django sessions (no DB storage)

### 🛠️ Admin Panel (Custom)
- Admin login (not Django admin)
- Add/Edit/Delete books
- Inventory management

---

## ⚙️ Setup & Run Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shiledae2005/project_book_store.git
cd book_cart-main
