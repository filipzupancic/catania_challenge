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


class EventList(object):
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
        'resources': 'list[EventBase]',
        'size': 'int',
        'offset': 'int',
        'total_size': 'int',
        'last_event_id': 'str'
    }

    attribute_map = {
        'resources': 'resources',
        'size': 'size',
        'offset': 'offset',
        'total_size': 'totalSize',
        'last_event_id': 'lastEventId'
    }

    def __init__(self, resources=None, size=None, offset=None, total_size=None, last_event_id=None):
        """
        EventList - a model defined in Swagger
        """

        self._resources = None
        self._size = None
        self._offset = None
        self._total_size = None
        self._last_event_id = None

        if resources is not None:
          self.resources = resources
        self.size = size
        self.offset = offset
        self.total_size = total_size
        if last_event_id is not None:
          self.last_event_id = last_event_id

    @property
    def resources(self):
        """
        Gets the resources of this EventList.

        :return: The resources of this EventList.
        :rtype: list[EventBase]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this EventList.

        :param resources: The resources of this EventList.
        :type: list[EventBase]
        """

        self._resources = resources

    @property
    def size(self):
        """
        Gets the size of this EventList.

        :return: The size of this EventList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this EventList.

        :param size: The size of this EventList.
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")

        self._size = size

    @property
    def offset(self):
        """
        Gets the offset of this EventList.

        :return: The offset of this EventList.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this EventList.

        :param offset: The offset of this EventList.
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")

        self._offset = offset

    @property
    def total_size(self):
        """
        Gets the total_size of this EventList.

        :return: The total_size of this EventList.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """
        Sets the total_size of this EventList.

        :param total_size: The total_size of this EventList.
        :type: int
        """
        if total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")

        self._total_size = total_size

    @property
    def last_event_id(self):
        """
        Gets the last_event_id of this EventList.
        Id of the most recent event on the list (is passed to sinceId on the event API)

        :return: The last_event_id of this EventList.
        :rtype: str
        """
        return self._last_event_id

    @last_event_id.setter
    def last_event_id(self, last_event_id):
        """
        Sets the last_event_id of this EventList.
        Id of the most recent event on the list (is passed to sinceId on the event API)

        :param last_event_id: The last_event_id of this EventList.
        :type: str
        """

        self._last_event_id = last_event_id

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
        if not isinstance(other, EventList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
