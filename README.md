# To setup the infrastructure 

## Go to the vagrant folder

Start the 3 VMs (One master, 2 workers) using `vagrant up`.

Then provide the ssh info to ansible with: `vagrant ssh-config > vagrant-ssh`.

Your 3 VMs should be up and running.

## Move to kubernetes-cluster folder

Make sure ansible is installed locally (with pip). 

Then, to setup your machines, move to the ansible folder and: 

1. `ansible-playbook -i inventory/hosts.yml playbooks/bootstrap.yml -vv` to ensure python and sudo are installed.
2. `ansible-playbook -i inventory/hosts.yml playbooks/common.yml -vv` to do the following:
    1. Install base system tools
    2. Configure the VMs to host k8s
    3. Install the node-exporters
3. `ansible-playbook -i inventory/hosts.yml playbooks/master.yml -vv` to configure the master node:
    1. Init the node & cluster
    2. Install flannel
    3. Install etcd
4. `ansible-playbook -i inventory/hosts.yml playbooks/worker.yml -vv` to make the worker nodes join the cluster

## Finally, move to the monitoring folder

Start the monitoring stack (Prometheus+Grafana) by a simple `docker compose up` (within the docker folder)



