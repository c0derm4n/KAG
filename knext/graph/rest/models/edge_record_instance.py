# coding: utf-8
# Copyright 2023 OpenSPG Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


"""
    knext

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from knext.common.rest.configuration import Configuration


class EdgeRecordInstance(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "src_type": "str",
        "src_id": "str",
        "dst_type": "str",
        "dst_id": "str",
        "label": "str",
        "properties": "object",
    }

    attribute_map = {
        "src_type": "srcType",
        "src_id": "srcId",
        "dst_type": "dstType",
        "dst_id": "dstId",
        "label": "label",
        "properties": "properties",
    }

    def __init__(
        self,
        src_type=None,
        src_id=None,
        dst_type=None,
        dst_id=None,
        label=None,
        properties=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """EdgeRecordInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._src_type = None
        self._src_id = None
        self._dst_type = None
        self._dst_id = None
        self._label = None
        self._properties = None
        self.discriminator = None

        self.src_type = src_type
        self.src_id = src_id
        self.dst_type = dst_type
        self.dst_id = dst_id
        self.label = label
        self.properties = properties

    @property
    def src_type(self):
        """Gets the src_type of this EdgeRecordInstance.  # noqa: E501


        :return: The src_type of this EdgeRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._src_type

    @src_type.setter
    def src_type(self, src_type):
        """Sets the src_type of this EdgeRecordInstance.


        :param src_type: The src_type of this EdgeRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and src_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `src_type`, must not be `None`"
            )  # noqa: E501

        self._src_type = src_type

    @property
    def src_id(self):
        """Gets the src_id of this EdgeRecordInstance.  # noqa: E501


        :return: The src_id of this EdgeRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._src_id

    @src_id.setter
    def src_id(self, src_id):
        """Sets the src_id of this EdgeRecordInstance.


        :param src_id: The src_id of this EdgeRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and src_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `src_id`, must not be `None`"
            )  # noqa: E501

        self._src_id = src_id

    @property
    def dst_type(self):
        """Gets the dst_type of this EdgeRecordInstance.  # noqa: E501


        :return: The dst_type of this EdgeRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._dst_type

    @dst_type.setter
    def dst_type(self, dst_type):
        """Sets the dst_type of this EdgeRecordInstance.


        :param dst_type: The dst_type of this EdgeRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and dst_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `dst_type`, must not be `None`"
            )  # noqa: E501

        self._dst_type = dst_type

    @property
    def dst_id(self):
        """Gets the dst_id of this EdgeRecordInstance.  # noqa: E501


        :return: The dst_id of this EdgeRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._dst_id

    @dst_id.setter
    def dst_id(self, dst_id):
        """Sets the dst_id of this EdgeRecordInstance.


        :param dst_id: The dst_id of this EdgeRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and dst_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `dst_id`, must not be `None`"
            )  # noqa: E501

        self._dst_id = dst_id

    @property
    def label(self):
        """Gets the label of this EdgeRecordInstance.  # noqa: E501


        :return: The label of this EdgeRecordInstance.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this EdgeRecordInstance.


        :param label: The label of this EdgeRecordInstance.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label`, must not be `None`"
            )  # noqa: E501

        self._label = label

    @property
    def properties(self):
        """Gets the properties of this EdgeRecordInstance.  # noqa: E501


        :return: The properties of this EdgeRecordInstance.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this EdgeRecordInstance.


        :param properties: The properties of this EdgeRecordInstance.  # noqa: E501
        :type: object
        """
        if (
            self.local_vars_configuration.client_side_validation and properties is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `properties`, must not be `None`"
            )  # noqa: E501

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EdgeRecordInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EdgeRecordInstance):
            return True

        return self.to_dict() != other.to_dict()