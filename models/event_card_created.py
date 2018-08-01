# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EventCardCreated(object):
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
        'recipient': 'User',
        'type': 'str',
        'card': 'CardBase'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'recipient': 'recipient',
        'type': '$type',
        'card': 'card'
    }

    def __init__(self, id=None, created=None, recipient=None, type=None, card=None):
        """
        EventCardCreated - a model defined in Swagger
        """

        self._id = None
        self._created = None
        self._recipient = None
        self._type = None
        self._card = None

        if id is not None:
          self.id = id
        self.created = created
        if recipient is not None:
          self.recipient = recipient
        self.type = type
        if card is not None:
          self.card = card

    @property
    def id(self):
        """
        Gets the id of this EventCardCreated.

        :return: The id of this EventCardCreated.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventCardCreated.

        :param id: The id of this EventCardCreated.
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """
        Gets the created of this EventCardCreated.

        :return: The created of this EventCardCreated.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this EventCardCreated.

        :param created: The created of this EventCardCreated.
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def recipient(self):
        """
        Gets the recipient of this EventCardCreated.

        :return: The recipient of this EventCardCreated.
        :rtype: User
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """
        Sets the recipient of this EventCardCreated.

        :param recipient: The recipient of this EventCardCreated.
        :type: User
        """

        self._recipient = recipient

    @property
    def type(self):
        """
        Gets the type of this EventCardCreated.

        :return: The type of this EventCardCreated.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EventCardCreated.

        :param type: The type of this EventCardCreated.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def card(self):
        """
        Gets the card of this EventCardCreated.

        :return: The card of this EventCardCreated.
        :rtype: CardBase
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this EventCardCreated.

        :param card: The card of this EventCardCreated.
        :type: CardBase
        """

        self._card = card

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
        if not isinstance(other, EventCardCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
