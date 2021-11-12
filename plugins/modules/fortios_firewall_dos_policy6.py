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
module: fortios_firewall_dos_policy6
short_description: Configure IPv6 DoS policies in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify firewall feature and dos_policy6 category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.10"
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
    enable_log:
        description:
            - Enable/Disable logging for task.
        type: bool
        required: false
        default: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root
    member_path:
        type: str
        description:
            - Member attribute path to operate on.
            - Delimited by a slash character if there are more than one attribute.
            - Parameter marked with member_path is legitimate for doing member operation.
    member_state:
        type: str
        description:
            - Add or delete a member under specified attribute path.
            - When member_state is specified, the state option is ignored.
        choices:
            - present
            - absent
    
    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - present
            - absent
    firewall_dos_policy6:
        description:
            - Configure IPv6 DoS policies.
        default: null
        type: dict
        suboptions:
            anomaly:
                description:
                    - Anomaly name.
                type: list
                suboptions:
                    action:
                        description:
                            - Action taken when the threshold is reached.
                        type: str
                        choices:
                            - pass
                            - block
                            - proxy
                    log:
                        description:
                            - Enable/disable anomaly logging.
                        type: str
                        choices:
                            - enable
                            - disable
                    name:
                        description:
                            - Anomaly name.
                        required: true
                        type: str
                    quarantine:
                        description:
                            - Quarantine method.
                        type: str
                        choices:
                            - none
                            - attacker
                    quarantine_expiry:
                        description:
                            - Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m). Requires quarantine set to attacker.
                        type: str
                    quarantine_log:
                        description:
                            - Enable/disable quarantine logging.
                        type: str
                        choices:
                            - disable
                            - enable
                    status:
                        description:
                            - Enable/disable this anomaly.
                        type: str
                        choices:
                            - disable
                            - enable
                    threshold:
                        description:
                            - Anomaly threshold. Number of detected instances per minute that triggers the anomaly action.
                        type: int
                    threshold(default):
                        description:
                            - Number of detected instances per minute which triggers action (1 - 2147483647). Note that each anomaly has a different threshold
                               value assigned to it.
                        type: int
            comments:
                description:
                    - Comment.
                type: str
            dstaddr:
                description:
                    - Destination address name from available addresses.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address6.name firewall.addrgrp6.name.
                        required: true
                        type: str
            interface:
                description:
                    - Incoming interface name from available interfaces. Source system.zone.name system.interface.name.
                type: str
            name:
                description:
                    - Policy name.
                type: str
            policyid:
                description:
                    - Policy ID.
                required: true
                type: int
            service:
                description:
                    - Service object from available options.
                type: list
                suboptions:
                    name:
                        description:
                            - Service name. Source firewall.service.custom.name firewall.service.group.name.
                        required: true
                        type: str
            srcaddr:
                description:
                    - Source address name from available addresses.
                type: list
                suboptions:
                    name:
                        description:
                            - Service name. Source firewall.address6.name firewall.addrgrp6.name.
                        required: true
                        type: str
            status:
                description:
                    - Enable/disable this policy.
                type: str
                choices:
                    - enable
                    - disable
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
  - name: Configure IPv6 DoS policies.
    fortios_firewall_dos_policy6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_dos_policy6:
        anomaly:
         -
            action: "pass"
            log: "enable"
            name: "default_name_6"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            status: "disable"
            threshold: "11"
            threshold(default): "12"
        comments: "<your_own_value>"
        dstaddr:
         -
            name: "default_name_15 (source firewall.address6.name firewall.addrgrp6.name)"
        interface: "<your_own_value> (source system.zone.name system.interface.name)"
        name: "default_name_17"
        policyid: "18"
        service:
         -
            name: "default_name_20 (source firewall.service.custom.name firewall.service.group.name)"
        srcaddr:
         -
            name: "default_name_22 (source firewall.address6.name firewall.addrgrp6.name)"
        status: "enable"

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
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import schema_to_module_spec
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_schema_versioning
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import is_same_comparison
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.comparison import serialize
def filter_firewall_dos_policy6_data(json):
    option_list = ['anomaly', 'comments', 'dstaddr',
                   'interface', 'name', 'policyid',
                   'service', 'srcaddr', 'status' ]
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

