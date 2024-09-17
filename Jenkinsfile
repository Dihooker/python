pipeline {
    agent any
    stages {
        stage('Clonar Repositorio') {
            steps {
                // Clona tu repositorio desde GitHub
                git 'https://github.com/Dihooker/python.git'
            }
        }
        stage('Verificar Python') {
            steps {
                // Verifica que Python esté instalado
                sh 'python3 --version'
            }
        }
        stage('Ejecutar prueba.py') {
            steps {
                // Ejecuta tu script prueba.py
                sh 'python3 prueba.py'
            }
        }
    }
}

