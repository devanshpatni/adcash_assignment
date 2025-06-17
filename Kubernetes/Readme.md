# Commands used for set-up

### Basic Flow inside Kubernetes
![alt text](image.png)

#### Short Description of files

- ingress-prometheus-installation.sh -> Script for installing and configuring Nginx Ingress and Premetheus Agent.
- ingress-webapp-service.yaml -> Ingress Service for our webapplication having path based routings.
- prom-servicediscovery.yaml -> Service Monitor for discovering the services and scaping the metrics from /metrics endpoint. 
- values-ingress.yaml -> Custom configurations for nginx ingress controller. 
- values-prom.yaml -> Custom configurations for Prometheus agent.  
- webapp-deployment.yaml -> Main deployemnt file for deploying the webapplication and CLusterIP service for the deployment.
  
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
