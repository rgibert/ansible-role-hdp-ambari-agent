HDP Ambari Agent
================

Installs and configures Ambari agent

Requirements
------------

- none

Role Variables
--------------

| Variable | Default | Definition |
|----------|---------|------------|
| ambari_version | 2.5.2.0 | |
| ambari_agent_user | root | |
| ambari_agent_group | root | |
| ambari_agent_log_dir | /var/log/ambari-agent | |
| ambari_agent_log_level | INFO | |
| ambari_server_host | localhost | |
| ambari_server_port | 8440 | |
| ambari_server_secure_port | 8441 | |

Dependencies
------------

- none

Example Playbook
----------------

```
- hosts:
    - servers
  roles:
    - hdp-ambari-agent
```

License
-------

GPLv3

Author Information
------------------

Richard Gibert
<richard@gibert.ca>
