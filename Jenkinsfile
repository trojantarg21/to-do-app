pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub_credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/trojantarg21/to-do-app'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Docker Build & Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub_credentials', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        bat """
                        echo %DOCKERHUB_PASSWORD% | docker login -u %DOCKERHUB_USERNAME% --password-stdin
                        docker build -t %DOCKERHUB_USERNAME%/todo_app:latest .
                        docker push %DOCKERHUB_USERNAME%/todo_app:latest
                        """
                    }
                }
            }
        }
    }
}

