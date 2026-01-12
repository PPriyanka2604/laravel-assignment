Laravel & Python Automation 
Overview

This repository contains the completed implementation of the assigned tasks involving a Laravel web application, Python Selenium automation, and HTML page integration. The project demonstrates backend setup, basic authentication flow, browser automation, and route-based view rendering in Laravel.

Task 1: Laravel Project Setup
Description

A Laravel project was set up and configured locally. The application includes a login page and routing setup to verify successful rendering.

Key Points

Laravel project configured locally

Login page accessible at:
http://127.0.0.1:8000/login

Laravel server runs successfully using php artisan serve

Screenshot of the running Laravel server and login page included

Task 2: Python Selenium Automation
Description

A Python script was created using Selenium to automate the login process of the Laravel application.

Features

Python script: login_automation.py

Uses Selenium and webdriver-manager

Opens the Laravel login page

Fills email and password fields with sample credentials

Clicks the login button

Closes the browser automatically after execution

Requirements
pip install selenium webdriver-manager

Run Script
python login_automation.py


Screenshot of the automated browser execution is included.

Task 3: HTML Page Integration in Laravel
Description

A static HTML page was integrated into the Laravel project using Blade and routing.

Implementation

Blade file created at:
resources/views/calendar.blade.php

Route added in routes/web.php

Page accessible at:
http://127.0.0.1:8000/html-page

Page displays confirmation text:
“Calendar Page Loaded Successfully”

Screenshot of the calendar page is included.

Project Structure
main-laravel/
├── app/
├── routes/
│   └── web.php
├── resources/
│   └── views/
│       ├── login.blade.php
│       ├── calendar.blade.php
│       └── welcome.blade.php
├── public/
├── screenshots/
│   ├── laravel_server.png
│   ├── python_automation.png
│   └── calendar_page.png
├── login_automation.py
└── README.md

How to Run the Laravel Project

Navigate to the Laravel project folder:

cd main-laravel


Install dependencies:

composer install


Copy environment file:

cp .env.example .env


Generate application key:

php artisan key:generate


Start the server:

php artisan serve

Files Included

main-laravel/ – Laravel application

login_automation.py – Python Selenium script

screenshots/ – Proof of execution (Laravel server, login page, automation, calendar page)

Notes

The vendor/ folder is excluded from version control and should be installed via Composer.

Screenshots are included as execution proof.

Author

Priyanka
GitHub: PPriyanka2604
