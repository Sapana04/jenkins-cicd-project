pipeline {

    agent any

    environment {
        IMAGE_NAME = "demo-app"
        TAG = "v1"
        CONTAINER_NAME = "demo"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Sapana04/jenkins-cicd-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                --name $CONTAINER_NAME \
                -p 5000:5000 \
                $IMAGE_NAME:$TAG
                '''
            }
        }

        stage('Verify Container') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {

        success {
            echo 'CI/CD Pipeline Successfully Executed 🚀'
        }

        failure {
            echo 'Pipeline Failed ❌'
        }
    }
}

