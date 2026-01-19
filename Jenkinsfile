pipeline {
  agent any

  stages {
    stage('Clone Repo') {
      steps {
        git 'https://github.com/yourusername/devops-project.git'
      }
    }

    stage('Build Image') {
      steps {
        sh 'docker build -t yourdockerhubusername/flaskapp:latest .'
      }
    }

    stage('Push Image') {
      steps {
        sh 'docker push yourdockerhubusername/flaskapp:latest'
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f deployment.yaml'
        sh 'kubectl apply -f service.yaml'
      }
    }
  }
}