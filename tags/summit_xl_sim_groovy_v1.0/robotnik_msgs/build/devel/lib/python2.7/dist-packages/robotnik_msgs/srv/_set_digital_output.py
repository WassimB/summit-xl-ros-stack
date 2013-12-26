"""autogenerated by genpy from robotnik_msgs/set_digital_outputRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class set_digital_outputRequest(genpy.Message):
  _md5sum = "e1dc4e43688f0a8d32bc10e72fd189d2"
  _type = "robotnik_msgs/set_digital_outputRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 output
bool value

"""
  __slots__ = ['output','value']
  _slot_types = ['int8','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       output,value

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(set_digital_outputRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.output is None:
        self.output = 0
      if self.value is None:
        self.value = False
    else:
      self.output = 0
      self.value = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_bB.pack(_x.output, _x.value))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 2
      (_x.output, _x.value,) = _struct_bB.unpack(str[start:end])
      self.value = bool(self.value)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_bB.pack(_x.output, _x.value))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 2
      (_x.output, _x.value,) = _struct_bB.unpack(str[start:end])
      self.value = bool(self.value)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_bB = struct.Struct("<bB")
"""autogenerated by genpy from robotnik_msgs/set_digital_outputResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class set_digital_outputResponse(genpy.Message):
  _md5sum = "e2cc9e9d8c464550830df49c160979ad"
  _type = "robotnik_msgs/set_digital_outputResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool ret


"""
  __slots__ = ['ret']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ret

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(set_digital_outputResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ret is None:
        self.ret = False
    else:
      self.ret = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_B.pack(self.ret))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.ret,) = _struct_B.unpack(str[start:end])
      self.ret = bool(self.ret)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_B.pack(self.ret))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.ret,) = _struct_B.unpack(str[start:end])
      self.ret = bool(self.ret)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class set_digital_output(object):
  _type          = 'robotnik_msgs/set_digital_output'
  _md5sum = '5df94efb72fc0f5277220bfb51b87d14'
  _request_class  = set_digital_outputRequest
  _response_class = set_digital_outputResponse
