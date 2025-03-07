pipeline {
    agent any
    triggers {
    	pollSCM('* * * * *')
    }
    stages {
        stage("Unittest") {
            steps {
                sh "python3 test.py"
            }
        }
    }
}
