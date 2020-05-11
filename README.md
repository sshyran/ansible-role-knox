<p><img src="http://pngimg.com/uploads/skeleton/skeleton_PNG42642.png" alt="skeleton logo" title="graph" align="right" height="60" /></p>

# Ansible Role Template
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![pipeline status](https://gitlab.lmru.adeo.com/BI/dataplatform-infrastructure/role-template/badges/master/pipeline.svg)](https://gitlab.lmru.adeo.com/BI/dataplatform-infrastructure/role-template/commits/master)
[![IRC](https://img.shields.io/badge/dataplatformhq.slack.com-%23ansible-yellow.svg)](https://dataplatform-hq.slack.com/messages/CLM2NRTCL)

Ansible role template, template or boilerplate as you prefer. With Molecule + Testinfra tests enabled, Yamllint configured, Jenkins or Gitlab CI pipelines ready to go, to be cloned to get started on a new role.

## How to get started

Here's a TODO list to get started ASAP with you role development

- Clone this repo
- Open `create.sh` with your favorite editor
- Modify variables mentioned in that file
- Run `create.sh`

## Important notes

You may need to install and use following tools for best start ansible role development:
* [Molecule](https://molecule.readthedocs.io/en/stable/) - Tests runner
* [Ansible lint](https://github.com/ansible/ansible-lint) - Syntax check
* [Testinfra](https://github.com/philpep/testinfra) - Test converge
* [Goss](https://goss.rocks/) - Test converge
* [Tox](https://tox.readthedocs.io/en/latest/) - virtualenv management (test for py27,py3)

Test infrastructure:
* [Docker](https://www.docker.com/) - tests inside docker containers
* [Vagrant](https://www.vagrantup.com/) - tests inside VMs (virtualbox, vmware, etc)

Git:
* [Pre commit](https://pre-commit.com/) - git pre-commit hooks for run test before commit
* [Github changelog generator](https://github.com/skywinder/Github-Changelog-Generator) - generate CHANGELOG file properly


## Result

After running `create.sh` it will convert this repo into a directory structure with everything needed to start 
developing new DataPlatform ansible role. Next you may do the following:

- Write some tasks in `tasks/main.yml`
- Write [TestInfra](http://TestInfra.readthedocs.io/) validation tests in `molecule/default/tests/test_default.py`
- Remove `molecule/default/tests/__pycache__` if it exists
- Update platforms and roles dependencies lists in `meta/main.yml`
- If you've roles dependencies, rename `molecule/default/requirements.sample.yml` in `molecule/default/requirements.yml` and update its content
- Update platforms list in `molecule/default/molecule.yml`
- Plug CI/CD to automatically run molecule test. Either
  - Jenkins : create a new project copying https://jenkins.local/job/yourteam/job/ansible-role-template. Put your role's name, edit the repository URL (search for git@gitlab.local:rg/ansible-role-template.git and update it). And enable Jenkins@astjenkins deploy key in Gitlab project Settings / Repository / Deploy Keys
  - Gitlab CI : enable a gitlab runner for the gitlab project you're on. The `.gitlab-ci.yml` is enough to run molecule after each commit.
- Replace this `README.md` with a quick doc
- Push and wait for a mail about your pipeline first failure (of course it'll fail the first time.)


## Warnings

- Running `create.sh` deletes `.git` directory.
- README.md file is overwritten with ROLE_README.md

## Ansible tests with Molecule

[Molecule](http://molecule.readthedocs.io/) is a tool (a python library) specialized in testing Ansible role, usually applying them on docker container then running validation test with TestInfra (another python library).

### Install

See the inline provisionning script in file `Vagrantfile` for a scripted CentOS 7 installation

```bash
$provisionning = <<-PROVISIONNING
# This part
PROVISIONNING
```

Otherwise, you need the following

- Docker installed and ready to run https://docs.docker.com/install/
- Docker's python SDK https://pypi.org/project/docker/
- Latest ansible version installed. Which means Python 3.5 or above https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
- SELinux disabled. I couldn't find a working combination of Python 3.5 and libselinux-python. Another solution would be to use Debian / Ubuntu...
- Molecule installed : https://molecule.readthedocs.io/en/master/installation.html

### How it works

In this example repository, there's a `molecule` folder with a molecule `default` scenario folder. `molecule test` command will run this default scenario, aka those roughtly those steps : lint your Ansible role (in fact all the .yml and .py in this repository) taking in account `.yamllint` and `.flake8`, then create docker containers according to the `molecule.yml` platforms list and `Dockerfile.j2` template, install the required roles, apply this role to the containers, apply again to check idempotency, run validation tests via TestInfra (default library used, could be goland based Goss or ruby chef based Inspec). And cleanup after every success / fail.


### Roles requirements

Your Ansible role might requires other roles as defined in `meta/main.yml`. For molecule to install those before testing your role, create an ansible-galaxy requirement file at  `molecule/default/requirements.yml`, which may looks like

**Important** due to a bug described on [ansible side](https://github.com/ansible/ansible/issues/45475) and [gitlab's ](https://gitlab.com/gitlab-org/gitlab-ce/issues/50228), the `+`` in `gitlab+deploy-token-XX` should be replaced by `%2B`.

```yaml
---
- name: org.security
  src: git+https://gitlab%2Bdeploy-token-16:sBVJGCGCHGCHGCHGm6byho6@gitlab.local/rg/ansible-role-security.git
```

### Local test via Vagrant

The easiest way is to use Vagrant to boot a preconfigured CentOS VM. A `Vagrantfile` is provided in this repository, just follow the step to get started

- Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- Install [Vagrant](https://www.vagrantup.com/downloads.html)
- Open a command prompt in the repository local folder and run `vagrant up`
- Wait for it to be done starting & configuring & provionning, then `vagrant ssh`
- Once connected in the VM, testing molecule is `sudo su; cd /vagrant; molecule test`

### Test with a homemade VM

Otherwise you can install a Linux VM yourself. The requirements for molecule to work is

- Docker installed and ready to run https://docs.docker.com/install/
- Docker's python SDK https://pypi.org/project/docker/
- Latest ansible version installed. Which means Python 3.5 or above https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
- Molecule installed : https://molecule.readthedocs.io/en/master/installation.html

Once installed, get the role on the VM (git clone, or download zip...) then `molecule test`

Don't try to run this directly on Windows, you'll waste too much time setting it up.

### Gitlab runner test

Debugging a Gitlab CI pipeline, you can run molecule directly on the gitlab runner which just failed. Only for SysAdmin :-].

```bash
sudo updatedb
cd $(dirname $(locate virtenv | grep 'ansible-role-webenv' | egrep 'env$'))
source virtenv/bin/activate
molecule --debug test
```

## Known issues

Here's a quick list of errors happening often

### The output has been hidden, aka how to debug

```
failed: [localhost] (item=None) => {"censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result", "changed": false}
```

The only option without hacking molecule's hidden mechanics is to run `molecule --debug test`. It's very verbose, you might want to copy/paste the log in a file to use some "Ctrl-F error" or whatever.

### Gitlab runner / Jenkins slave can't git clone this repository

Might be that the git(lab) repository got an autosigned certificate. Run `git config --global http.sslVerify false` on the slave.

### Required roles can't install

```
[WARNING]: - org.repositories was NOT installed successfully: - command
git clone http://gitlab-ci-
token:-XXXXXXXXXXXXXX@gitlab.local/rg/ansible-role-
repositories.git org.repositories failed in directory /home/gitlab-
runner/.ansible/tmp/ansible-local-323273gxhdf1f61/tmpx4e6yr0t (rc=128)
ERROR! - you can use --ignore-errors to skip failed roles and finish processing the list.
```

Someone (vagrant or molecule or yourself) is trying to do a command alike `ansible-galaxy install -r requirements.yml`, which is failing. Either this specific gitlab token is invalid (can't authent with it) or once authentified the account doesn't have the right to read & clone the repository, or you're trying to clone in a directory where you can't write.

### Molecule can't build its image

```
TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item=None)
ok: [localhost] => (item=None)
ok: [localhost] => (item=None)
ok: [localhost] => (item=None)
ok: [localhost]

TASK [Build an Ansible compatible image] ***************************************
changed: [localhost] => (item=None)
changed: [localhost] => (item=None)
failed: [localhost] (item=None) => {"censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result", "changed": false}
failed: [localhost] (item=None) => {"censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result", "changed": false}
fatal: [localhost]: FAILED! => {"censored": "the output has been hidden due to the fact that 'no_log: true' was specified for this result", "changed": true}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=1


ERROR:
An error occured during the test sequence.  Cleaning up.
--> Scenario: 'default'
--> Action: 'destroy'
```

Most likely you specified a bad docker image for test in `molecule/default/molecule.yml`, or there's something wrong with `molecule/default/Dockerfile.j2`. Run `molecule --debug create` until you find what's the problem.

About the bad docker image, pay attention to the tag used. Say you want to fix the tag, centos:7.4 and centos:6.9. CentOS' docker images' tags are listed here https://hub.docker.com/r/library/centos/tags/ and as one can see, there's a 6.9 tag but no 7.4, instead there's a 7.4.WXYZ.

### Testing service doesn't work

In Molecule's verify step you might have this kind of issue

```
tests/test_default.py:37:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <service network>

    @property
    def is_running(self):
        return self.run_expect(
>           [0, 3], "systemctl is-active %s", self.name).rc == 0
E       AssertionError: Unexpected exit code 1 for CommandResult(command='systemctl is-active network', exit_status=1, stdout='', stderr='Failed to get D-Bus connection: Operation not permitted')
E       assert 1 in [0, 3]
E        +  where 1 = CommandResult(command='systemctl is-active network', exit_status=1, stdout='', stderr='Failed to get D-Bus connection: Operation not permitted').rc

../../virtenv/lib/python3.6/site-packages/testinfra/modules/service.py:106: AssertionError
===================== 3 failed, 12 passed in 86.68 seconds =====================
An error occurred during the test sequence action: 'verify'. Cleaning up.
```

The `Failed to get D-Bus connection: Operation not permitted` is about systemd being difficult to run in docker container. Have a look [here](https://github.com/CentOS/CentOS-Dockerfiles/blob/master/systemd/centos7/Dockerfile) to see how CentOS customize their minimal CentOS 7 container image to be "systemd-enabled". And while starting the container make sure it's privileged as explained [here](https://hub.docker.com/r/centos/systemd/). For Molecule configuration, it looks like this :

```yaml
- name: molecule-YOUR_ROLE_NAME-centos7
  image: centos/systemd
  privileged: True
  volumes:
    - "/sys/fs/cgroup:/sys/fs/cgroup:ro"
```
