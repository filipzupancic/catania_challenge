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


class EventContactDeleted(object):
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
        'created': 'datetime',
        'type': 'str',
        'contact': 'ContactBase'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'type': '$type',
        'contact': 'contact'
    }

    def __init__(self, id=None, created=None, type=None, contact=None):
        """
        EventContactDeleted - a model defined in Swagger
        """

        self._id = None
        self._created = None
        self._type = None
        self._contact = None

        if id is not None:
          self.id = id
        if created is not None:
          self.created = created
        self.type = type
        if contact is not None:
          self.contact = contact

    @property
    def id(self):
        """
        Gets the id of this EventContactDeleted.
        Event id

        :return: The id of this EventContactDeleted.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventContactDeleted.
        Event id

        :param id: The id of this EventContactDeleted.
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """
        Gets the created of this EventContactDeleted.
        Date time when event was created

        :return: The created of this EventContactDeleted.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this EventContactDeleted.
        Date time when event was created

        :param created: The created of this EventContactDeleted.
        :type: datetime
        """

        self._created = created

    @property
    def type(self):
        """
        Gets the type of this EventContactDeleted.

        :return: The type of this EventContactDeleted.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EventContactDeleted.

        :param type: The type of this EventContactDeleted.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def contact(self):
        """
        Gets the contact of this EventContactDeleted.
        Contact resource

        :return: The contact of this EventContactDeleted.
        :rtype: ContactBase
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this EventContactDeleted.
        Contact resource

        :param contact: The contact of this EventContactDeleted.
        :type: ContactBase
        """

        self._contact = contact

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
        if not isinstance(other, EventContactDeleted):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
