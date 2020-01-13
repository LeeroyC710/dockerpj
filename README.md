# Project
To create a service application that depends on three other services to function properly. In this case for this project created a service app that generates a random number and random letter and joins the two together to generate a random sentence (dare) in service3 pushing this feature on to the main service (service4).

*[Presentation](#presentation)
 
*[Brief](#brief)

*[Risk Assessment](#riskassessment)

*[Error Logs](#errorLogs)

*[Solution](#solution)

*[Delivered Solution](#deliveredsolution)

*[Service Architecture](#servicearchitecture)

*[Technology Used](#report)

*[Deployment](#Deployment)

*[Improvements for the future](#improve)

<a name="brief"></a>
## Project Brief
To create a service application that depends on three other services to function properly. In this case for this project created a service app that generates a random number and random letter and joins the two together to generate a random sentence (dare) in service3 pushing this feature on to the main service (service4).
The project name: Darephase - through its development it was designed to allow users to have access to a mini-game. The idea itself was generated from house games with friends and family and designed for fun. This project was built on docker container images and it runs on python langauage as the majority. 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/Trello.png)

<a name="risk assessment"></a>
## Risk Assessment
Before this project started I used trello to plan out on the direction of the project and also kept all logs updated whether it was errors and fixes made within the application itself. I also had to carry out extensive research on some topics i didn't quite understand in-order to meet the requirements of the services. Generated a few ideas from the start and started looking at the ones that were potentially approachable based on the topics covered during my training weeks. I also started doing a risk assessment of the project as i started building the application. 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/riskassessment.png)

<a name="errorlogs"></a>
## Error Logs
During the development stage and deployment stage there was some errors that would pop-up whilst attempting to build the app on docker compose and sometimes whilst running jenkins, some of these were easy fixes and some required some research in-house and also online in-order to resolve these without breaking more functions on the application. I used the error log to record these problems and noted some quick fixes that can still applied for future use in later development stages. 

Have a look at the error logs to see some of the errors that popped up. 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/Errorlogs.png)

<a name="solution"></a>
## Solution
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/deliveredsolution.png)
The project name: Darephase - through its development it was designed to allow users to have access to a mini-game.
The app itself is running on the MVP but however it is currently using 4 images (services) in order for it to function to its purpose. The app has been tested whilst being developed for example some services connections and outputs, Postman was used to check if each service was giving out the right output. 


<a name="Delivered solution"></a>
## Delievered Solution 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/DarePhase.png)
To produce this solution i had to use tools that go hand to hand with each stage of the development stage. The solution is based on flask-app service with 3 services working with the frontend which is service4 in this case.  

<a name="service architecture"></a>
### Service Architecture
Please check the service architecture in the documentation
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/ServiceArchitecture.png)

<a name="Technology used"></a>
### Technology Used
Here's a set of tools used for the project to come to a successful development: 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/TechnologyUsed.png)

<a name="Improvements for the future"></a>
### Improvements for the future
For the future built of this service I should make sure I allow enough time for more research on bug fixes and also ways to improve the service itself without any interruptions to the userability of the application service. That means enabling jenkins to auto-mate the full built of the full stack application allow replicas to act as clones whilst changes happen in the background. Below is a CI Pipeline of the improved process of the application as a service using Jenkins. 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/JenkinsCIPipeline.png)


