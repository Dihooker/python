pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
    }

    stages {
        stage('Ejecutar Pruebas') {
            steps {
                // Ejecutar pruebas con pytest o cualquier otro framework que uses
                sh "python${PYTHON_VERSION} -m pytest test_calculadora.py"
            }
        }

        stage('Construir Artefacto') {
            steps {
                // Construir tu artefacto si es necesario
                echo 'Construyendo el artefacto...'
            }
        }

        stage('Despliegue') {
            steps {
                // Despliegue de tu aplicación (esto puede variar según tu configuración)
                echo 'Desplegando la aplicación...'
            }
        }
    }

    post {
        always {
            echo 'Limpieza del entorno...'
            cleanWs()
        }
        success {
            echo 'Pipeline completado con éxito.'
        }
        failure {
            echo 'Pipeline fallido. Revisa los logs para más detalles.'
        }
    }
}

