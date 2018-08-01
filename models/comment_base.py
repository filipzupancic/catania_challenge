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


class CommentBase(object):
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
        'author': 'User',
        'created': 'datetime',
        'parent': 'CardBase',
        'attachments': 'ListOfResourcesOfFile',
        'snippet': 'str',
        'tags': 'ListOfTags'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'revision': 'revision',
        'client_id': 'clientId',
        'type': '$type',
        'author': 'author',
        'created': 'created',
        'parent': 'parent',
        'attachments': 'attachments',
        'snippet': 'snippet',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, revision=None, client_id=None, type=None, author=None, created=None, parent=None, attachments=None, snippet=None, tags=None):
        """
        CommentBase - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._revision = None
        self._client_id = None
        self._type = None
        self._author = None
        self._created = None
        self._parent = None
        self._attachments = None
        self._snippet = None
        self._tags = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if revision is not None:
          self.revision = revision
        if client_id is not None:
          self.client_id = client_id
        self.type = type
        if author is not None:
          self.author = author
        if created is not None:
          self.created = created
        if parent is not None:
          self.parent = parent
        if attachments is not None:
          self.attachments = attachments
        if snippet is not None:
          self.snippet = snippet
        if tags is not None:
          self.tags = tags

    @property
    def id(self):
        """
        Gets the id of this CommentBase.
        Resource id

        :return: The id of this CommentBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CommentBase.
        Resource id

        :param id: The id of this CommentBase.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this CommentBase.
        Resource name or title

        :return: The name of this CommentBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CommentBase.
        Resource name or title

        :param name: The name of this CommentBase.
        :type: str
        """

        self._name = name

    @property
    def revision(self):
        """
        Gets the revision of this CommentBase.
        Resource revision

        :return: The revision of this CommentBase.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this CommentBase.
        Resource revision

        :param revision: The revision of this CommentBase.
        :type: str
        """

        self._revision = revision

    @property
    def client_id(self):
        """
        Gets the client_id of this CommentBase.
        Resource client id

        :return: The client_id of this CommentBase.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CommentBase.
        Resource client id

        :param client_id: The client_id of this CommentBase.
        :type: str
        """

        self._client_id = client_id

    @property
    def type(self):
        """
        Gets the type of this CommentBase.

        :return: The type of this CommentBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CommentBase.

        :param type: The type of this CommentBase.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def author(self):
        """
        Gets the author of this CommentBase.
        Author of comment

        :return: The author of this CommentBase.
        :rtype: User
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this CommentBase.
        Author of comment

        :param author: The author of this CommentBase.
        :type: User
        """

        self._author = author

    @property
    def created(self):
        """
        Gets the created of this CommentBase.
        Created date time of comment

        :return: The created of this CommentBase.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this CommentBase.
        Created date time of comment

        :param created: The created of this CommentBase.
        :type: datetime
        """

        self._created = created

    @property
    def parent(self):
        """
        Gets the parent of this CommentBase.
        Parent of comment (the card it belongs to)

        :return: The parent of this CommentBase.
        :rtype: CardBase
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this CommentBase.
        Parent of comment (the card it belongs to)

        :param parent: The parent of this CommentBase.
        :type: CardBase
        """

        self._parent = parent

    @property
    def attachments(self):
        """
        Gets the attachments of this CommentBase.
        List of attachments on comment

        :return: The attachments of this CommentBase.
        :rtype: ListOfResourcesOfFile
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this CommentBase.
        List of attachments on comment

        :param attachments: The attachments of this CommentBase.
        :type: ListOfResourcesOfFile
        """

        self._attachments = attachments

    @property
    def snippet(self):
        """
        Gets the snippet of this CommentBase.
        Comment snippet

        :return: The snippet of this CommentBase.
        :rtype: str
        """
        return self._snippet

    @snippet.setter
    def snippet(self, snippet):
        """
        Sets the snippet of this CommentBase.
        Comment snippet

        :param snippet: The snippet of this CommentBase.
        :type: str
        """

        self._snippet = snippet

    @property
    def tags(self):
        """
        Gets the tags of this CommentBase.
        Tags reference on comment

        :return: The tags of this CommentBase.
        :rtype: ListOfTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CommentBase.
        Tags reference on comment

        :param tags: The tags of this CommentBase.
        :type: ListOfTags
        """

        self._tags = tags

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
        if not isinstance(other, CommentBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
