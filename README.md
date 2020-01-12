# Project
To create a service application that depends on three other services to function properly. In this case for this project created a service app that generates a random number and random letter and joins the two together to generate a random sentence (dare) in service3 pushing this feature on to the main service (service4).

*[Presentation](#presentation)
 
*[Brief](#brief)

*[Solution](#solution)
*[Delivered Solution](#delivered solution)

*[Testing](#testing)
*[Report](#report)

*[Deployment](#Deployment)

*[Improvements for the future](#improve)

<a name="brief"></a>
## Project Brief
To create a service application that depends on three other services to function properly. In this case for this project created a service app that generates a random number and random letter and joins the two together to generate a random sentence (dare) in service3 pushing this feature on to the main service (service4).
The project name: Darephase - through its development it was designed to allow users to have access to a mini-game. The idea itself was generated from house games with friends and family and designed for fun. This project was built on docker container images and it runs on python langauage as the majority. 

<a name="solution"></a>
### Solution
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/deliveredsolution.png)
The project name: Darephase - through its development it was designed to allow users to have access to a mini-game. The idea its
The app itself is running on the MVP but however it is currently using 4 images (services) in order for it to function to its purpose. The app has been tested whilst being developed for example some services connections and outputs, Postman was used to check if each service was giving out the right output.  
###Delievered Solution 
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/DarePhase.png)
The ER diagrams show a relation between the two tables, although this is functional the user is able to navigate between the account page, events and home page. The user_id is also foreignkey in the event table as it triggers the creation and of events in the table, users are not able to use this feature unless they log in or are registered. 

<a name="mla"></a>
### Service Architecture
Please check the service architecture in the documentation
![alt text](https://github.com/LeeroyC710/dockerpj/blob/master/documentation/ServiceArchitecture.png)
