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
    slackSend (channel: "${slack_channel}", color: '#FFFF00', message: "CI/CD 를 실행합니다. \n 작업 : '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}

/* Slack 도커 알람 함수 */
def notifyDocker(slack_channel) {
    slackSend (channel: "${slack_channel}", color: '#FFFF00', message: "도커 이미지 빌드/푸쉬를 실행합니다. \n 작업 : '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}

/* Slack 베포 알람 함수 */
def notifyDeployment(slack_channel) {
    slackSend (channel: "${slack_channel}", color: '#FFFF00', message: "배포를 실행합니다. \n 작업 : '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}

/* Slack 성공 알람 함수 */
def notifySuccessful(slack_channel) {
    slackSend (channel: "${slack_channel}", color: '#00FF00', message: "CI/CD를 완료 하였습니다. \n 작업 : '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
}
/* Slack 실패 알람 함수 */
def notifyFailed(slack_channel) {
  slackSend (channel: "${slack_channel}", color: '#FF0000', message: "CI/CD를 실패 하였습니다. \n 작업 : '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
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
    containerTemplate(
      name: 'kubectl', 
      image: 'lachlanevenson/k8s-kubectl:v1.21.5', 
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
      try {
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
          notifyDocker(SLACK_CHANNEL)
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
        // kubernetes에 배포하는 stage, 배포할 yaml파일(필자의 경우 test.yaml)은 jenkinsfile과 마찬가지로 git소스 root에 위치시킨다.
        // kubeconfigID에는 앞서 설정한 Kubernetes Credentials를 입력하고 'sh'는 쿠버네티스 클러스터에 원격으로 실행시킬 명령어를 기술한다.
        stage('Kubernetes deploy') {
          notifyDeployment(SLACK_CHANNEL)
          container('kubectl') {
              sh "kubectl apply -f k8s/"
          }
        }
        notifySuccessful(SLACK_CHANNEL)
      } catch(e) {
        /* 배포 실패 시 */
        currentBuild.result = "FAILED"
        notifyFailed(SLACK_CHANNEL)
    }
  }
}