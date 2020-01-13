pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t jenkins@swarm-vm  << EOF
				git clone https://github.com/LeeroyC710/dockerpj.git
				
                           	cd dockerpj/
                           	docker-compose up -d --build
                           	docker-compose down 
                           	docker-compose push
				
                           	'''
            
            		}
        	}
        	stage('--Deploy services--'){
			steps{
				sh '''ssh -t jenkins@swarm-vm  << EOF
                       		cd dockerpj/
                       		docker stack deploy docker-compose.yaml  
				
				'''
			}
		}
	}
}
