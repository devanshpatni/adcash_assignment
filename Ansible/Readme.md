### Why Ansible?

Ansible was used to configure Prometheus and Grafana on a central EC2-based monitoring server. Unlike Terraform, which excels at provisioning infrastructure, Ansible is better suited for in-instance configuration tasks—hence its use here. I used official Prometheus and Grafana collections to automate key setup stages like installing packages, configuring services, starting them, and managing their configuration files. This avoided the complexity of writing all tasks manually. I also set the Grafana admin credentials and enabled the remote write feature in Prometheus to allow metric ingestion from remote Prometheus agents.

### Brief Description of Project Files

- group_vars/all.yml → Contains global variables accessible to all hosts in the Ansible inventory.
- group_vars/monitoring.yml → Defines variables specific to hosts in the monitoring group only.
- roles/aws_provision → Contains tasks for provisioning the EC2 instance and adding its IP to the monitoring group for Prometheus and Grafana setup.
- roles/monitoring_setup → Handles the configuration of Prometheus and Grafana on the provisioned EC2 instance. It also manages security group rules to expose the Grafana dashboard publicly and restrict Prometheus access to the private EKS IP.
- ansible.cfg → Ansible’s global configuration file.
- requirements.yml → Lists the Ansible collections required to run configuration tasks (e.g., Prometheus and Grafana roles).
- setup.yml → The main playbook that orchestrates the full setup process end-to-end.

### Commands used for set-up

#### Downloading the requiremnets
```
ansible-galaxy collection install -r requirements.yml
```

#### Running the Setup
```
ansible-playbook setup.yml
```

#### Note
Update all missing variable values and file paths according to your specific environment before execution. 
