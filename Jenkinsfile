pipeline {
    agent any

    stages {

        stage('Deploy Frontend') {
            steps {
                sh 'sudo cp -r frontend/* /var/www/html/'
            }
        }

        stage('Deploy Backend') {
            steps {
                sh 'pip3 install -r backend/requirements.txt --break-system-packages'
                sh 'pkill -f app.py || true'
                sh 'nohup python3 backend/app.py > backend.log 2>&1 &'
            }
        }
    }
}
