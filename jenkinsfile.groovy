// /* pipeline 변수 설정 */
// def app

// node {
//     def dockerId = "och5351"
//     def dockerRepo = "expresstest"
//     def DATE = new Date();
//     // github으로부터 소스 다운하는 stage
//     stage('Checkout') {
//             checkout scm   
//     }
 
//     // windows pm인 chocolately 를 활용 하여 nodejs 설치 및 준비 stage
//     stage('Build'){  
//         bat "choco install nodejs-lts -y"
//         // sh "echo 'Ready to build'"
//         // mvnHome = tool 'Maven 3.6.0'
//         bat "npm audit fix"
//         bat "npm install"
//         bat "npm build"
//     }
    
    
//     /*
//     //sonarqube 정적분석 실행하는 stage, jenkins와 sonarqube연동을 하지 않았다면 이부분은 주석처리
//     stage('Static Code Analysis') {  
//         sh "'${mvnHome}/bin/mvn' clean verify sonar:sonar -Dsonar.projectName=pipeline_test -Dsonar.projectKey=pipeline_test -Dsonar.projectVersion=$BUILD_NUMBER"
//     }
//     */

//     //dockerfile기반 빌드하는 stage ,git소스 root에 dockerfile이 있어야한다
//     stage('Build docker image'){   
//         app = docker.build("${dockerId}/${dockerRepo}")
//     }

//     //docker image를 push하는 stage, 필자는 dockerhub에 이미지를 올렸으나 보통 private image repo를 별도 구축해서 사용하는것이 좋음
//     //docker.withRegistry에 dockerhub는 앞서 설정한 dockerhub credentials의 ID이다.
//     stage('Push image') {   
//         docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
//             app.push("${env.BUILD_NUMBER}")
//             app.push("latest")
//         }
//         bat "docker rmi registry.hub.docker.com/${dockerId}/${dockerRepo}:${env.BUILD_NUMBER}"
//     }
     
//     // kubernetes에 배포하는 stage, 배포할 yaml파일(필자의 경우 test.yaml)은 jenkinsfile과 마찬가지로 git소스 root에 위치시킨다.
//     // kubeconfigID에는 앞서 설정한 Kubernetes Credentials를 입력하고 'sh'는 쿠버네티스 클러스터에 원격으로 실행시킬 명령어를 기술한다.
//     stage('Kubernetes deploy') {
//         //kubernetesDeploy configs: "k8s", 
//         kubeconfigId: 'och_k8s'
//         //bat "kubectl --kubeconfig=C:/jenkins_k8s/config get no"
//         bat "kubectl --kubeconfig=C:/jenkins_k8s/config apply -f k8s/"
        
//     }
    
//     stage('Complete') {
//         bat "echo 'The end'"
//     }
// }

/*
/*
   * jenkins podtemplete document
     * https://www.jenkins.io/doc/pipeline/steps/kubernetes/#podtemplate-define-a-podtemplate-to-use-in-the-kubernetes-plugin
   * 예제 Groovy code 
     * https://tech.osci.kr/2019/11/21/86026733/
     test
*/
podTemplate(label: 'jenkins-slave-pod',  //jenkins slave pod name
  containers: [
    containerTemplate(
      name: 'git', // container 에 git 설정
      image: 'alpine/git',
      command: 'cat',
      ttyEnabled: true
    ), 
    containerTemplate(
      name: 'node', // container 에 node 설정
      image: 'node:14.18-alpine3.11',
      command: 'cat',
      ttyEnabled: true
    ),
    containerTemplate(
      name: 'docker',
      image: 'docker',
      command: 'cat',
      ttyEnabled: true
    ),
    containerTemplate(
      name: 'kubectl', 
      image: 'bitnami/kubectl:1.21.5', 
      command: 'cat', 
      ttyEnabled: true
    ),
  ],
  volumes: [ 
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'), 
  ]
)

{
    node('jenkins-slave-pod') {  // 상위에 node 작성 'jenkins-slave-pod' 
        def dockerId = "och5351"
        def dockerRepo = "expresstest"
        def DATE = new Date();
        // def DOCKER_IMAGE_NAME = "och5351/kubernetes_test"           // 생성하는 Docker image 이름
        // def DOCKER_IMAGE_TAGS = "test_app"  // 생성하는 Docker image 태그
        // def USERNAME = "och5351"
        
        // jenkins Clone Stage는 Jenkins 내부에서 구현
        stage('Clone repository') {
            container('git') {
                // https://gitlab.com/gitlab-org/gitlab-foss/issues/38910
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/devlop']],
                    userRemoteConfigs: [
                        [url: 'https://github.com/och5351/Backend.git']//, credentialsId: 'gitlab-account']
                    ],
                ])
            }
        }
        
      
    }   
}