pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat 'python -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest --html=report.html --self-contained-html -n 3'
            }
        }
    }

    post {

        always {
            archiveArtifacts artifacts: 'report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Playwright tests passed successfully!'
        }

        failure {
            echo 'Playwright tests failed!'
        }
    }
}