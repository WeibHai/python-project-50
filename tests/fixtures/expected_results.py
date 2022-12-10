result_stylish = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

result_plain = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

internal_representation = [{'type': 'removed', 'name': 'follow', 'value': False}, {'type': 'unchanged', 'name': 'host', 'value': 'hexlet.io'}, {'type': 'removed', 'name': 'proxy', 'value': '123.234.53.22'}, {'type': 'changed', 'name': 'timeout', 'value': 50, 'value2': 20}, {'type': 'added', 'name': 'verbose', 'value': True}]

result_stylish_r = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

result_plain_r = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

r_internal_representation = [{'type': 'root', 'name': 'common', 'value': None, 'children': [{'type': 'added', 'name': 'follow', 'value': False}, {'type': 'unchanged', 'name': 'setting1', 'value': 'Value 1'}, {'type': 'removed', 'name': 'setting2', 'value': 200}, {'type': 'changed', 'name': 'setting3', 'value': True, 'value2': None}, {'type': 'added', 'name': 'setting4', 'value': 'blah blah'}, {'type': 'added', 'name': 'setting5', 'value': {'key5': 'value5'}}, {'type': 'root', 'name': 'setting6', 'value': None, 'children': [{'type': 'root', 'name': 'doge', 'value': None, 'children': [{'type': 'changed', 'name': 'wow', 'value': '', 'value2': 'so much'}]}, {'type': 'unchanged', 'name': 'key', 'value': 'value'}, {'type': 'added', 'name': 'ops', 'value': 'vops'}]}]}, {'type': 'root', 'name': 'group1', 'value': None, 'children': [{'type': 'changed', 'name': 'baz', 'value': 'bas', 'value2': 'bars'}, {'type': 'unchanged', 'name': 'foo', 'value': 'bar'}, {'type': 'changed', 'name': 'nest', 'value': {'key': 'value'}, 'value2': 'str'}]}, {'type': 'removed', 'name': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'type': 'added', 'name': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

data_file1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}

data_file2 = {"timeout": 20, "verbose": True, "host": "hexlet.io"}

data_r_file1 = {
    "common": {
  "setting1": "Value 1",
  "setting2": 200,
  "setting3": True,
  "setting6": {
      "key": "value",
     "doge": {
      "wow": ""
        }
      }
    },
    "group1": {
       "baz": "bas",
       "foo": "bar",
      "nest": {
       "key": "value"
      }
    },
    "group2": {
       "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  }

data_r_file2 = {
  "common": {
      "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
        "key5": "value5"
    },
    "setting6": {
         "key": "value",
         "ops": "vops",
        "doge": {
         "wow": "so much"
      }
    }
  },
  "group1": {
     "foo": "bar",
     "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}
