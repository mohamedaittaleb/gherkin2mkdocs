node('jenkins_slave') {
    stage('Checkout') {
        checkout scm
    }

    stage("convert from .feature to .md"){
        dir("project/src/test/resources") {
            sh "/usr/local/bin/gherkin2markdown features docs"
        }
    }

    stage(" generate mkdocs.yml file"){
        dir("project/src/test/resources") {
            sh "echo \"## Index \"> docs/index.md"
            sh "python generate-mkdocs-yml.py"
        }
    }
    stage('Build Mkdocs Site') {
        sh "pip install mkdocs --user"
        sh "pip install mkdocs-material --user"
        dir("project/src/test/resources") {
            sh "/home/jenkins/.local/bin/mkdocs build"
        }
    }
}

