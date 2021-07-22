## Welcome to madura_api GitHub Page

This is a python module that can be used to access madura online dictionary from your python code.

### Install it
```python
pip install madura-api
```

### Use it
```python
import madura_api
result=madura_api.Translate('life')
print(result.list)
```
```python
[
  ['Civ.', 'ආයුෂ'],
  ['n.', 'ජීව'],
  ['n.', 'ජීවය'],
  ['n.', 'ජීවි'],
  ['n.', 'දිවිය'],
  ['a.', 'දිවිහිම්'],
  ['n.', 'පණ'],
  ['n.', 'පණ ඇති සත්තු'],
  ['n.', 'ප්‍රාණවත්කම'],
  ['n.', 'ප්‍රාණියා'],
  ['n.', 'පාණ'],
  ['n.', 'මිනිසුන් ගේ වගතුග'],
  ['Psy.', 'වය'],
  ['n.', 'විත කථාව'],
  ['Law.', 'විතකාලය'],
  ['n.', 'විතය'],
  ['n.', 'සමාජය']
]

```
