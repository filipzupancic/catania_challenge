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


class SyncSettingsGmail(object):
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
        'is_enabled': 'bool',
        'import_day_range': 'int',
        'auth_code': 'str',
        'refresh_token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'revision': 'revision',
        'client_id': 'clientId',
        'type': '$type',
        'is_enabled': 'isEnabled',
        'import_day_range': 'importDayRange',
        'auth_code': 'authCode',
        'refresh_token': 'refreshToken'
    }

    def __init__(self, id=None, name=None, revision=None, client_id=None, type=None, is_enabled=None, import_day_range=None, auth_code=None, refresh_token=None):
        """
        SyncSettingsGmail - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._revision = None
        self._client_id = None
        self._type = None
        self._is_enabled = None
        self._import_day_range = None
        self._auth_code = None
        self._refresh_token = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if revision is not None:
          self.revision = revision
        if client_id is not None:
          self.client_id = client_id
        self.type = type
        if is_enabled is not None:
          self.is_enabled = is_enabled
        if import_day_range is not None:
          self.import_day_range = import_day_range
        if auth_code is not None:
          self.auth_code = auth_code
        if refresh_token is not None:
          self.refresh_token = refresh_token

    @property
    def id(self):
        """
        Gets the id of this SyncSettingsGmail.
        Resource id

        :return: The id of this SyncSettingsGmail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SyncSettingsGmail.
        Resource id

        :param id: The id of this SyncSettingsGmail.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SyncSettingsGmail.
        Resource name or title

        :return: The name of this SyncSettingsGmail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SyncSettingsGmail.
        Resource name or title

        :param name: The name of this SyncSettingsGmail.
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """
        Gets the revision of this SyncSettingsGmail.
        Resource revision

        :return: The revision of this SyncSettingsGmail.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this SyncSettingsGmail.
        Resource revision

        :param revision: The revision of this SyncSettingsGmail.
        :type: str
        """

        self._revision = revision

    @property
    def client_id(self):
        """
        Gets the client_id of this SyncSettingsGmail.
        Resource client id

        :return: The client_id of this SyncSettingsGmail.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this SyncSettingsGmail.
        Resource client id

        :param client_id: The client_id of this SyncSettingsGmail.
        :type: str
        """

        self._client_id = client_id

    @property
    def type(self):
        """
        Gets the type of this SyncSettingsGmail.

        :return: The type of this SyncSettingsGmail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SyncSettingsGmail.

        :param type: The type of this SyncSettingsGmail.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this SyncSettingsGmail.
        Sync is enabled

        :return: The is_enabled of this SyncSettingsGmail.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this SyncSettingsGmail.
        Sync is enabled

        :param is_enabled: The is_enabled of this SyncSettingsGmail.
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def import_day_range(self):
        """
        Gets the import_day_range of this SyncSettingsGmail.
        Email import day range for the past

        :return: The import_day_range of this SyncSettingsGmail.
        :rtype: int
        """
        return self._import_day_range

    @import_day_range.setter
    def import_day_range(self, import_day_range):
        """
        Sets the import_day_range of this SyncSettingsGmail.
        Email import day range for the past

        :param import_day_range: The import_day_range of this SyncSettingsGmail.
        :type: int
        """

        self._import_day_range = import_day_range

    @property
    def auth_code(self):
        """
        Gets the auth_code of this SyncSettingsGmail.
        Google authentication code

        :return: The auth_code of this SyncSettingsGmail.
        :rtype: str
        """
        return self._auth_code

    @auth_code.setter
    def auth_code(self, auth_code):
        """
        Sets the auth_code of this SyncSettingsGmail.
        Google authentication code

        :param auth_code: The auth_code of this SyncSettingsGmail.
        :type: str
        """

        self._auth_code = auth_code

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this SyncSettingsGmail.
        Google refresh token

        :return: The refresh_token of this SyncSettingsGmail.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this SyncSettingsGmail.
        Google refresh token

        :param refresh_token: The refresh_token of this SyncSettingsGmail.
        :type: str
        """

        self._refresh_token = refresh_token

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
        if not isinstance(other, SyncSettingsGmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
