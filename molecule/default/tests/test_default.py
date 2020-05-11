import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


# Example for files existence
@pytest.mark.parametrize(
    "path",
    [
        ("/etc/hosts"),
        # ("/etc/redhat-release"),
        # ("/etc/sysctl.conf"),
        ("/etc/resolv.conf"),
    ],
)
def test_files_exists(host, path):
    f = host.file(path)
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


# Example for installed packages
def test_package_installed(host):
    p = host.package("bash")
    assert p.is_installed


# Example for running services
# Be careful that
# - service & systemctl command aren't installed in CentOS / RHEL basic containers
# - testing systemd service doesn't work out of the box, you need to have a systemd-ready container like centos/systemd
def test_service_is_running(host):
    if (
        host.system_info.distribution in ["centos", "redhat"]
        and int(host.system_info.release[0]) < 7
    ):
        s = host.service("network")
    else:
        s = host.service("systemd-journald")
    assert s.is_running
    assert s.is_enabled
