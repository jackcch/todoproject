pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                echo "Stage 1 - Build Container Image"
                pwd
                docker build -t jackcch/todoproject:latest .
            }
        }
        stage('Push Image to Repository') {
            steps {
                echo "Stage 2 - Push Image to Repo"
            }
        }
    }
}