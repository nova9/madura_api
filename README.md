# madura_api
A Python API to access online madura dictionary

## Usage
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

```
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

```
[
    ['n.','bood'],
    ['n.', 'book'],
    ['n.', 'scroll']
]
```
---
# If there is no result, translate function will return a suggestion list inside another list like this,

## Example 3

```python
from madura_api import translate

result_list=translate('meen')
print(result_list)
```

*result_list* is a list of lists like this,

```
[
    ['meed'],
    ['meek'],
    ['meekness'],
    ['meerkat'],
    ['meerschaum'],
    ['meet'],
    ['meeting'],
    ['meeting adjourned'],
    ['meeting annual general'],
    ['meeting extraordinary']
]
```