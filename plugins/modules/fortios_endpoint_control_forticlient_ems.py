#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_endpoint_control_forticlient_ems
short_description: Configure FortiClient Enterprise Management Server (EMS) entries in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify endpoint_control feature and forticlient_ems category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.8"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.9.0
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root

    state:
        description:
            - Indicates whether to create or remove the object.
              This attribute was present already in previous version in a deeper level.
              It has been moved out to this outer level.
        type: str
        required: false
        choices:
            - present
            - absent
        version_added: 2.9
    endpoint_control_forticlient_ems:
        description:
            - Configure FortiClient Enterprise Management Server (EMS) entries.
        default: null
        type: dict
        suboptions:
            state:
                description:
                    - B(Deprecated)
                    - Starting with Ansible 2.9 we recommend using the top-level 'state' parameter.
                    - HORIZONTALLINE
                    - Indicates whether to create or remove the object.
                type: str
                required: false
                choices:
                    - present
                    - absent
            address:
                description:
                    - Firewall address name. Source firewall.address.name.
                type: str
            admin_password:
                description:
                    - FortiClient EMS admin password.
                type: str
            admin_type:
                description:
                    - FortiClient EMS admin type.
                type: str
                choices:
                    - Windows
                    - LDAP
            admin_username:
                description:
                    - FortiClient EMS admin username.
                type: str
            https_port:
                description:
                    - 'FortiClient EMS HTTPS access port number. (1 - 65535).'
                type: int
            listen_port:
                description:
                    - 'FortiClient EMS telemetry listen port number. (1 - 65535).'
                type: int
            name:
                description:
                    - FortiClient Enterprise Management Server (EMS) name.
                required: true
                type: str
            rest_api_auth:
                description:
                    - FortiClient EMS REST API authentication.
                type: str
                choices:
                    - disable
                    - userpass
            serial_number:
                description:
                    - FortiClient EMS Serial Number.
                type: str
            upload_port:
                description:
                    - 'FortiClient EMS telemetry upload port number. (1 - 65535).'
                type: int
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure FortiClient Enterprise Management Server (EMS) entries.
    fortios_endpoint_control_forticlient_ems:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      endpoint_control_forticlient_ems:
        address: "<your_own_value> (source firewall.address.name)"
        admin_password: "<your_own_value>"
        admin_type: "Windows"
        admin_username: "<your_own_value>"
        https_port: "7"
        listen_port: "8"
        name: "default_name_9"
        rest_api_auth: "disable"
        serial_number: "<your_own_value>"
        upload_port: "12"

'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def filter_endpoint_control_forticlient_ems_data(json):
    option_list = ['address', 'admin_password', 'admin_type',
                   'admin_username', 'https_port', 'listen_port',
                   'name', 'rest_api_auth', 'serial_number',
                   'upload_port']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def endpoint_control_forticlient_ems(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['endpoint_control_forticlient_ems'] and data['endpoint_control_forticlient_ems']['state']:
        state = data['endpoint_control_forticlient_ems']['state']
    else:
        state = True
    endpoint_control_forticlient_ems_data = data['endpoint_control_forticlient_ems']
    filtered_data = underscore_to_hyphen(filter_endpoint_control_forticlient_ems_data(endpoint_control_forticlient_ems_data))

    if state == "present":
        return fos.set('endpoint-control',
                       'forticlient-ems',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('endpoint-control',
                          'forticlient-ems',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_endpoint_control(data, fos):

    if data['endpoint_control_forticlient_ems']:
        resp = endpoint_control_forticlient_ems(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('endpoint_control_forticlient_ems'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "endpoint_control_forticlient_ems": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "address": {"required": False, "type": "str"},
                "admin_password": {"required": False, "type": "str"},
                "admin_type": {"required": False, "type": "str",
                               "choices": ["Windows",
                                           "LDAP"]},
                "admin_username": {"required": False, "type": "str"},
                "https_port": {"required": False, "type": "int"},
                "listen_port": {"required": False, "type": "int"},
                "name": {"required": True, "type": "str"},
                "rest_api_auth": {"required": False, "type": "str",
                                  "choices": ["disable",
                                              "userpass"]},
                "serial_number": {"required": False, "type": "str"},
                "upload_port": {"required": False, "type": "int"}

            }
        }
    }

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)

        is_error, has_changed, result = fortios_endpoint_control(module.params, fos)
        versions_check_result = connection.get_system_version()
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and galaxy, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
