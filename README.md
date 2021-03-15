# RoboticBase example: UoA PoC 3


## Getting Started
### Start UoA-PoC3 on Azure AKS

### Start UoA-PoC3 on Minikube
1. Set the password of MQTT user in the following yaml file:
    * [group\_vars/all.yml](ansible/group_vars/all.yml)
1. If necessary, update the values defined in the following yml files:
    * [inventories/minikube/group\_vars/minikube.yml](ansible/inventories/minikube/group_vars/minikube.yml)
    * [inventories/minikube/host\_vars/localhost.yml](ansible/inventories/minikube/host_vars/localhost.yml)
1. Start "pipenv shell"

    ```
    $ pipenv shell
    ```
1. Start RoboticBase/core on minikube using ansible

    ```
    $ ansible-playbook -i inventories/minikube --extra-vars="ansible_python_interpreter=$(which python)" minikube.yml
    ```

1. 


## License

[Apache License 2.0](/LICENSE)

## Copyright
Copyright (c) 2018-2020 [TIS Inc.](https://www.tis.co.jp/)
