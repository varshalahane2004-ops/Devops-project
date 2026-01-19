pipeline {
  agent any

  stages {
    stage('Clone Repo') {
      steps {
        git 'https://github.com/varshalahane2004-ops/Devops-project.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t flaskapp:latest .'
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