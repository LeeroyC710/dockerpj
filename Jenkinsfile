pipeline {
          agent any
	  
	  stages{
                stage('--Test1--'){
                        steps{ 
		                 sh '''cd qa-portal-services/ 		
                                       mvn clean install -DskipTests
				       cd ..
                                       docker-compose build 
                                       docker-compose push
				       ssh -i "docker-key.pem" ubuntu@ec2-00.00.000.00.eu-west-2.compute.amazonaws.com << EOF
				       docker stack deploy --compose-file=docker-compose.yaml
				       '''
                            }
                 } 
                stage('--Clean up--'){
                        steps{
                                 sh '''ssh -i "docker-key.pem" ubuntu@ec2-00.00.00.00.eu-west-2.compute.amazonaws.com << EOF
                                       docker system prune -f
                                       '''
                            }
                  }
	 }
}
