pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/flask-cicd"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/flask-cicd-jenkins-k8s.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    dockerImage.push('latest')
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                helm upgrade --install flask-app helm/flask-app --set image.repository=${DOCKER_IMAGE} --set image.tag=latest
                '''
            }
        }
    }
}
