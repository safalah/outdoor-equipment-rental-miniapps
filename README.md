# Flask Equipment Rental Management System

This is a web-based Equipment Rental Management System built with Python and Flask. The application supports two main roles: Admin and User (Renter), and uses SQLite for data storage via Flask-SQLAlchemy.

## Features

### Authentication & Authorization
- **User Registration:** Users can register with personal details and address information.
- **Login/Logout:** Secure access with session management. Includes security features like a login attempt limit (locks out after 5 failed attempts).
- **Role-based Access Control:** Separate dashboards and functionalities for Admin and User roles.

### Admin Features
- **Equipment Management:** Admins can view, add, update, and delete equipment inventory.
- **Rentals Management:** Admins can view all rental transactions, filter them by status (active, returned, cancelled), and delete rental records.

### User (Renter) Features
- **View Equipment:** Browse available equipment for rent.
- **Manage Rentals:**
  - Create new rental transactions.
  - Update active rentals (change quantity or duration).
  - Cancel rentals.
  - Return rented items.
- **Invoicing:** View generated invoices for active rental transactions.
- **Profile Management:** View personal profile, update UserID or password, and delete account.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite (managed via Flask-SQLAlchemy)
- **Frontend:** HTML templates (Jinja2)
- **Deployment:** Ready for deployment with Gunicorn (`Procfile` included)

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation & Setup

1. **Clone or Download the Repository**

2. **Navigate to the Project Directory**
   ```bash
   cd path/to/project
   ```

3. **Install Dependencies**
   Install the required Python packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   The database (`tugas_project.db`) is automatically created in the `instance` folder when the application is run for the first time.

5. **Run the Application**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000` or `http://localhost:5000`.

## Project Structure

- `app.py`: Main Flask application file containing all routes and controllers.
- `Database.py`: Database connection and CRUD operations.
- `Equipment_Management.py`, `Rents_Management.py`, `Renter.py`, `Main_Menu.py`, `Menu_Auth.py`, `Profile.py`, `Invoice.py`: Modules handling specific domain logic.
- `Validators.py`: Contains validation logic (e.g., for registration).
- `templates/`: Directory containing all HTML files.
- `instance/`: Directory where the SQLite database file is stored.

## Deployment
The project includes a `Procfile` and `gunicorn` in its `requirements.txt`, making it ready for deployment on platforms like Heroku or Render.
