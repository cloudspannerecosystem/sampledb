# Copyright 2019 Google Inc. All Rights Reserved.
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

"""Integration test for batch_import"""

import os
import datetime
import batch_import
from google.cloud import spanner


def test_batch_import():
  instance_id = os.environ['SPANNER_INSTANCE']

  # Append the current timestamp to the database name.
  now_str = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  database_id = 'sampledb_%s' % now_str
  batch_import.main(instance_id, database_id)

  # Delete the database.
  spanner_client = spanner.Client()
  instance = spanner_client.instance(instance_id)
  database = instance.database(database_id)
  database.drop()
