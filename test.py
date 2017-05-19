import mmh3object
import mmh3
import timeit

# Makes a hash from a dictionary, list, tuple or set to any level, that contains
# only other hashable types (including any lists, tuples, sets, and
# dictionaries).

def mmh3object_purepython(o):

  hash_func = mmh3.hash

  t = type(o)

  if t in (str, unicode, int, long, float, bool):
    return hash_func(repr(o))

  elif t in (tuple, list):
    return hash_func(repr([mmh3object_purepython(e) for e in o]))

  elif t is dict:
    return hash_func(repr(sorted([(k, mmh3object_purepython(v)) for k, v in o.iteritems()])))

  elif t in (set, frozenset):
    return hash_func(repr(sorted([mmh3object_purepython(e) for e in o])))

  elif isinstance(o, (tuple, list)):
    return hash_func(repr([mmh3object_purepython(e) for e in o]))

  elif isinstance(o, (set, frozenset)):
      return hash_func(repr(sorted([mmh3object_purepython(e) for e in o])))

  elif isinstance(o, dict):
      return hash_func(repr(sorted([(k, mmh3object_purepython(v)) for k, v in o.iteritems()])))

  else:
    return hash_func(repr(o))

# Compatibility
for val in [
    True,
    None,
    1,
    0,
    "heo",
    u"heo",
    {"a": 1},
    {"a": {"b": set([3])}}
]:
    # print val
    # print mmh3object.mmh3object(val)
    # print mmh3object_purepython(val)
    assert mmh3object.mmh3object(val) == mmh3object_purepython(val)

N = 100000
# Performance
for val in [
    {"a": {"b": set([3])}},
    {
        "price": {
          "op": {
            "t": {
              "r": 0.2000000000000000111
            },
            "c": "EUR",
            "p": 7.7500000000000008882
          }
        },
        "hashes": {
          "parsed_noprice": "izN3HPc+33AYigJxY+7FXw==",
          "document": "EutG+msjMsx6XXXMsY6gDQ==",
          "root": "OaIvv9gWFIgpLEfyTaz1VQ==",
          "parsed": "BDxZPHX/9mR88zWIMQ+EJg==",
          "full_parsed": "/DZ0/i8EY6l7FrQBShJsqA=="
        },
        "detected_page_type": "product",
        "market": "fr_FR_EUR",
        "refresh_interval": 24,
        "fetch_flags": {
          "page_type_error": False,
          "delete_cp_error": False
        },
        "refetch": {
          "lastfail": None,
          "consecutivefails": 0,
        },
        "isparent": True
    }
]:
    print "Pure-python Performance for %s hashes of %s : %s" % (N, val, timeit.timeit('mmh3object_purepython(%s)' % (repr(val), ), number=N, setup="from __main__ import mmh3object_purepython"))
    print "Cython Performance for %s hashes of %s : %s" % (N, val, timeit.timeit('mmh3object.mmh3object(%s)' % (repr(val), ), number=N, setup="from __main__ import mmh3object"))

print "Tests OK!"
