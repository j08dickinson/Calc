pipeline {
    agent any
    triggers {
    	cron('*****')
    }
    stages {
        stage("Unittest") {
            steps {
                sh "python3 test.py"
            }
        }
    }
}
