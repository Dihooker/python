pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clona tu repositorio desde GitHub y especifica la rama
                git branch: 'main', url: 'https://github.com/Dihooker/python.git'
            }
        }
        stage('Verificar Python') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Ejecutar prueba.py') {
            steps {
                sh 'python3 prueba.py'
            }
        }
    }
}
