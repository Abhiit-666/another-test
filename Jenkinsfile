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
          build 'testadd'
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
