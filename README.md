# 🧠 GenSQL: AI-Powered NoSQL / MongoDB → SQL Converter

A Generative AI-based web application that converts NoSQL and MongoDB JSON data into structured SQL queries using LLaMA 3.1 via Groq API.

---

## 🚀 Features

- 🔄 Convert NoSQL JSON → SQL
- 🍃 Convert MongoDB documents → SQL
- 🧩 Automatic schema inference
- 🏗️ Generates:
  - CREATE TABLE statements
  - INSERT queries
- 🔗 Handles nested JSON and arrays (normalization)
- 🗄️ Supports multiple SQL dialects:
  - MySQL
  - PostgreSQL
  - SQLite
- 📁 Upload JSON file or paste manually
- 📥 Download generated SQL

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **AI Model**: LLaMA 3.1 (via Groq API)  
- **Data Format**: JSON → SQL  

---

## 📸 Screenshots

### 🔹 Home Page
![Home](screenshots/home.png)

### 🔹 JSON Input
![Input](screenshots/input.png)

### 🔹 Generated SQL Output
![Output](screenshots/output.png)

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/GenSQL.git
cd GenSQL
