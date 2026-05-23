pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Building app..."'
                sh 'python3 app.py'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                sh 'pytest test_app.py -v'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Building Docker image..."'
                sh 'docker build -t devops-app .'
                sh 'docker run --rm devops-app'
            }
        }
    }
}
