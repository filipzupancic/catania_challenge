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


class File(object):
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
        'created': 'datetime',
        'owner': 'User',
        'size': 'int',
        'hidden': 'bool',
        'thumbnail_info': 'ThumbnailInfo',
        'parent_comment': 'CommentBase',
        'parent_card': 'CardBase'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'revision': 'revision',
        'client_id': 'clientId',
        'type': '$type',
        'created': 'created',
        'owner': 'owner',
        'size': 'size',
        'hidden': 'hidden',
        'thumbnail_info': 'thumbnailInfo',
        'parent_comment': 'parentComment',
        'parent_card': 'parentCard'
    }

    def __init__(self, id=None, name=None, revision=None, client_id=None, type=None, created=None, owner=None, size=None, hidden=None, thumbnail_info=None, parent_comment=None, parent_card=None):
        """
        File - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._revision = None
        self._client_id = None
        self._type = None
        self._created = None
        self._owner = None
        self._size = None
        self._hidden = None
        self._thumbnail_info = None
        self._parent_comment = None
        self._parent_card = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if revision is not None:
          self.revision = revision
        if client_id is not None:
          self.client_id = client_id
        self.type = type
        if created is not None:
          self.created = created
        if owner is not None:
          self.owner = owner
        if size is not None:
          self.size = size
        if hidden is not None:
          self.hidden = hidden
        if thumbnail_info is not None:
          self.thumbnail_info = thumbnail_info
        if parent_comment is not None:
          self.parent_comment = parent_comment
        if parent_card is not None:
          self.parent_card = parent_card

    @property
    def id(self):
        """
        Gets the id of this File.
        Resource id

        :return: The id of this File.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this File.
        Resource id

        :param id: The id of this File.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this File.
        Resource name or title

        :return: The name of this File.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this File.
        Resource name or title

        :param name: The name of this File.
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """
        Gets the revision of this File.
        Resource revision

        :return: The revision of this File.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this File.
        Resource revision

        :param revision: The revision of this File.
        :type: str
        """

        self._revision = revision

    @property
    def client_id(self):
        """
        Gets the client_id of this File.
        Resource client id

        :return: The client_id of this File.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this File.
        Resource client id

        :param client_id: The client_id of this File.
        :type: str
        """

        self._client_id = client_id

    @property
    def type(self):
        """
        Gets the type of this File.

        :return: The type of this File.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this File.

        :param type: The type of this File.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def created(self):
        """
        Gets the created of this File.
        Date time when file was created

        :return: The created of this File.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this File.
        Date time when file was created

        :param created: The created of this File.
        :type: datetime
        """

        self._created = created

    @property
    def owner(self):
        """
        Gets the owner of this File.
        File owner

        :return: The owner of this File.
        :rtype: User
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this File.
        File owner

        :param owner: The owner of this File.
        :type: User
        """

        self._owner = owner

    @property
    def size(self):
        """
        Gets the size of this File.
        File size (in bytes)

        :return: The size of this File.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this File.
        File size (in bytes)

        :param size: The size of this File.
        :type: int
        """

        self._size = size

    @property
    def hidden(self):
        """
        Gets the hidden of this File.
        File is hidden

        :return: The hidden of this File.
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """
        Sets the hidden of this File.
        File is hidden

        :param hidden: The hidden of this File.
        :type: bool
        """

        self._hidden = hidden

    @property
    def thumbnail_info(self):
        """
        Gets the thumbnail_info of this File.
        File's thumbnail info

        :return: The thumbnail_info of this File.
        :rtype: ThumbnailInfo
        """
        return self._thumbnail_info

    @thumbnail_info.setter
    def thumbnail_info(self, thumbnail_info):
        """
        Sets the thumbnail_info of this File.
        File's thumbnail info

        :param thumbnail_info: The thumbnail_info of this File.
        :type: ThumbnailInfo
        """

        self._thumbnail_info = thumbnail_info

    @property
    def parent_comment(self):
        """
        Gets the parent_comment of this File.

        :return: The parent_comment of this File.
        :rtype: CommentBase
        """
        return self._parent_comment

    @parent_comment.setter
    def parent_comment(self, parent_comment):
        """
        Sets the parent_comment of this File.

        :param parent_comment: The parent_comment of this File.
        :type: CommentBase
        """

        self._parent_comment = parent_comment

    @property
    def parent_card(self):
        """
        Gets the parent_card of this File.
        Originating card of file

        :return: The parent_card of this File.
        :rtype: CardBase
        """
        return self._parent_card

    @parent_card.setter
    def parent_card(self, parent_card):
        """
        Sets the parent_card of this File.
        Originating card of file

        :param parent_card: The parent_card of this File.
        :type: CardBase
        """

        self._parent_card = parent_card

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
        if not isinstance(other, File):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
