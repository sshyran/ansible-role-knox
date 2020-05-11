# YOU.SKELETON_APPLICATION
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![pipeline status](https://gitlab.lmru.adeo.com/BI/dataplatform-infrastructure/role-SKELETON_APPLICATION/badges/master/pipeline.svg)](https://gitlab.lmru.adeo.com/BI/dataplatform-infrastructure/role-SKELETON_APPLICATION/commits/master)
[![IRC](https://img.shields.io/badge/dataplatformhq.slack.com-%23ansible-yellow.svg)](https://dataplatform-hq.slack.com/messages/CLM2NRTCL)

## Description

Deploy [SKELETON_APPLICATION](https://gitlab.lmru.adeo.com/BI/dataplatform-infrastructure/role-SKELETON_APPLICATION) using ansible.


Role Variables
--------------

See `defaults/main.yml` and `vars/main.yml`, or the example below

Dependencies
------------

See `meta/main.yml` for other roles dependencies

Example Playbook
----------------

```yaml
---
- hosts: all
- roles:
  - role: SKELETON_APPLICATION
    vars:
      your_role_variable_here: true
      your_role_variable_list_also_here:
        - one
        - 2
        - b'11'
```

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py27-ansible25 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.


## Authors

* **Dmitry Ibragimov** - *Initial work* - [60073101](https://gitlab.lmru.adeo.com/60073101)
* **SKELETON_AUTHOR** - *First implementation*
See also the list of [contributors](https://gitlab.lmru.adeo.com/groups/BI/dataplatform-ansible/-/group_members) who participated in this project.

## License

This project is licensed under the ADEO InnerSource License.

## Acknowledgments

* [Ansible Linting](https://medium.com/faun/linting-your-ansible-playbooks-and-make-a-continuous-integration-ci-solution-bcf8b4ea4c03)
* [Molecule examples](https://github.com/ansible/molecule/tree/master/test/scenarios/driver)
* [Testinfra](https://github.com/philpep/testinfra)
* Dragons will be here...