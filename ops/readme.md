## Developer Operations Engineer Take Home Challenge!

##### Using AWS free-tier only resources, create the following infrastructure using an IaC solution like Terraform:

1. Make a VPC with private/public subnets, routing/acl, IG, and security groups. 
1. Add an EC2 bastion server with a keyfile we can use to access the VPC resources below. Note: you can provide the keyfile to us using onetimesecret.com or any secret sharing service.
1. Create an ECS solution with load balancer, service, task, task definition, image repository. 
1. Host a basic Apache site with a simple index.html file that says `hello!`.
1. Provide **unambiguous** instructions for accessing the container via SSH so we can make text modifications to the index.html `hello pico!` and save them.
1. Submit your final Terraform solution as a GitHub repository.

## Extra credit: 
Use ACM and host the solution over https.  
Use Terraform Cloud free tier for your IaC solution.  
Use blue/green migrations in ECS.
