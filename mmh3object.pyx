from libc.string cimport strlen
from libc.stdint cimport uint32_t, int32_t

cdef int hash_func(char* s):
    cdef uint32_t seed = 0;
    cdef int32_t result[1];

    MurmurHash3_x86_32(s, strlen(s), seed, result)

    return result[0]

hash_True = hash_func(b"True")
hash_False = hash_func(b"False")
hash_None = hash_func(b"None")

cpdef mmh3object(o):
  """
  Makes a hash from a dictionary, list, tuple or set to any level, that contains
  only other hashable types (including any lists, tuples, sets, and
  dictionaries).
  """

  if o is True:
    return hash_True

  elif o is False:
    return hash_False

  elif o is None:
    return hash_None

  t = type(o)

  if t is str or t is unicode or t is int or t is long or t is float:
    return hash_func(bytes(repr(o)))

  elif t is tuple or t is list:
    return hash_func(bytes(repr([mmh3object(e) for e in o])))

  elif t is dict:
    return hash_func(bytes(repr(sorted([(k, mmh3object(v)) for k, v in o.iteritems()]))))

  elif t is set or t is frozenset:
    return hash_func(bytes(repr(sorted([mmh3object(e) for e in o]))))

  elif isinstance(o, (tuple, list)):
      return hash_func(bytes(repr([mmh3object(e) for e in o])))

  elif isinstance(o, (set, frozenset)):
      return hash_func(bytes(repr(sorted([mmh3object(e) for e in o]))))

  elif isinstance(o, dict):
      return hash_func(bytes(repr(sorted([(k, mmh3object(v)) for k, v in o.iteritems()]))))

  else:
      return hash_func(bytes(repr(o)))
