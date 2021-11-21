pipeline{
  agent any
    stages{
    
    stage('build'){
      steps{
        script{
          build 'add'
          
        }
      }
    }
    stage('test'){
      
      steps{
        script{
          buil 'addtest'
      }
    }
    }
    stage('deploy'){
      steps{
        script{
          echo"deploying"
        
      }
     }
    }
  }
}
