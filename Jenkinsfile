pipeline {
    agent Any
    environemnt {
        Docker_name: "alvinselva/nginx:latest"
        Docker_credentials: "dock-cred"
        K8s_credentials: "k8s-cred"
    }

    stages{
        stage("Code checkout") {
            step{
                sh "git clone: <url>"
            }
        }
    }
    stages{
        stage("Docker build") {
            step{
                script {
                    sh "docker build -t ${Docker_name}:${git_commit} ."
                }
            }
        }
    }

    stages{
        stage("Image Scan") {
            step{
                script {
                    sh "trivy scan --format table -o scan.html --severity CRETICAL, HIGH ${Docker_name}:${git_commit}"
                }
            }
        }
    }

    stages{
        stage("Docker Push") {
            step{
                script {
                    credentials = ${Docker_credentials("dock-cred")}
                    docker push ${Docker_name}:${git_commit}
                }
            }
        }
    }

    stages{
        stage("Deploy to k8s") {
            step{
                script {
                    sh """
                    credentials = ${k8s_credentials("k8s-cred")}
                    kubectl apply -f deployment.yaml
                    kubectl apply -f svc.yaml
                    kubectl apply -f pvc.yaml
                    """
                }
            }
        }
    }

}