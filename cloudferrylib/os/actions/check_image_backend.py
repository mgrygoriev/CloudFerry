# Copyright (c) 2015 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and#
# limitations under the License.


from cloudferrylib.base.action import action
from cloudferrylib.utils import utils as utl

LOG = utl.get_log(__name__)


class CheckImageBackend(action.Action):
    def run(self, **kwargs):
        """Check image backend by getting list of images.

        """
        image_resource = self.cloud.resources[utl.IMAGE_RESOURCE]
        try:
            images_list = image_resource.glance_client.images.list()
            if images_list:
                LOG.debug('Images list is OK')
        except Exception as e:
            LOG.error('Images list error')
            raise e
