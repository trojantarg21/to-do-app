A simple and efficient to-do list application built with Flask (Python). The app allows users to create, update, and delete tasks, helping you stay organized and productive.

Table of Contents:
1. Features

2. Installation

3. Usage

4. Technologies

5. Running Tests

6. Docker Setup

7. Contributing

8. License

Features
1. Add tasks to your to-do list

2. Mark tasks as completed

3. Delete tasks

4. Simple, clean, and intuitive interface

Installation
   
Follow these steps to set up the project locally:

Clone the repository:
git clone https://github.com/trojantarg21/todo_app.git
cd todo_app

Install dependencies:
pip install -r requirements.txt

Usage
To start the Flask server locally, run:
python app.py
The app will run at http://localhost:5000.

Technologies
Flask: A lightweight Python web framework.

HTML/CSS: For creating the frontend user interface.

Running Tests
This project includes unit tests to ensure the app works as expected. To run the tests, use pytest.

Install pytest: If you don’t have pytest installed, you can install it by running:
pip install pytest

Run tests: To run the tests, execute the following command:
pytest

Docker Setup
This project also includes a Dockerfile to containerize the application. To build and run the app in Docker:

Build the Docker image:
docker build -t todo_app .

Run the Docker container:
docker run -p 5000:8000 todo_app
You can now access the app at http://localhost:5000.

Contributing

Fork the repository:
Create a new branch (git checkout -b feature/your-feature-name).

Make your changes:
Commit your changes (git commit -am 'Add your feature').

Push to the branch (git push origin feature/your-feature-name).

Open a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
