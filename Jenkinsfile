pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat '''
                C:\\Users\\sidda\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m pip install --upgrade pip
                C:\\Users\\sidda\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe install -r requirements.txt
                '''
            }
        }

        stage('Run') {
            steps {
                bat '''
                C:\\Users\\sidda\\AppData\\Local\\Programs\\Python\\Python310\\python.exe app.py
                '''
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed.'
        }
    }
}
