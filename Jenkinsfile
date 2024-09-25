pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8'
    }

    stages {
        stage('Preparar Entorno') {
            steps {
                script {
                    // Instalar dependencias si usas un archivo requirements.txt
                   
                }
            }
        }

        stage('Ejecutar Pruebas') {
            steps {
                // Asegúrate de tener un archivo de pruebas, por ejemplo, test_calculadora.py
                sh "python${PYTHON_VERSION} -m pytest test_calculadora.py"
            }
        }

        stage('Construir Artefacto') {
            steps {
                // Si tu calculadora genera algún artefacto, puedes construirlo aquí
                echo 'Construyendo el artefacto...'
            }
        }

        stage('Despliegue') {
            steps {
                // Despliegue de tu aplicación, si aplica
                echo 'Desplegando la aplicación...'
            }
        }
    }

    post {
        always {
            // Limpieza del entorno
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
