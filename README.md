# Django PostgreSQL Project

This project demonstrates how to set up a Django application with a PostgreSQL database.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- PostgreSQL
- `pip` (Python package installer)
- `virtualenv` (for creating isolated Python environments)

## Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/jourzy/first-django-postgres.git
   cd first-django-postgres/django_postgres_project
   ```

2. **Create and activate a virtual environment:**

    ```
    python -m venv env
    # On Windows
    env\Scripts\activate
    # On Unix or MacOS
    source env/bin/activate
    ```

3. **Install the required packages:**

    ```pip install -r requirements.txt```


4. **Configure the PostgreSQL database:**

    - Ensure PostgreSQL is running.

    - Create a new PostgreSQL database and user.

    - Update the ```DATABASES``` setting in ```settings.py``` with your database credentials:

    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Apply database migrations:**

    ```python manage.py migrate```


6. **Create a superuser (optional):**

    ```python manage.py createsuperuser```

7. **Run the development server:**

    ```python manage.py runserver```

    Access the application at http://127.0.0.1:8000/.
