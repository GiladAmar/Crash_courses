# Regex


Case-sensitive by default

|      Symbol      | Description                                                                                    |
|:----------------:|:-----------------------------------------------------------------------------------------------|
|        \d        | Digits 0-9                                                                                     |
|        \D        | Non-digit                                                                                      |
|        .         | Single wildcard matching anything except a newline. <br/>Use escape to match a period ```\.``` |
|      [abc]       | Single wildcard of specified list in []                                                        |
|     [A-Za-z]     | Single wildcard in whole char range                                                            |
|      [3-9]       | Digits 3 to 9                                                                                  |
|      [^abc]      | Single wildcard NOT in list [^ ]                                                               |
|        \w        | Metacharacter.<br/>Equivalent to [A-Za-z0-9_].                                                 |
|        \W        | Non-alphanumeric.<br/>Equivalent to [^a-zA-Z0-9_]                                              |
|       a{3}       | Makes 3 repetitions of a                                                                       |
|      a{1-3}      | Some engines allow a specified range of repetitions                                            |
|     [wxy]{5}     | Five characters of either wxy                                                                  |
|      .{2,6}      | Any two to six characters                                                                      |
|        c*        | 0 or more c's                                                                                  |
|        c+        | 1 or more c's                                                                                  |
|       \d+        | 1 or more digit                                                                                |
|      [abc]+      | 1 or more of a, b or c.                                                                        |
|       ab?c       | b is optional, may or may not be there                                                         |
|       [*+]       | **NB** Special chars don't have meaning inside a set.<br/>This just matches * or +             |
|       ' '        | Space                                                                                          |
|        \t        | Tab                                                                                            |
|        \n        | Newline                                                                                        |
|        \r        | Carriage return                                                                                |
|        \b        | Boundary between word and non word                                                             |
|        \B        | Not a word boundary e.g. never at the end of a sentence                                        |
|        \s        | Matches ALL space types                                                                        |
|        \S        | Non-whitespace                                                                                 |
|      ^___$:      | ^ is the start and $ the end of the line                                                       |
|     (X)....      | Whole string is matched but only part in () is returned                                        |
|      (X(Y))      | Can capture multiple, even nested items                                                        |
| (cat &#124; dog) | The OR operator                                                                                |

Make the next sequence case-insensitive

    (?i) - Signifies that the next sequence is case-insensitive.


| Symbol |     Description     |
|:------:|:-------------------:|
|   ?=   | Positive Lookahead  |
|   ?!   | Negative Lookahead  |
|  ?<=   | Positive Lookbehind |
|  ?<!   | Negative Lookbehind |

Look behind/aheads in parentheses is not returned

| Greedy |  Lazy  |
|:------:|:------:|
|   *    |   *?   |
|   +    |   +?   |
|   ?    |   ??   |
|  {n}   |  {n}?  |
|  {n,}  | {n,}?  |
| {n,m}  | {n,m}? |
\
Add a ```?``` to a quantifier to make it lazy.

Example: "stackoverflow"
  - greedy: ``s.*o`` matches ```stackoverflo```
  - lazy: ``s.*?o`` matches ```stacko```

## Useful Cases
Is email

    (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

Find urls

    (https?:\/\/)(www\.)?(?<domain>[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6})(?<path>\/[-a-zA-Z0-9@:%_\/+.~#?&=]*)?

Is Prime

    /^1?$|^(11+?)\1+$/

Finding all chars from a different character-set e.g Chinese:
```[\x{4e00}-\x{9fa5}]+```
or hebrew
```[a-z\u0590-\u05fe]+```

Year Range
```\b(?:19|20)\d{2}\b``` - match all years between 1900 and 2099

------------------------------------------------------------------------------
## TODO
- Regex in python std.
- Regex in Pandas
- Regex in bash
- Test regex at https://regex101.com/


```\b(0?[1-9]|[12]\d|3[01])([\/\-])(0?[1-9]|1[012])\2(\d{4})```
The only new concept here is that we're using \2 to match the second capture group, which is the divider (/ or -).

Replace date formats:
```python
import re
regex = r'\b(0?[1-9]|[12]\d|3[01])([ \/\-])(0?[1-9]|1[012])\2(\d{4})'
test_str = "Today's date is 18/09/2017"
subst = r'\3\2\1\2\4'
result = re.sub(regex, subst, test_str)
print(result)
```

```python
# Named capture groups
import re
import urllib.request

html = str(urllib.request.urlopen("https://moz.com/top500").read())
regex = r"(https?:\/\/)(www\.)?(?P<domain>[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6})(?P<path>\/[-a-zA-Z0-9@:%_\/+.~#?&=]*)?"
matches = re.finditer(regex, html)

for match in matches:
  print(match.group('domain'))
```
