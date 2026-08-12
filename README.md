# Student Management System

Hi — I'm Manohar. I built this Student Management System as a Django project to manage students, courses, enrollments, attendance, grades and basic reports.

This repo contains the Django app modules I used while building it:

- accounts — custom user / auth related code
- students — student models, views and templates
- courses — courses and curriculum management
- enrollments — student-course relationships
- attendance — attendance tracking
- grades — grade entry and reporting
- departments — department/org structure
- reports — generation of simple reports
- dashboard — a simple admin dashboard
- audit — auditing / change tracking helpers
- core / student_management — project configuration and settings
- templates — HTML templates used by the project

I keep a SQLite DB in the repo for reference (db.sqlite3.before-custom-user.sqlite3). If you want to start from a clean database, delete db.sqlite3 and run the migrations.

Requirements
------------
This project was developed with Python and Django. The repository includes a requirements file named `requrements.txt` (note: spelled without the second 'i') — use that to install dependencies.

Setup (quick)
-------------
1. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell)

2. Install dependencies:

   pip install -r requrements.txt

3. Apply migrations and create a superuser:

   python manage.py migrate
   python manage.py createsuperuser

4. Run the development server:

   python manage.py runserver

5. Open http://127.0.0.1:8000/ in your browser.

Notes
-----
- The project uses SQLite by default. If you prefer PostgreSQL or MySQL, update `student_management/settings.py` DATABASES and install the appropriate DB driver.
- There is a sample SQLite file included (`db.sqlite3.before-custom-user.sqlite3`). I left it in the repo for convenience when testing users, but you might want to remove it before publishing a production app.
- If you spot any typos (I know `requrements.txt` is misspelled), feel free to send a PR — I can fix it or you can.

Development
-----------
- Tests: I didn't include automated tests in this snapshot. Adding unit tests for models and views would be a great improvement.
- Formatting: I normally use black/isort for formatting — not enforced here yet.

Contributing
------------
If you'd like to contribute, open an issue or submit a pull request. Small, focused PRs are easiest to review.

License
-------
Add a license file if you intend to make this open-source. For now, this repo has no license specified.

Contact
-------
If you want to reach me about this project, open an issue or contact me on my GitHub profile: https://github.com/manoharworks
