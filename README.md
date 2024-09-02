# Simple WSGI Application "Hello, World !!!"

This is a simple WSGI (Web Server Gateway Interface) application built with Python. The application is designed to serve a basic "Hello, World!" message or an HTML template.

## Project Structure

```plaintext
my_wsgi_project/
│
├── app.py               # Main WSGI application file
├── requirements.txt     # List of dependencies (optional)
├── wsgi.py              # WSGI server entry point (optional)
├── static/              # Directory for static files (optional)
│   ├── styles.css       # Example CSS file
│   └── script.js        # Example JavaScript file
└── templates/           # Directory for HTML templates (optional)
    └── index.html       # Example HTML template
```

## Files Description

- app.py: The core WSGI application file that handles requests and returns responses.
- requirements.txt: Contains the list of dependencies needed for the project, such as Gunicorn.
- wsgi.py: An entry point to run the application using a WSGI server like Gunicorn or the built-in server (wsgiref.simple_server).
- static/: A directory to store static files like CSS, JavaScript, and images.
- templates/: A directory to store HTML templates used in the application.

# Getting Started

## Prerequisites

- Python 3.x installed on your system.
- Optional: pip for managing Python packages.

## Installation

1. Clone the repository: <br/>

```sh
git clone https://github.com/your-username/my_wsgi_project.git
cd my_wsgi_project

```

2. (Optional) Create a virtual environment: <br/>

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies: <br/>

```sh
pip install -r requirements.txt
```

## Running the Application

You can run the application using Gunicorn or the built-in server (wsgiref.simple_server).

### Using Gunicorn

```sh
gunicorn wsgi:application
```

<br/>

- Visit http://localhost:8000 in your web browser.

### Using wsgiref.simple_server

- Definision : 'wsgiref.simple_server' is a simple WSGI server provided by Python for development and testing purposes.

```sh
python wsgi.py
```

<br/>

- Visit http://localhost:8000 in your web browser.

## Customization

- Static Files: Place your CSS, JavaScript, or image files in the static/ directory.
- HTML Templates: Modify the index.html file in the templates/ directory to change the HTML response.

## Conclusion

- The HelloWorld-BasicWSGI-App provides a straightforward introduction to WSGI applications in Python. With a simple setup, it demonstrates how to serve basic content using WSGI and how to structure a Python project with static files and HTML templates. This application serves as a foundation for more complex WSGI projects and can be easily extended to include additional functionality or integrate with other components.
  "# HelloWorld-BasicWSGI-App"
