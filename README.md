Assignment Submission

This project contains the completion of all three assigned tasks.

--------------------------------------------------
Task 1: Laravel Project Setup
--------------------------------------------------
- Laravel project was set up locally.
- Database was configured using the provided SQL file.
- Login page is accessible at:
  http://127.0.0.1:8000/login
- Screenshot of the login page is included.

--------------------------------------------------
Task 2: Python Selenium Automation
--------------------------------------------------
- A Python Selenium script was created.
- File name: login_automation.py
- The script performs the following:
  - Opens the Laravel login page
  - Fills email and password fields with sample values
  - Closes the browser automatically

--------------------------------------------------
Task 3: HTML Page Integration
--------------------------------------------------
- An HTML calendar page was added to the Laravel project.
- Blade file created:
  resources/views/calendar.blade.php
- Route added:
  /html-page
- Calendar page loads successfully inside Laravel.
- Screenshot of the calendar page is included.

--------------------------------------------------
How to Run the Laravel Project
--------------------------------------------------
1. Open terminal in project root folder
2. Run:
   composer install
3. Copy:
   .env.example to .env
4. Run:
   php artisan key:generate
5. Start server:
   php artisan serve

--------------------------------------------------
How to Run Python Automation Script
--------------------------------------------------
1. Install dependencies:
   pip install selenium webdriver-manager
2. Run script:
   python login_automation.py

--------------------------------------------------
Files Included
--------------------------------------------------
- main-laravel/   (Laravel project)
- login_automation.py
- screenshots/   (Login page and calendar page screenshots)

--------------------------------------------------
End of Submission
--------------------------------------------------
