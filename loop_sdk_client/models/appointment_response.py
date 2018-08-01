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


class AppointmentResponse(object):
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
        'id': 'str',
        'name': 'str',
        'revision': 'str',
        'client_id': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'revision': 'revision',
        'client_id': 'clientId',
        'type': '$type',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, revision=None, client_id=None, type=None, status=None):
        """
        AppointmentResponse - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._revision = None
        self._client_id = None
        self._type = None
        self._status = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if revision is not None:
          self.revision = revision
        if client_id is not None:
          self.client_id = client_id
        self.type = type
        if status is not None:
          self.status = status

    @property
    def id(self):
        """
        Gets the id of this AppointmentResponse.
        Resource id

        :return: The id of this AppointmentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AppointmentResponse.
        Resource id

        :param id: The id of this AppointmentResponse.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AppointmentResponse.
        Resource name or title

        :return: The name of this AppointmentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AppointmentResponse.
        Resource name or title

        :param name: The name of this AppointmentResponse.
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """
        Gets the revision of this AppointmentResponse.
        Resource revision

        :return: The revision of this AppointmentResponse.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AppointmentResponse.
        Resource revision

        :param revision: The revision of this AppointmentResponse.
        :type: str
        """

        self._revision = revision

    @property
    def client_id(self):
        """
        Gets the client_id of this AppointmentResponse.
        Resource client id

        :return: The client_id of this AppointmentResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this AppointmentResponse.
        Resource client id

        :param client_id: The client_id of this AppointmentResponse.
        :type: str
        """

        self._client_id = client_id

    @property
    def type(self):
        """
        Gets the type of this AppointmentResponse.

        :return: The type of this AppointmentResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AppointmentResponse.

        :param type: The type of this AppointmentResponse.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def status(self):
        """
        Gets the status of this AppointmentResponse.
        Status of attendee for authorized user

        :return: The status of this AppointmentResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AppointmentResponse.
        Status of attendee for authorized user

        :param status: The status of this AppointmentResponse.
        :type: str
        """

        self._status = status

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
        if not isinstance(other, AppointmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
