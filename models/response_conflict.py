# coding: utf-8

"""
    My Title

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ResponseConflict(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'message': 'str',
        'error_code': 'str',
        'posted_resource': 'ResourceBase',
        'conflicted_resource': 'ResourceBase'
    }

    attribute_map = {
        'message': 'message',
        'error_code': 'errorCode',
        'posted_resource': 'postedResource',
        'conflicted_resource': 'conflictedResource'
    }

    def __init__(self, message=None, error_code=None, posted_resource=None, conflicted_resource=None):
        """
        ResponseConflict - a model defined in Swagger
        """

        self._message = None
        self._error_code = None
        self._posted_resource = None
        self._conflicted_resource = None

        if message is not None:
          self.message = message
        if error_code is not None:
          self.error_code = error_code
        if posted_resource is not None:
          self.posted_resource = posted_resource
        if conflicted_resource is not None:
          self.conflicted_resource = conflicted_resource

    @property
    def message(self):
        """
        Gets the message of this ResponseConflict.
        Response message

        :return: The message of this ResponseConflict.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResponseConflict.
        Response message

        :param message: The message of this ResponseConflict.
        :type: str
        """

        self._message = message

    @property
    def error_code(self):
        """
        Gets the error_code of this ResponseConflict.
        Error code (list of error codes available at enums/ErrorCode)

        :return: The error_code of this ResponseConflict.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this ResponseConflict.
        Error code (list of error codes available at enums/ErrorCode)

        :param error_code: The error_code of this ResponseConflict.
        :type: str
        """

        self._error_code = error_code

    @property
    def posted_resource(self):
        """
        Gets the posted_resource of this ResponseConflict.
        Resource being created or updated.

        :return: The posted_resource of this ResponseConflict.
        :rtype: ResourceBase
        """
        return self._posted_resource

    @posted_resource.setter
    def posted_resource(self, posted_resource):
        """
        Sets the posted_resource of this ResponseConflict.
        Resource being created or updated.

        :param posted_resource: The posted_resource of this ResponseConflict.
        :type: ResourceBase
        """

        self._posted_resource = posted_resource

    @property
    def conflicted_resource(self):
        """
        Gets the conflicted_resource of this ResponseConflict.
        Existing resource in conflict upon create or update event.

        :return: The conflicted_resource of this ResponseConflict.
        :rtype: ResourceBase
        """
        return self._conflicted_resource

    @conflicted_resource.setter
    def conflicted_resource(self, conflicted_resource):
        """
        Sets the conflicted_resource of this ResponseConflict.
        Existing resource in conflict upon create or update event.

        :param conflicted_resource: The conflicted_resource of this ResponseConflict.
        :type: ResourceBase
        """

        self._conflicted_resource = conflicted_resource

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ResponseConflict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
