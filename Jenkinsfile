#!/usr/bin/env groovy

pipeline {
  agent none

  options {
    timeout(time: 30, unit: 'MINUTES')
  }

  triggers {
    cron('H 3 * * *')
  }

  environment {
    GMT_HTTP_PORT = "18080"

    PARTICLES_URL = "https://github.com/radon-h2020/radon-particles.git"
    PARTICLES_BRANCH = "master"
    PARTICLES_DIR = "radon-particles"
    PARTICLES_EXPORT_URL = "http://127.0.0.1:${GMT_HTTP_PORT}/winery/servicetemplates"

    CTT_DOCKER_NAME = "RadonCTT"
    CTT_DOCKER_ORG = "radonconsortium"
    CTT_DOCKER_REPO = "radon-ctt"
    CTT_DOCKER_FQN = "${DOCKER_ORG}/${DOCKER_REPO}"
    CTT_PORT = "18080"
    CTT_PORT_EXT = "7999"
  }

  stages {
    stage('Set up and start GMT') {
      agent any
      steps {
        sh "docker-compose pull"
        sh "rm -rf ${PARTICLES_DIR}"
        sh "git clone --single-branch --branch ${PARTICLES_BRANCH} ${PARTICLES_URL} ${PARTICLES_DIR}"
        sh "chmod -R a+rwx ${PARTICLES_DIR}"
        sh "docker-compose up -d"
        sh "sleep 30"
      }
    }

    stage('Obtain SUT Service Templates') {
      matrix {
	      agent any
	      axes {
	        axis {
	          name 'SERVICE_TEMPLATE'
           values 'SockShopTestingExample', 'ThumbnailGeneration'
	        }
	      }
      	stages {
	        stage('Query Service Template') {
	          environment {
	            CSAR = "SUT_${SERVICE_TEMPLATE}.csar"
	          }
	          steps {
	            sh "curl -H 'Accept: application/xml' -o \"${CSAR}\" \"${PARTICLES_EXPORT_URL}/radon.blueprints/${SERVICE_TEMPLATE}/?yaml&csar\""
	            stash name: "${SERVICE_TEMPLATE}", includes: "${CSAR}"
	          }
	        }
	      }
      }
    }
	
    stage('Obtain TI Service Templates') {
      matrix {
        agent any
        axes {
          axis {
            name 'SERVICE_TEMPLATE'
            values 'JMeterMasterOnly', 'DeploymentTestAgent'
          }
        }
        stages {
          stage('Query Service Template') {
            environment {
              CSAR = "TI_${SERVICE_TEMPLATE}"
            }
            steps {
              sh "curl -H 'Accept: application/xml' -o \"${CSAR}\" \"${PARTICLES_EXPORT_URL}/radon.blueprints.testing/${SERVICE_TEMPLATE}/?yaml&csar\""
              stash name: "${SERVICE_TEMPLATE}", includes: "${CSAR}"
            }
          }  
        }
      }
    }
    
    stage('Stop GMT and Clean up') {
      steps {
        sh "docker-compose -fsv"
        sh "rm -rf ${PARTICLES_DIR}"
      }
    }
  }
}

