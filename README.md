# Backend Assignment Django Project

This is a basic Django project that serves a app in which you can have user and post.

## Getting Started

These instructions will help you set up and run the project on your local machine for development purposes.


1. Clone this repository to your local machine:

```commandline
git clone https://github.com/srinivaskstpl/backend-assignment.git
cd backend-assignment
```


### Prerequisites

Before you begin, make sure you have the following software installed on your system:

### Installing Dependencies

2. Create a virtual environment to isolate project dependencies:

```commandline
python -m venv /path/to/new/virtual/environment
```

3. Activate the virtual environment:

    - On Windows:

    ```
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```
    source venv/bin/activate
    ```

4. Install project dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

### Running the Development Server

*Before running data base migration make sure 
you have created ```backendassignment``` project
in your postgres db.*

1. Apply initial database migrations:

```
python manage.py migrate
```

2. You can create a superuser by below command:

```
python manage.py createsuperuser
```

3. Start the development server:

```
python manage.py runserver
```


The development server should now be running at `http://localhost:8000/`.

3. Access the Django admin panel at `http://localhost:8000/admin/` and log in with the admin credentials.


## Run using docker

To run the project using docker follow the following steps.

1. Build the Docker image using the following command:

```commandline
docker build -t django-app .
```

2. Run the container using the following command:

```commandline
docker run -p 8000 --net="host" django-app
```

## postman collection
Postman collection JSON is added in repository you can import the file in postman