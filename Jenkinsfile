#!/usr/bin/env groovy

node {

  stage('Checkout') {
    checkout scm
  }

  stage('Build') {
    docker.image('zenoss/build-tools:0.0.10').inside() { 
      sh '''
        make clean
        make
      '''
    }
  }

  stage('Publish') {
    def remote = [:]
    withFolderProperties {
      withCredentials( [sshUserPrivateKey(credentialsId: 'PUBLISH_SSH_KEY', keyFileVariable: 'identity', passphraseVariable: '', usernameVariable: 'userName')] ) {
        remote.name = env.PUBLISH_SSH_HOST
        remote.host = env.PUBLISH_SSH_HOST
        remote.user = userName
        remote.identityFile = identity
        remote.allowAnyHosts = true

        def tar_ver = sh( returnStdout: true, script: ''' awk -F"'" '/^version/{print $2}' setup.py ''' ).trim()
        sshPut remote: remote, from: 'dist/zenoss.extjs-' + tar_ver + '.tar.gz', into: env.PUBLISH_SSH_DIR
      }
    }
  }

}