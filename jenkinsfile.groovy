// /* pipeline 변수 설정 */
// def app

// node {
//     def dockerId = "och5351"
//     def dockerRepo = "expresstest"
//     def DATE = new Date();

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

// Pipeline 변수 
def dockerId = "och5351"
def dockerRepo = "expresstest"
def SLACK_CHANNEL = "develop-deployment-alarm"
def DATE = new Date();

/* Slack 시작 알람 함수 */
def notifyStarted(slack_channel) {
    slackSend (channel: "${slack_channel}", color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}
/* Slack 성공 알람 함수 */
def notifySuccessful(slack_channel) {
    slackSend (channel: "${slack_channel}", color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}
/* Slack 실패 알람 함수 */
def notifyFailed(slack_channel) {
  slackSend (channel: "${slack_channel}", color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}

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
    // containerTemplate(
    //   name: 'kubectl', 
    //   image: 'bitnami/kubectl:1.21.5', 
    //   command: 'cat', 
    //   ttyEnabled: true
    // ),
  ],
  volumes: [ 
    hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock'), 
  ]
)

{
    node('jenkins-slave-pod') {  // 상위에 node 작성 'jenkins-slave-pod' 
        // Start
        stage('Start'){
          notifyStarted(SLACK_CHANNEL)
        }

        // git clone 스테이지
        stage('Clone repository') {
          container('git') {
              checkout scm
          }
        }
        // node build 스테이지
        stage('node build') {
          container('node') {
              sh "npm audit fix"
              sh "npm install"
              sh "npm build"
          }
        }
        // docker image build 스테이지
        stage('docker build') {
          container('docker') {
              app = docker.build("${dockerId}/${dockerRepo}")
          }
        }
        //docker.withRegistry에 dockerhub는 앞서 설정한 dockerhub credentials의 ID이다.
        stage('Push image') {   
          container('docker') {
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                app.push("${env.BUILD_NUMBER}")
                app.push("latest")
            }
            sh "docker rmi registry.hub.docker.com/${dockerId}/${dockerRepo}:${env.BUILD_NUMBER}"
          }
      }

      notifySuccessful(SLACK_CHANNEL)
    } catch(e) {
      /* 배포 실패 시 */
      currentBuild.result = "FAILED"
      notifyFailed(SLACK_CHANNEL)
    }
}