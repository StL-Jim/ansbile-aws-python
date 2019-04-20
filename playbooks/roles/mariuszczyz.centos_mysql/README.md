# CentOS 7 MySQL Installation and Configuration Role

MySQL server installation role for CentOS 7. It installs and configures the latest version of MariaDB. 

The included configuration file is tweaked for low resources servers with limited available memory, less than 2 GB.

## Requirements

None.

## Role Variables

In `vars/secret-vault.yml`

`MYSQL_ROOT_PASSWORD` - set this to your own mysql root password, this file is meant to be vaulted.

## Dependencies

None.

## Example Playbook

Fetch this role from Ansible Galaxy:

`ansible-galaxy install mariuszczyz.centos-mysql`

In playbook.yml:

```bash
- hosts: servers
  roles:
    - { role: mariuszczyz.centos-mysql, tags: ['centos-mysql'] }
```

## License

BSD

## Author Information

Author: Mariusz Czyz  

Date: 10/2018
