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



