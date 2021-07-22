# madura_api
A Python API to access online madura dictionary

# Usage
Install the package

```python
pip3 install madura-api
```

## Example 1

```python
from madura_api import translate

result_list=translate('Home')
print(result_list)
```

*result_list* is a list of lists like this,

```python
[
    ['n.', 'ආල'],
    ['n.', 'ආලය'],
    ['n.', 'උත්පත්ති ස්ථානය'],
    ['n.', 'උන්හිටි තැන'],
    ['n.', 'ගෘහය'],
    ['n.', 'ගෙදර'],
    ['a.', 'ගෙදර පිළිබඳ වූ'],
    ['vi.', 'ගෙදරට ආපසු පැමිණෙනවා'],
    ['n.', 'ගේ'],
    ['n.', 'ගේදොර'],
    ['n.', 'ඝර'],
    ['n.', 'නිවස'],
    ['n.', 'නිවහන'],
    ['n.', 'නිවාසය'],
    ['n.', 'නිවෙස'],
    ['Ele.', 'නිවෙසනවා'],
    ['Ele.', 'නිවෙසීම'],
    ['n.', 'පදිංචිය'],
    ['Soc.', 'පවුල'],
    ['Soc.', 'ස්වදේශ'],
    ['n.', 'සියරට']
]
```

## Example 2

```python
from madura_api import translate

result_list=translate('පොත')
print(result_list)
```

*result_list* is a list of lists like this,

```python
[
    ['n.','bood'],
    ['n.', 'book'],
    ['n.', 'scroll']
]
```
---

- If there is no result, translate function will return False

## Example 3

```python
from madura_api import translate

result_list=translate('meen')
print(result_list)
```
```python
False
```

# Advanced Usage (Suggestions)

## Example 4

This is how you translate something if you wanna work with suggestions

```python
import madura_api

result=madura_api.Translate('home')
print(result.list)
```
```python
[
    ['n.', 'ආල'],
    ['n.', 'ආලය'],
    ['n.', 'උත්පත්ති ස්ථානය'],
    ['n.', 'උන්හිටි තැන'],
    ['n.', 'ගෘහය'],
    ['n.', 'ගෙදර'],
    ['a.', 'ගෙදර පිළිබඳ වූ'],
    ['vi.', 'ගෙදරට ආපසු පැමිණෙනවා'],
    ['n.', 'ගේ'],
    ['n.', 'ගේදොර'],
    ['n.', 'ඝර'],
    ['n.', 'නිවස'],
    ['n.', 'නිවහන'],
    ['n.', 'නිවාසය'],
    ['n.', 'නිවෙස'],
    ['Ele.', 'නිවෙසනවා'],
    ['Ele.', 'නිවෙසීම'],
    ['n.', 'පදිංචිය'],
    ['Soc.', 'පවුල'],
    ['Soc.', 'ස්වදේශ'],
    ['n.', 'සියරට']
]
```

If you try to translate something that can't be translated it'll give you a suggestion list like this,

## Example 5
```python
import madura_api

result=madura_api.Translate('meen')
print(result.list)
```
```python
[
    'meed',
    'meek',
    'meekness',
    'meerkat',
    'meerschaum',
    'meet',
    'meeting',
    'meeting adjourned', 
    'meeting annual general',
    'meeting extraordinary'
]
```

But you will need to know if the output you get is a suggestion or not. This how you do that,

## Example 6
```python
import madura_api

result=madura_api.Translate('meen')
print(result.is_a_suggestion)
```
```python
True
```

# Miscellaneous Stuff

If you think *madura_api* is a pain in the ass to type, do this

```python
import madura_api as mapi
```
