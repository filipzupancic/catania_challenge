# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from loop_sdk_client.models.event_base import EventBase  # noqa: F401,E501
from loop_sdk_client.models.user import User  # noqa: F401,E501


class EventUserRegistered(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'created': 'datetime',
        'recipient': 'User',
        'type': 'str',
        'user_agent': 'str',
        'auth_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'recipient': 'recipient',
        'type': '$type',
        'user_agent': 'userAgent',
        'auth_type': 'authType'
    }

    def __init__(self, id=None, created=None, recipient=None, type=None, user_agent=None, auth_type=None):
        """EventUserRegistered - a model defined in Swagger"""  # noqa: E501

        self._user_agent = None
        self._auth_type = None
        self.discriminator = None
        self._user = None

        if id is not None:
            self.id = id
        self.created = created
        if recipient is not None:
            self.recipient = recipient
        self.type = type
        if user_agent is not None:
            self.user_agent = user_agent
        if auth_type is not None:
            self.auth_type = auth_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, EventUserRegistered):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
