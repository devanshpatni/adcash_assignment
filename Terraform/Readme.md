### Why Terraform ?

I used Terraform to provision the initial infrastructure, including EKS, ECR, and VPC, leveraging the official AWS EKS and VPC modules. The primary motivation for using Terraform was the need for repeated provisioning and teardown of infrastructure during development, which would have been time-consuming and error-prone if done manually. Additionally, automating infrastructure deployment helped optimize costs, as I could easily destroy resources when not in use and recreate them as needed, ensuring I only incurred charges while actively working.

### Brief Description of Project Files

- main.tf –> Contains the core configuration for provisioning AWS resources such as EKS, VPC, and ECR.
- provider.tf –> Defines the AWS provider settings required for Terraform to interact with the AWS environment.
- variables.tf –> Declares the input variables used across Terraform modules, promoting reusability and parameterization.
- terraform.tfvars –> Specifies the values for input variables; users can modify this file to customize deployments without changing the main configuration files.

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

#### Note
Update all missing variable values and file paths according to your specific environment before execution.

