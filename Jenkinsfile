pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Sapana04/jenkins-cicd-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t demo-app:v1 .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f demo || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name demo -p 5000:5000 demo-app:v1'
            }
        }
    }

    post {
        success {
            echo "Deployment Successful 🚀"
        }
        failure {
            echo "Deployment Failed ❌"
        }
    }
}

