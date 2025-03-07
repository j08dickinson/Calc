pipeline {
    agent any
    triggers {
    	cron('1****')
    }
    stages {
        stage("Unittest") {
            steps {
                sh "python3 test.py"
            }
        }
    }
}
