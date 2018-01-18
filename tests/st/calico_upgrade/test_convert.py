# Copyright (c) 2015-2017 Tigera, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import logging
import copy

from nose_parameterized import parameterized

from tests.st.test_base import TestBase
from tests.st.utils.utils import *
from tests.st.utils.data import *

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)

filebase = "test-data/v1/"

class TestNoData(TestBase):
    """
    Test calico-upgrade with an empty etcdv2 datastore.
    """
    def test_dry_run(self, filename):
        """
        Test dry-run when the etcdv2 datastore is empty.
        """
        # Convert the file
        rc = calicoctl("convert -f %s" % filebase+filename)
        rc.assert_no_error()

        # With the converted data to a temp file
        with open("/tmp/converted", 'w') as f:
            f.write(rc.output)

        # Load the converted data
        rc = calicoctl("apply -f /tmp/converted")
        rc.assert_no_error()
