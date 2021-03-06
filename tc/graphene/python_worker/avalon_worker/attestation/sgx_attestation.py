#!/usr/bin/python3

# Copyright 2020 Intel Corporation
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

from abc import ABC, abstractmethod


class SGXAttestation(ABC):
    """
    Abstract class for SGX attestation.
    """

# -------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

# -------------------------------------------------------------------------

    @abstractmethod
    def get_mrenclave(self):
        """
        Get mrenclave value of enclave.

        Returns :
            mrenclave value of enclave as hex string.
            If Intel SGX environment is not present returns empty string.
        """
        pass

# -------------------------------------------------------------------------

    @abstractmethod
    def get_quote(self):
        """
        Get quote of enclave.

        Returns :
            quote value of enclave as base64 encoded string.
            If Intel SGX environment is not present returns empty string.
        """
        pass

# -------------------------------------------------------------------------

    @abstractmethod
    def write_user_report_data(self, user_data):
        """
        Write SGX user report data to be added in quote.
        This API is called before fetching the quote from SGX.

        Parameters :
            user_data: User report data in bytes.

        Returns :
            boolean: True if user report data write is success.
                     False in case of error.
        """
        pass

# -------------------------------------------------------------------------
