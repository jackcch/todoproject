def containerName="todoproject"
def tag="latest"
def dockerHubUser="jackcch"
def gitURL="https://github.com/jackcch/todoproject.git"
pipeline {
    agent any
    stages {
        stage('Build Image') {
            steps {
                echo "Stage 1 - Build Container Image"
                sh "pwd"
                sh "docker image prune -f"
                sh "docker build -t $containerName:$tag --pull --no-cache ."
                echo "Stage 1 - Image Build Completed"
            }
        }
        stage('Push Image to Repository') {
            steps {
                echo "Stage 2 - Push Image to Repo"
                withCredentials([usernamePassword(credentialsId: 'dockerHubAccount', usernameVariable: 'dockerUser', passwordVariable: 'dockerPassword')]) 
                {
                    sh ('docker login -u $dockerUser -p $dockerPassword')
                    sh "docker tag $containerName:$tag $dockerUser/$containerName:$tag"
                    sh "docker push $dockerUser/$containerName:$tag"
                }
            }
        }
    }
}