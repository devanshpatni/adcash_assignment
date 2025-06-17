helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm upgrade prometheus-agent prometheus-community/kube-prometheus-stack   --namespace prometheus-agent   --create-namespace   -f value-prom.yml
helm upgrade --install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace -f values-ingress.yaml