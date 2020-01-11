pipeline{
	agent any

	stages{
		
		
        	stage('--docker-compose build and push--'){
			steps{
                    		sh '''ssh -t jenkins@docker-jenkins  << leeroy
                           	cd dockerpj/
                           	docker-compose up -d --build
                           	docker-compose down 
                           	docker-compose push
				
                           	'''
            
            		}
        	}
        	stage('--Deploy services--'){
			steps{
				sh '''ssh -t jenkins@docker-jenkins  << leeroy
                       		cd dockerpj/
                       		docker stack deploy docker-compose.yaml  
				
				'''
			}
		}
	}
}
