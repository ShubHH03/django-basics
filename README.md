
# Django Basics

This repository provides a basic setup for a Django project. It includes instructions for setting up the environment, creating a Django project, running the project, and creating an app within the project.

## Environment Setup

### Windows

1. Create a virtual environment:
    ```sh
    python -m venv env
    ```

2. Activate the virtual environment:
    ```sh
    .\env\Scripts\activate
    ```

### Mac

1. Create a virtual environment:
    ```sh
    python3 -m venv env
    ```

2. Activate the virtual environment:
    ```sh
    source env/bin/activate
    ```

## Install Django

Once the virtual environment is activated, install Django using pip:

```sh
pip install django
```

## Creating a Django Project

To create a new Django project, run the following command:

```sh
django-admin startproject <project-name>
```

## Running the Project

Navigate to the project directory and run the following command to start the development server:

```sh
python manage.py runserver
```

## Creating a Django App

To create a new app within your Django project, run the following command:

```sh
python manage.py startapp <app-name>
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
