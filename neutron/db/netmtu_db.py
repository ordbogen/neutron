# Copyright (c) 2015 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from neutron.api.v2 import attributes
from neutron.db import db_base_plugin_v2
from neutron.extensions import netmtu
from neutron.plugins.common import utils


CONF = cfg.CONF


# TODO(ihrachys): the class is not used in the tree; mixins are generally
# discouraged these days, so maybe it's worth considering deprecation for the
# class. Interested plugins would be able to ship it on their own, if they want
# to stick to mixins, or implement the behaviour in another way.
class Netmtu_db_mixin(object):
    """Mixin class to add network MTU support to db_base_plugin_v2."""

    def _extend_network_dict_mtu(self, network_res, network_db):
        # don't use network_db argument since MTU is not persisted in database
        network_res[netmtu.MTU] = utils.get_deployment_physnet_mtu()
        return network_res

    db_base_plugin_v2.NeutronDbPluginV2.register_dict_extend_funcs(
        attributes.NETWORKS, ['_extend_network_dict_mtu'])
