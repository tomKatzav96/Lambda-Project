pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh './tests/unit_test_by_branch.sh $BRANCH_NAME'
            }
        }
        stage('update lambda') {
            steps {
                sh './deployment/deploy_by_branch.sh $BRANCH_NAME'
            }
        }
    }
}