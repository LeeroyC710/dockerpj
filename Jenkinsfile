ls
pwd
$(whoami)
docker --version
docker-comopse --version
docker-compose build
docker-compose push
				
ssh -t swarm-vm  << EOF
echo ssh-success
export ("$BUILD_NUMBER")
git clone https://github.com/LeeroyC710/dockerpj
cd dockerpj/
docker stack deploy --compose-file docker-compose.yaml dockerpj-app
EOF
