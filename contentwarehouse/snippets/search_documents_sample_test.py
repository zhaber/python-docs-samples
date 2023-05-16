# # Copyright 2023 Google LLC
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
#


# Set two environment variables before running the test GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_USER
# For example,
# export GOOGLE_CLOUD_PROJECT = pso-starter-kit
# export GOOGLE_CLOUD_USER = my_ldap  (without @google.com)


import os


from contentwarehouse.snippets import search_documents_sample
from contentwarehouse.snippets import test_utilities
import pytest


project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
location = "us"  # Format is 'us' or 'eu'
document_query_text = "document"




def test_search_documents(capsys: pytest.CaptureFixture) -> None:
    project_number = test_utilities.get_project_number(project_id)
    search_documents_sample.search_documents_sample(
        project_number=project_number,
        location=location,
        document_query_text=document_query_text,
    )
    out, _ = capsys.readouterr()


    assert "document" in out
