# Django Ticket System

## Project Overview
The Django Ticket System is a web-based platform for managing and tracking support tickets. It allows users to submit, prioritize, and monitor tickets, providing an efficient way to manage issues and requests within an organization.

## Features
- User authentication (sign up, login, logout)
- Create, update, and delete tickets
- Track ticket status (Active,Pending,Compleated)
- Admin panel for managing tickets and users

## Technologies Used
- **Django**: Backend framework
- **SQLite**: Default database (can be replaced with PostgreSQL, MySQL, etc.)
- **HTML/CSS**: Frontend design

## Getting Started

### Prerequisites
To run this project locally, you will need the following:
- Python 3.x
- Django 4.x
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/django-ticket-system.git
    cd django-ticket-system
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Visit the app at `http://127.0.0.1:8000/`

## Usage
- Register an account or log in to start using the ticket system.
- Create new tickets, assign them priorities, and track their progress.
- Admin users can manage tickets and users from the Django admin panel.

## Folder Structure
```plaintext
src/
│
├── project/       # Main Django project folder (core configuration)
│   ├── templates/ 
│   |           ├── main.html          # Main global template
│   |           ├── users.html         # Template for user-related views
│   ├── __init__.py          # Marks this folder as a Python package
│   ├── asgi.py              # ASGI configuration for async handling
│   ├── settings.py          # Django settings file (main configuration)
│   ├── urls.py              # Project-wide URL routing
│   └── wsgi.py              # WSGI configuration for web servers
│
├── tickets/       # Tickets app (handles ticket-related functionality)
│   ├── templates/ 
│   |           ├── all_closed_tickets.html  # Displays all closed tickets
│   |           ├── all_tickets.html         # Displays all tickets
│   |           ├── create_ticket.html       # Form to create a new ticket
│   |           ├── ticket_detail.html       # Shows the details of a ticket
│   |           ├── tickets_queue.html       # Queue or list of tickets in progress
│   |           ├── update_ticket.html       # Form to update a ticket
│   |           └── workspace.html           # Workspace view for ticket management
│   ├── __init__.py          # Marks this folder as a Python package
│   ├── admin.py             # Django admin configuration for tickets
│   ├── apps.py              # App configuration (e.g., name and settings)
│   ├── models.py            # Database models for tickets
│   ├── tests.py             # Unit tests for the tickets app
│   ├── urls.py              # URL routing for the tickets app
│   └── views.py             # Views (controllers) for ticket handling
│
├── users/         # Users app (handles authentication and user-related functionality)
│   ├── templates/ 
│   |           ├── login.html            # Login page template
│   |           └── dashboard.html        # Dashboard for logged-in users
│   ├── __init__.py          # Marks this folder as a Python package
│   ├── admin.py             # Django admin configuration for users
│   ├── apps.py              # App configuration for users
│   ├── forms.py             # Forms related to users (e.g., login, registration)
│   ├── models.py            # User-related database models
│   ├── tests.py             # Unit tests for the users app
│   ├── urls.py              # URL routing for the users app
│   └── views.py             # Views (controllers) for user-related actions
│
├── static/              # Static files (CSS, JS, images)
├── templates/           # Global templates (shared across all apps)
├── manage.py            # Django management script (runserver, migrations, etc.)
└── requirements.txt     # Project dependencies (third-party libraries)
