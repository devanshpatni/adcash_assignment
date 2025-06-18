### Why Kubenetes ?
I have used Kubernetes to deploy my application, leveraging its powerful container orchestration capabilities to manage and scale containerized workloads efficiently. Specifically, I deployed the application on AWS Private EKS, which provides a secure and managed Kubernetes control plane. Using a private EKS cluster enhances security by restricting public internet access to worker nodes, thereby minimizing the attack surface and ensuring all communication stays within the VPC.

For deployment, I used the Deployment resource in Kubernetes to ensure features like replica management, rolling updates, and automated pod restarts in case of failures. I implemented readiness and liveness probes to monitor application health—automatically replacing unhealthy pods when necessary.
To expose the application externally, I set up an NGINX Ingress Controller with a public Network Load Balancer (NLB), enabling secure and efficient path-based routing via Kubernetes Ingress resources.
Additionally, I deployed a Prometheus Agent on the cluster to scrape metrics from the application and remote write them to a centralized Prometheus server. These metrics are then visualized through a Grafana dashboard, providing real-time monitoring and observability.

### Basic Flow inside Kubernetes
![image](https://github.com/user-attachments/assets/fcf67d38-b5f6-473c-bccf-b7ec9d8b3c43)


#### Brief Description of Project Files

- ingress-prometheus-installation.sh -> Script for installing and configuring Nginx Ingress and Premetheus Agent.
- ingress-webapp-service.yaml -> Ingress Service for our webapplication having path based routings.
- prom-servicediscovery.yaml -> Service Monitor for discovering the services and scaping the metrics from /metrics endpoint. 
- values-ingress.yaml -> Custom configurations for nginx ingress controller. 
- values-prom.yaml -> Custom configurations for Prometheus agent.  
- webapp-deployment.yaml -> Main deployemnt file for deploying the webapplication and CLusterIP service for the deployment.

### Commands used for set-up

#### For webapp and service deployment 
``` kubectl apply -f webapp-deployment-service.yaml  ```

#### For installing NGINX Ingress Controller and Prometheus-Grafana
```
chmod 755 ingress-prometheus-installation.sh
./ingress-prometheus-installation.sh

```

#### For deploying ingress configurations webapp application path based routing

``` kubectl apply -f ingress-webapp-service.yaml ```

#### For service discovery for prometheus to scrape metrics
 ``` kubectl apply -f prom-servicediscovery.yaml ```

#### Note
Update all missing variable values and file paths according to your specific environment before execution.
