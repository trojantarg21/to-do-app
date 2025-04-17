pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/trojantarg21/to-do-app'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --maxfail=1 --disable-warnings -q' // Use pytest for Python projects
            }
        }

        stage('Docker Build & Push') {
            environment {
                DOCKERHUB_USERNAME = credentials('dockerhub_username') // Jenkins credentials for Docker Hub username
                DOCKERHUB_PASSWORD = credentials('dockerhub_password') // Jenkins credentials for Docker Hub password
            }
            steps {
                bat """
                echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin
                docker build -t %DOCKERHUB_USERNAME%/todo_app:latest .
                docker push %DOCKERHUB_USERNAME%/todo_app:latest
                """
            }
        }
    }
}