def firewall_dos_policy6(data, fos, check_mode=False):

    vdom = data['vdom']
    
    state = data['state']
    
    firewall_dos_policy6_data = data['firewall_dos_policy6']
    filtered_data = underscore_to_hyphen(filter_firewall_dos_policy6_data(firewall_dos_policy6_data))

    # check_mode starts from here
    if check_mode:
        mkey = fos.get_mkey('firewall', 'dos_policy6', filtered_data, vdom=vdom)
        current_data = fos.get('firewall', 'dos_policy6', vdom=vdom, mkey=mkey)
        is_existed = current_data and current_data.get('http_status') == 200 \
            and type(current_data.get('results')) == list \
            and len(current_data['results']) > 0

        # 2. if it exists and the state is 'present' then compare current settings with desired
        if state == 'present' or state is True:
            if mkey is None:
                return False, True, filtered_data

            # if mkey exists then compare each other
            # record exits and they're matched or not
            if is_existed:
                is_same = is_same_comparison(
                    serialize(current_data['results'][0]), serialize(filtered_data))
                return False, not is_same, filtered_data

            # record does not exist
            return False, True, filtered_data

        if state == 'absent':
            if mkey is None:
                return False, False, filtered_data

            if is_existed:
                return False, True, filtered_data
            return False, False, filtered_data

        return True, False, {'reason: ': 'Must provide state parameter'}
    
    if state == "present" or state is True:
        return fos.set('firewall',
                       'DoS-policy6',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('firewall',
                          'DoS-policy6',
                          mkey=filtered_data['policyid'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')
    

def is_successful_status(resp):
    return 'status' in resp and resp['status'] == 'success' or \
        'http_status' in resp and resp['http_status'] == 200 or \
        'http_method' in resp and resp['http_method'] == "DELETE" and resp['http_status'] == 404



def fortios_firewall(data, fos, check_mode):

    fos.do_member_operation('firewall_dos_policy6')
    if data['firewall_dos_policy6']:
        resp = firewall_dos_policy6(data, fos, check_mode)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('firewall_dos_policy6'))
    if check_mode:
        return resp
    return not is_successful_status(resp), \
        is_successful_status(resp) and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp



versioned_schema = {
    "type": "list", 
    "children": {
        "status": {
            "type": "string", 
            "options": [
                {
                    "value": "enable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                {
                    "value": "disable", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            ], 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "name": {
            "type": "string", 
            "revisions": {
                "v6.4.4": True, 
                "v7.0.0": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": False
            }
        }, 
        "service": {
            "type": "list", 
            "children": {
                "name": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            }, 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "comments": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "srcaddr": {
            "type": "list", 
            "children": {
                "name": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            }, 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "policyid": {
            "type": "integer", 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "interface": {
            "type": "string", 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "dstaddr": {
            "type": "list", 
            "children": {
                "name": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            }, 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }, 
        "anomaly": {
            "type": "list", 
            "children": {
                "status": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "disable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "name": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "quarantine": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "none", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "attacker", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "threshold": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "quarantine_expiry": {
                    "type": "string", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "action": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "pass", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "block", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "proxy", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": False, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": False, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "threshold(default)": {
                    "type": "integer", 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "quarantine_log": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "disable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }, 
                "log": {
                    "type": "string", 
                    "options": [
                        {
                            "value": "enable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }, 
                        {
                            "value": "disable", 
                            "revisions": {
                                "v6.0.0": True, 
                                "v7.0.0": True, 
                                "v6.0.5": True, 
                                "v6.4.4": True, 
                                "v7.0.1": True, 
                                "v6.4.0": True, 
                                "v6.4.1": True, 
                                "v6.2.0": True, 
                                "v6.2.3": True, 
                                "v6.2.5": True, 
                                "v6.2.7": True, 
                                "v6.0.11": True
                            }
                        }
                    ], 
                    "revisions": {
                        "v6.0.0": True, 
                        "v7.0.0": True, 
                        "v6.0.5": True, 
                        "v6.4.4": True, 
                        "v7.0.1": True, 
                        "v6.4.0": True, 
                        "v6.4.1": True, 
                        "v6.2.0": True, 
                        "v6.2.3": True, 
                        "v6.2.5": True, 
                        "v6.2.7": True, 
                        "v6.0.11": True
                    }
                }
            }, 
            "revisions": {
                "v6.0.0": True, 
                "v7.0.0": True, 
                "v6.0.5": True, 
                "v6.4.4": True, 
                "v7.0.1": True, 
                "v6.4.0": True, 
                "v6.4.1": True, 
                "v6.2.0": True, 
                "v6.2.3": True, 
                "v6.2.5": True, 
                "v6.2.7": True, 
                "v6.0.11": True
            }
        }
    }, 
    "revisions": {
        "v6.0.0": True, 
        "v7.0.0": True, 
        "v6.0.5": True, 
        "v6.4.4": True, 
        "v7.0.1": True, 
        "v6.4.0": True, 
        "v6.4.1": True, 
        "v6.2.0": True, 
        "v6.2.3": True, 
        "v6.2.5": True, 
        "v6.2.7": True, 
        "v6.0.11": True
    }
}

def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = 'policyid'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": bool},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "member_path": {"required": False, "type": "str"},
        "member_state": {
            "type": "str",
            "required": False,
            "choices": ["present", "absent"]
        },
        "state": {"required": True, "type": "str",
                        "choices": ["present", "absent"]},
        "firewall_dos_policy6": {
            "required": False, "type": "dict", "default": None,
            "options": { 
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["firewall_dos_policy6"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["firewall_dos_policy6"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=True)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        if 'enable_log' in module.params:
            connection.set_option('enable_log', module.params['enable_log'])
        else:
            connection.set_option('enable_log', False)
        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "firewall_dos_policy6")
        
        is_error, has_changed, result = fortios_firewall(module.params, fos, module.check_mode)
        
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and your playbook, see more details by specifying option -vvv")

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