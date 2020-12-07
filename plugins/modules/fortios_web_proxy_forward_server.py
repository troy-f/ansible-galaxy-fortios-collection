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
module: fortios_web_proxy_forward_server
short_description: Configure forward-server addresses in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify web_proxy feature and forward_server category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.9"
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
        type: str
        required: true
        choices:
            - present
            - absent
    web_proxy_forward_server:
        description:
            - Configure forward-server addresses.
        default: null
        type: dict
        suboptions:
            addr_type:
                description:
                    - 'Address type of the forwarding proxy server: IP or FQDN.'
                type: str
                choices:
                    - ip
                    - fqdn
            comment:
                description:
                    - Comment.
                type: str
            fqdn:
                description:
                    - Forward server Fully Qualified Domain Name (FQDN).
                type: str
            healthcheck:
                description:
                    - Enable/disable forward server health checking. Attempts to connect through the remote forwarding server to a destination to verify that
                       the forwarding server is operating normally.
                type: str
                choices:
                    - disable
                    - enable
            ip:
                description:
                    - Forward proxy server IP address.
                type: str
            monitor:
                description:
                    - 'URL for forward server health check monitoring .'
                type: str
            name:
                description:
                    - Server name.
                required: true
                type: str
            port:
                description:
                    - Port number that the forwarding server expects to receive HTTP sessions on (1 - 65535).
                type: int
            server_down_option:
                description:
                    - 'Action to take when the forward server is found to be down: block sessions until the server is back up or pass sessions to their
                       destination.'
                type: str
                choices:
                    - block
                    - pass
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
  - name: Configure forward-server addresses.
    fortios_web_proxy_forward_server:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      web_proxy_forward_server:
        addr_type: "ip"
        comment: "Comment."
        fqdn: "<your_own_value>"
        healthcheck: "disable"
        ip: "<your_own_value>"
        monitor: "<your_own_value>"
        name: "default_name_9"
        port: "10"
        server_down_option: "block"

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


def filter_web_proxy_forward_server_data(json):
    option_list = ['addr_type', 'comment', 'fqdn',
                   'healthcheck', 'ip', 'monitor',
                   'name', 'port', 'server_down_option']
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


def web_proxy_forward_server(data, fos):
    vdom = data['vdom']
    state = data['state']
    web_proxy_forward_server_data = data['web_proxy_forward_server']
    filtered_data = underscore_to_hyphen(filter_web_proxy_forward_server_data(web_proxy_forward_server_data))

    if state == "present":
        return fos.set('web-proxy',
                       'forward-server',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('web-proxy',
                          'forward-server',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_web_proxy(data, fos):

    if data['web_proxy_forward_server']:
        resp = web_proxy_forward_server(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('web_proxy_forward_server'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "web_proxy_forward_server": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "addr_type": {"required": False, "type": "str",
                              "choices": ["ip",
                                          "fqdn"]},
                "comment": {"required": False, "type": "str"},
                "fqdn": {"required": False, "type": "str"},
                "healthcheck": {"required": False, "type": "str",
                                "choices": ["disable",
                                            "enable"]},
                "ip": {"required": False, "type": "str"},
                "monitor": {"required": False, "type": "str"},
                "name": {"required": True, "type": "str"},
                "port": {"required": False, "type": "int"},
                "server_down_option": {"required": False, "type": "str",
                                       "choices": ["block",
                                                   "pass"]}

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

        is_error, has_changed, result = fortios_web_proxy(module.params, fos)
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
