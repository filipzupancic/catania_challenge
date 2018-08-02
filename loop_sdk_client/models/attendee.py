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


class Attendee(object):
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
        'tags': 'ListOfTags',
        'weight': 'float',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'online_status': 'str',
        'last_activity_at': 'datetime',
        'status_updated_at': 'datetime',
        'is_optional': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'revision': 'revision',
        'client_id': 'clientId',
        'type': '$type',
        'tags': 'tags',
        'weight': 'weight',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'online_status': 'onlineStatus',
        'last_activity_at': 'lastActivityAt',
        'status_updated_at': 'statusUpdatedAt',
        'is_optional': 'isOptional',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, revision=None, client_id=None, type=None, tags=None, weight=None, email=None, first_name=None, last_name=None, online_status=None, last_activity_at=None, status_updated_at=None, is_optional=None, status=None):
        """
        Attendee - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._revision = None
        self._client_id = None
        self._type = None
        self._tags = None
        self._weight = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._online_status = None
        self._last_activity_at = None
        self._status_updated_at = None
        self._is_optional = None
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
        if tags is not None:
          self.tags = tags
        if weight is not None:
          self.weight = weight
        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if online_status is not None:
          self.online_status = online_status
        if last_activity_at is not None:
          self.last_activity_at = last_activity_at
        if status_updated_at is not None:
          self.status_updated_at = status_updated_at
        if is_optional is not None:
          self.is_optional = is_optional
        if status is not None:
          self.status = status

    @property
    def id(self):
        """
        Gets the id of this Attendee.
        Resource id

        :return: The id of this Attendee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Attendee.
        Resource id

        :param id: The id of this Attendee.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Attendee.
        Resource name or title

        :return: The name of this Attendee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Attendee.
        Resource name or title

        :param name: The name of this Attendee.
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """
        Gets the revision of this Attendee.
        Resource revision

        :return: The revision of this Attendee.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this Attendee.
        Resource revision

        :param revision: The revision of this Attendee.
        :type: str
        """

        self._revision = revision

    @property
    def client_id(self):
        """
        Gets the client_id of this Attendee.
        Resource client id

        :return: The client_id of this Attendee.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this Attendee.
        Resource client id

        :param client_id: The client_id of this Attendee.
        :type: str
        """

        self._client_id = client_id

    @property
    def type(self):
        """
        Gets the type of this Attendee.

        :return: The type of this Attendee.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Attendee.

        :param type: The type of this Attendee.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def tags(self):
        """
        Gets the tags of this Attendee.
        Tags reference on contact

        :return: The tags of this Attendee.
        :rtype: ListOfTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Attendee.
        Tags reference on contact

        :param tags: The tags of this Attendee.
        :type: ListOfTags
        """

        self._tags = tags

    @property
    def weight(self):
        """
        Gets the weight of this Attendee.
        Usage weight.

        :return: The weight of this Attendee.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Attendee.
        Usage weight.

        :param weight: The weight of this Attendee.
        :type: float
        """

        self._weight = weight

    @property
    def email(self):
        """
        Gets the email of this Attendee.
        User's email address

        :return: The email of this Attendee.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Attendee.
        User's email address

        :param email: The email of this Attendee.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this Attendee.
        User's first name

        :return: The first_name of this Attendee.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Attendee.
        User's first name

        :param first_name: The first_name of this Attendee.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Attendee.
        User's last name

        :return: The last_name of this Attendee.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Attendee.
        User's last name

        :param last_name: The last_name of this Attendee.
        :type: str
        """

        self._last_name = last_name

    @property
    def online_status(self):
        """
        Gets the online_status of this Attendee.
        Online status (possible values can be seen at enums/UserStatus)

        :return: The online_status of this Attendee.
        :rtype: str
        """
        return self._online_status

    @online_status.setter
    def online_status(self, online_status):
        """
        Sets the online_status of this Attendee.
        Online status (possible values can be seen at enums/UserStatus)

        :param online_status: The online_status of this Attendee.
        :type: str
        """

        self._online_status = online_status

    @property
    def last_activity_at(self):
        """
        Gets the last_activity_at of this Attendee.
        Date time of the user's last activity

        :return: The last_activity_at of this Attendee.
        :rtype: datetime
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        """
        Sets the last_activity_at of this Attendee.
        Date time of the user's last activity

        :param last_activity_at: The last_activity_at of this Attendee.
        :type: datetime
        """

        self._last_activity_at = last_activity_at

    @property
    def status_updated_at(self):
        """
        Gets the status_updated_at of this Attendee.
        Attendee status was last updated at time

        :return: The status_updated_at of this Attendee.
        :rtype: datetime
        """
        return self._status_updated_at

    @status_updated_at.setter
    def status_updated_at(self, status_updated_at):
        """
        Sets the status_updated_at of this Attendee.
        Attendee status was last updated at time

        :param status_updated_at: The status_updated_at of this Attendee.
        :type: datetime
        """

        self._status_updated_at = status_updated_at

    @property
    def is_optional(self):
        """
        Gets the is_optional of this Attendee.
        Attendee is optional flag - if it isn't optional, it's required

        :return: The is_optional of this Attendee.
        :rtype: bool
        """
        return self._is_optional

    @is_optional.setter
    def is_optional(self, is_optional):
        """
        Sets the is_optional of this Attendee.
        Attendee is optional flag - if it isn't optional, it's required

        :param is_optional: The is_optional of this Attendee.
        :type: bool
        """

        self._is_optional = is_optional

    @property
    def status(self):
        """
        Gets the status of this Attendee.
        Attendee response status (defined in enums/ResponseTypeModel). Can be either Accept, Tentative, Decline, Organizer or NeedsAction

        :return: The status of this Attendee.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Attendee.
        Attendee response status (defined in enums/ResponseTypeModel). Can be either Accept, Tentative, Decline, Organizer or NeedsAction

        :param status: The status of this Attendee.
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
        if not isinstance(other, Attendee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other