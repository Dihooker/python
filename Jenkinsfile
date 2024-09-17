pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                git 'https://github.com/Dihooker/python.git'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Ejecutar Script Python') {
            steps {
                sh 'python3 prueba.py'
            }
        }
    }
}
