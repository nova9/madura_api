## Welcome to madura_api GitHub Page

This is a python module that enables the ability to access madura online dictionary from your python code.

### Install it
> pip install madura-api

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
  ['n.', 'ප්\u200dරාණවත්කම'],
  ['n.', 'ප්\u200dරාණියා'],
  ['n.', 'පාණ'],
  ['n.', 'මිනිසුන් ගේ වගතුග'],
  ['Psy.', 'වය'],
  ['n.', 'විත කථාව'],
  ['Law.', 'විතකාලය'],
  ['n.', 'විතය'],
  ['n.', 'සමාජය']
]

```
