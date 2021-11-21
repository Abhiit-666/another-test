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
          buil 'testadd'
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
