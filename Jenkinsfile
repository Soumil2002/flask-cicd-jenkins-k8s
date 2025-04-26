pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = "soumil22/flask-love-app"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Soumil2002/flask-cicd-jenkins-k8s.git'
            }
        }

        stage('Clean Old Docker Images') {
            steps {
                script {
                    sh """
                        docker images | grep ${IMAGE_NAME.split('/')[1]} || true
                        docker rmi -f \$(docker images -q ${IMAGE_NAME}) || true
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Logout DockerHub') {
            steps {
                sh "docker logout"
            }
        }
        
      
        
        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                helm upgrade --install flask-love-app ./helm/flask-app \
                    --set image.repository=${IMAGE_NAME} \
                    --set image.tag=latest
                '''
            }
        }
    
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
