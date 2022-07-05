pipeline {
    agent any
    stages {
        stage('Checkout Source Code') {
            steps {
                echo "Stage 1 - Checkout Source Code"
            }
        }
        stage('Build Image') {
            steps {
                echo "Stage 2 - Build Container Image"
            }
        }
        stage('Push Image to Repository') {
            steps {
                echo "Stage 3 - Push Image to Repo"
            }
        }
    }
}