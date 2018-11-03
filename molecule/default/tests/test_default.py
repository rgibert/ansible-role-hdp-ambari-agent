import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user(host):
    assert host.user('ambari').exists


def test_group(host):
    assert host.group('ambari').exists


def test_installed(host):
    pkg = host.package('ambari-agent')
    assert pkg.is_installed


def test_service(host):
    pkg = host.service('ambari-agent')
    assert pkg.is_running
    assert pkg.is_enabled


def test_config_file(host):
    f = host.file('/etc/ambari-agent/conf/ambari-agent.ini')
    assert f.contains('ambari-agent')
    assert f.user == 'ambari'
    assert f.group == 'ambari'
    assert f.mode == 0o644
