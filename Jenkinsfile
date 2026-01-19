ipeline {
  agent any

  stages {
    stage('Clone Repo') {
      steps {
        git 'https://github.com/varshalahane2004-ops/Devops-project.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        bat 'docker build -t flaskapp:latest .'
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        bat 'kubectl apply -f deployment.yaml'
        bat 'kubectl apply -f service.yaml'
      }
    }
  }
}