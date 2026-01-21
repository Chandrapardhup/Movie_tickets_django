🎬 Movie Ticket Booking Backend (Django)
📌 Project Overview

This project is a backend system for a Movie Ticket Booking application, built using Django and Django REST Framework.
It models real-world movie booking logic using a relational database and exposes REST APIs for core operations.

🧱 Database Design

The system uses 5 core tables:

Table	Description
Users	Stores user details
Movies	Stores movie information
Theatres	Stores theatre details
Shows	Connects movies and theatres with timing
Bookings	Stores ticket booking transactions
🔗 Relationship Design (Foreign Keys)

A movie runs in many theatres and a theatre runs many movies.

This many-to-many relationship is resolved using the Shows table.

Each Show represents a specific movie in a specific theatre at a specific time.

A Booking links a User and a Show, representing a real ticket booking.

Foreign Key Mapping:

Show.movie_id → Movie

Show.theatre_id → Theatre

Booking.user_id → User

Booking.show_id → Show

This ensures data integrity and normalized design.

🌐 API Endpoints (Minimal & Practical)
Entity	Method	Endpoint
Users	POST	/api/users/create/
Users	GET	/api/users/
Movies	POST	/api/movies/create/
Movies	GET	/api/movies/
Theatres	POST	/api/theatres/create/
Theatres	GET	/api/theatres/
Shows	POST	/api/shows/create/
Shows	GET	/api/shows/
Bookings	POST	/api/bookings/create/
Bookings	GET	/api/bookings/
⚙️ Technologies Used

Python

Django

Django REST Framework

SQLite

Git & GitHub

🚀 How to Run the Project
git clone <repository-url>
cd movie_booking
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

🧠 Key Learnings

Designing normalized relational schemas

Implementing many-to-many relationships using junction tables

Working with Django ORM and foreign keys

Building REST APIs with Django REST Framework

Structuring Django projects for scalability
