# Assignment

## High-Level Flow Diagram
 ![image](https://github.com/user-attachments/assets/6f4f6159-5393-401f-b254-7dc100a652bc)
## Technologies Used
 1. Python - Development using Flask.
 2. AWS - Cloud infrastructure using EKS, ECR, and VPC.
 3. Terraform -  Infrastructure as Code (IaC) for deploying cloud resources.
 4. Docker - Containerization of the application
 5. Elastic Kubernetes Service (EKS) - Container orchestration and deployment.
 6. Ansible - For autometic resource deployment and server configurations. 
 7. Prometehus and Grafana -  Monitoring, observability, and metrics visualization.

##  Highlights of Each Technology Used.
 **Note** - Each folder documents the rationale behind the technology used, along with key files and essential commands.

### Python 
- Developed a lightweight web application using Flask.
- Implemented two endpoints: /gandalf and /colombo, each rendering custom HTML templates
- Integrated Prometheus for metrics instrumentation and export.

### Terraform 
- Automated the provisioning of infrastructure components: VPC, EKS, and ECR.
- Enabled quick and consistent creation/deletion of environments, saving time and cost.
- Utilized official Terraform modules for EKS and VPC to simplify deployment.

### Docker
- Containerized the Flask web application using Docker.
- Implemented a multi-stage build process to reduce image size.
- Used a distroless Python image to minimize the attack surface and improve security.

### Kubernetes
- Deployed the application to a private AWS Elastic Kubernetes Service (EKS) cluster.
- Used Deployment kind as for getting self-healing, scaling, and rollout management.
- Configured an NGINX Ingress Controller for path-based routing with an external public Network Load Balancer.
- Set up Prometheus Agent and Service Discovery within the cluster for scraping and sending custom metrics from application to central prometheus server.

### Ansible
- Used to automate the deployment and configuration of the Prometheus server on an EC2 instance.
- Configured Prometheus to receive remote write metrics from the Kubernetes-based Prometheus Agent.
- Set up Grafana for visualizing metrics, including user credentials and dashboards.
  
### Prometheus and Grafana
- Enabled Prometheus Agent with service discovery to automatically collect metrics from application services running in EKS.
- Configured remote write to forward the scraped metrics to a centralized Prometheus server.
- Created a custom Grafana dashboard to visualize request counts per endpoint.

##  Task Access or Additional Notes

### Webapp is available on - http://3.110.241.151/
   #### /gandalf
   ![image](https://github.com/user-attachments/assets/96375ae9-daf7-47bc-a662-31d35370bef0)

   #### /colombo
   ![image](https://github.com/user-attachments/assets/3ae48381-9d60-48a3-98ca-bd7945ea78b3)

   
### Graphana Dashboard is available on - http://13.233.164.36:3000/
![image](https://github.com/user-attachments/assets/3b4df12c-7697-4e28-9f9f-aa7f2a48b821)

