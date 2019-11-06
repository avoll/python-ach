pipeline {
    agent {
        dockerfile {
            filename "Dockerfile"
            args "-u root"
        }
    }

    environment {
        PYTHONDONTWRITEBYTECODE = 1
    }

    stages {
        stage("Test") {
            steps {
                script {
                    sh "poetry run py.test"
                }
            }
        }
        stage("Publish Wheel") {
            when {
                branch "master"
            }
            environment {
                NEXUS = credentials("jenkins-internal-nexus")
                REPO = "https://nexus.earnup.com/repository/PyPI-Internal/"
            }
            steps {
                script {
                    sh "poetry build -f wheel"
                    sh "poetry config repositories.earnup $REPO"
                    sh "poetry publish -r earnup -u $NEXUS_USR -p $NEXUS_PSW"
                }
            }
        }
    }
}
