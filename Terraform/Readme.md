### Why Terraform ?

I used Terraform to provision the initial infrastructure, including EKS, ECR, and VPC, leveraging the official AWS EKS and VPC modules. The primary motivation for using Terraform was the need for repeated provisioning and teardown of infrastructure during development, which would have been time-consuming and error-prone if done manually. Additionally, automating infrastructure deployment helped optimize costs, as I could easily destroy resources when not in use and recreate them as needed, ensuring I only incurred charges while actively working.


### Commands used for set-up

#### Initializing the project and downloading the modules and providers
``` 
terraform init
```

#### To validate the syntax and formatting 
```
terraform fmt
terraform validate
```

#### To see what all changes will be performed 

```
terraform plan
```

#### To apply the configuration and changes
``` 
terraform apply
```
