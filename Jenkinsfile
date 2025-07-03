pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                bat '''
                C:\\Users\\mdtal\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m pip install --upgrade pip
                C:\\Users\\mdtal\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run') {
            steps {
                bat '''
                C:\\Users\\mdtal\\AppData\\Local\\Programs\\Python\\Python312\\python.exe app.py
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

}
