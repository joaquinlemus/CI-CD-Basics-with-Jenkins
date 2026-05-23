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
post {
    success {
        mail to: 'tu@gmail.com',
             subject: "Build exitoso: ${env.JOB_NAME}",
             body: "El pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} completó exitosamente."
    }
    failure {
        mail to: 'tu@gmail.com',
             subject: "Build fallido: ${env.JOB_NAME}",
             body: "El pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} falló. Revisa el Console Output."
    }
}
