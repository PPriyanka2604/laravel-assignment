# Laravel & Python Selenium Automation Project 🚀

This repository contains a Laravel web application integrated with a Python Selenium automation script.  
The project demonstrates backend setup, routing, Blade views, and browser automation for login and page navigation.

---

## ✨ Features

### 🔹 Laravel Application
- Laravel project configured and running locally
- Login page rendered using Blade templates
- Custom HTML (Calendar) page integrated into Laravel
- Routing handled via `routes/web.php`
- Pages served using `php artisan serve`

### 🔹 Python Selenium Automation
- Automated browser testing using Selenium
- Opens the Laravel login page
- Fills email and password fields with sample data
- Clicks the login button
- Verifies page navigation
- Closes the browser automatically after execution

### 🔹 HTML Page Integration
- Static Calendar page integrated into Laravel
- Blade view created for calendar page
- Route configured for `/html-page`
- Page successfully loads inside Laravel

---

## 🛠️ Technologies Used

- **Backend:** Laravel (PHP)
- **Frontend:** Blade, HTML, CSS
- **Automation:** Python, Selenium, WebDriver Manager
- **Browser:** Microsoft Edge / Chrome
- **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
laravel/
├── main-laravel/
│   ├── app/
│   ├── public/
│   ├── resources/
│   │   └── views/
│   │       ├── login.blade.php
│   │       ├── calendar.blade.php
│   │       └── welcome.blade.php
│   ├── routes/
│   │   └── web.php
│   ├── .env.example
│   └── artisan
│
├── login_automation.py
│
├── screenshots/
│   ├── laravel_server.png
│   ├── python_automation.png
│   └── calendar_page.png
│
└── README.md

````
⚙️ Installation & Setup

1️⃣ Laravel Setup

```

cd main-laravel
composer install
cp .env.example .env
php artisan key:generate
php artisan serve

````
Laravel server will run at:
```
http://127.0.0.1:8000

```
Login Page:
```
http://127.0.0.1:8000/login

```
Calendar Page:
```
http://127.0.0.1:8000/html-page

```
2️⃣ Python Selenium Setup
Install dependencies:
```
pip install selenium webdriver-manager

```
Run automation script:
```
python login_automation.py

```
📸 Screenshots

Screenshots are included as proof of execution:

Laravel server running

Automated login using Selenium

Calendar page successfully loaded

Location:
```
screenshots/

```
📝 Notes

The vendor/ folder is excluded from version control and must be installed via Composer

Screenshots are included for validation purposes

Sample credentials are used only for demonstration

👩‍💻 Author

Priyanka
GitHub: PPriyanka2604
