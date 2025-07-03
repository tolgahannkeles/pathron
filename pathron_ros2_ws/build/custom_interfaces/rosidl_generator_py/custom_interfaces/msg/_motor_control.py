# generated from rosidl_generator_py/resource/_idl.py.em
# with input from custom_interfaces:msg/MotorControl.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_MotorControl(type):
    """Metaclass of message 'MotorControl'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('custom_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'custom_interfaces.msg.MotorControl')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__motor_control
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__motor_control
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__motor_control
            cls._TYPE_SUPPORT = module.type_support_msg__msg__motor_control
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__motor_control

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class MotorControl(metaclass=Metaclass_MotorControl):
    """Message class 'MotorControl'."""

    __slots__ = [
        '_front_left',
        '_front_right',
        '_rear_left',
        '_rear_right',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'front_left': 'uint8',
        'front_right': 'uint8',
        'rear_left': 'uint8',
        'rear_right': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.front_left = kwargs.get('front_left', int())
        self.front_right = kwargs.get('front_right', int())
        self.rear_left = kwargs.get('rear_left', int())
        self.rear_right = kwargs.get('rear_right', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.front_left != other.front_left:
            return False
        if self.front_right != other.front_right:
            return False
        if self.rear_left != other.rear_left:
            return False
        if self.rear_right != other.rear_right:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def front_left(self):
        """Message field 'front_left'."""
        return self._front_left

    @front_left.setter
    def front_left(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'front_left' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'front_left' field must be an unsigned integer in [0, 255]"
        self._front_left = value

    @builtins.property
    def front_right(self):
        """Message field 'front_right'."""
        return self._front_right

    @front_right.setter
    def front_right(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'front_right' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'front_right' field must be an unsigned integer in [0, 255]"
        self._front_right = value

    @builtins.property
    def rear_left(self):
        """Message field 'rear_left'."""
        return self._rear_left

    @rear_left.setter
    def rear_left(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'rear_left' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'rear_left' field must be an unsigned integer in [0, 255]"
        self._rear_left = value

    @builtins.property
    def rear_right(self):
        """Message field 'rear_right'."""
        return self._rear_right

    @rear_right.setter
    def rear_right(self, value):
        if self._check_fields:
            assert \
                isinstance(value, int), \
                "The 'rear_right' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'rear_right' field must be an unsigned integer in [0, 255]"
        self._rear_right = value
