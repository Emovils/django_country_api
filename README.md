# Django Citizens RESTful API

A simple Django REST Framework (DRF) API for managing citizen records. This API allows you to create, read, update, and delete (CRUD) citizens with their basic details.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Features
- Add a new citizen with:
  - First Name
  - Father's Name
  - Mother's Name
  - Home Town
  - Gender
- Retrieve all citizens
- Retrieve a single citizen by ID
- Update a citizen’s information
- Delete a citizen

## Installation

1. Clone the repository:
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create a virtual environment
   python -m venv venv
   Activate the virtual environment:

On Windows:

venv\Scripts\activate


On macOS/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Start the server:

python manage.py runserver

Usage

You can access the API locally at:

http://127.0.0.1:8000/api/citizens/


Use Postman or any HTTP client to interact with the endpoints.

API Endpoints
Method	Endpoint	Description
GET	/api/citizens/	Retrieve all citizens
POST	/api/citizens/	Create a new citizen
GET	/api/citizens/{id}/	Retrieve a single citizen by ID
PUT	/api/citizens/{id}/	Update a citizen
PATCH	/api/citizens/{id}/	Partially update a citizen
DELETE	/api/citizens/{id}/	Delete a citizen
Example Requests & Responses
GET all citizens

Request:

GET http://127.0.0.1:8000/api/citizens/


Response:

[
  {
    "id": 1,
    "first_name": "John",
    "father_name": "Michael",
    "mother_name": "Sarah",
    "home_town": "Lagos",
    "gender": "Male"
  },
  {
    "id": 2,
    "first_name": "Jane",
    "father_name": "David",
    "mother_name": "Mary",
    "home_town": "Abuja",
    "gender": "Female"
  }
]

GET single citizen

Request:

GET http://127.0.0.1:8000/api/citizens/1/


Response:

{
  "id": 1,
  "first_name": "John",
  "father_name": "Michael",
  "mother_name": "Sarah",
  "home_town": "Lagos",
  "gender": "Male"
}

POST new citizen

Request:

POST http://127.0.0.1:8000/api/citizens/


Body (JSON):

{
  "first_name": "Alice",
  "father_name": "George",
  "mother_name": "Helen",
  "home_town": "Port Harcourt",
  "gender": "Female"
}


Response:

{
  "id": 3,
  "first_name": "Alice",
  "father_name": "George",
  "mother_name": "Helen",
  "home_town": "Port Harcourt",
  "gender": "Female"
}

PUT update citizen

Request:

PUT http://127.0.0.1:8000/api/citizens/3/


Body (JSON):

{
  "first_name": "Alice",
  "father_name": "George",
  "mother_name": "Helen",
  "home_town": "Kano",
  "gender": "Female"
}


Response:

{
  "id": 3,
  "first_name": "Alice",
  "father_name": "George",
  "mother_name": "Helen",
  "home_town": "Kano",
  "gender": "Female"
}

PATCH partial update

Request:

PATCH http://127.0.0.1:8000/api/citizens/3/


Body (JSON):

{
  "home_town": "Ibadan"
}


Response:

{
  "id": 3,
  "first_name": "Alice",
  "father_name": "George",
  "mother_name": "Helen",
  "home_town": "Ibadan",
  "gender": "Female"
}

DELETE citizen

Request:

DELETE http://127.0.0.1:8000/api/citizens/3/


Response:

204 No Content

Technologies

Python 3.12

Django 5.x

Django REST Framework

SQLite (default database)

Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

License

This project is licensed under the MIT License.
4. 

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
