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


class ExpendOneHopRequest(object):
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
        "project_id": "int",
        "type_name": "str",
        "biz_id": "str",
        "edge_type_name_constraint": "list[EdgeTypeName]",
    }

    attribute_map = {
        "project_id": "projectId",
        "type_name": "typeName",
        "biz_id": "bizId",
        "edge_type_name_constraint": "edgeTypeNameConstraint",
    }

    def __init__(
        self,
        project_id=None,
        type_name=None,
        biz_id=None,
        edge_type_name_constraint=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ExpendOneHopRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._type_name = None
        self._biz_id = None
        self._edge_type_name_constraint = None
        self.discriminator = None

        self.project_id = project_id
        self.type_name = type_name
        self.biz_id = biz_id
        self.edge_type_name_constraint = edge_type_name_constraint

    @property
    def project_id(self):
        """Gets the project_id of this ExpendOneHopRequest.  # noqa: E501


        :return: The project_id of this ExpendOneHopRequest.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ExpendOneHopRequest.


        :param project_id: The project_id of this ExpendOneHopRequest.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and project_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `project_id`, must not be `None`"
            )  # noqa: E501

        self._project_id = project_id

    @property
    def type_name(self):
        """Gets the type_name of this ExpendOneHopRequest.  # noqa: E501


        :return: The type_name of this ExpendOneHopRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this ExpendOneHopRequest.


        :param type_name: The type_name of this ExpendOneHopRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type_name`, must not be `None`"
            )  # noqa: E501

        self._type_name = type_name

    @property
    def biz_id(self):
        """Gets the biz_id of this ExpendOneHopRequest.  # noqa: E501


        :return: The biz_id of this ExpendOneHopRequest.  # noqa: E501
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this ExpendOneHopRequest.


        :param biz_id: The biz_id of this ExpendOneHopRequest.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and biz_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `biz_id`, must not be `None`"
            )  # noqa: E501

        self._biz_id = biz_id

    @property
    def edge_type_name_constraint(self):
        """Gets the edge_type_name_constraint of this ExpendOneHopRequest.  # noqa: E501


        :return: The edge_type_name_constraint of this ExpendOneHopRequest.  # noqa: E501
        :rtype: list[EdgeTypeName]
        """
        return self._edge_type_name_constraint

    @edge_type_name_constraint.setter
    def edge_type_name_constraint(self, edge_type_name_constraint):
        """Sets the edge_type_name_constraint of this ExpendOneHopRequest.


        :param edge_type_name_constraint: The edge_type_name_constraint of this ExpendOneHopRequest.  # noqa: E501
        :type: list[EdgeTypeName]
        """

        self._edge_type_name_constraint = edge_type_name_constraint

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
        if not isinstance(other, ExpendOneHopRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExpendOneHopRequest):
            return True

        return self.to_dict() != other.to_dict()
