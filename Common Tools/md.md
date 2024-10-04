# Headers
# Header 1
## Header 2
### Header 3

## Lists:
### Numbered
1. One
2. Two
3. Three

### Points
- 1st level
- 1st level too
    - 2nd level
        - 3rd level

### Checkboxes
- [ ] Empty checkbox
- [X] Full checkbox

## Text Formatting
*italic* or _italic_

**bold**

~~strikethrough~~

x<sup>supertext</sup>

x<sub>subtext<sub>

==highlight==

## Horizontal rules
* * *

***

---

***

___


## Links

* Letters convert to lower case
* Leading and trailing whitespace are removed
* formatting is removed

[header link](#header-1)

[url](http://hyperopt.github.io/hyperopt/)


## Code Blocks:
Code highlighting can be specified for bash, python etc... `inline code`
```python
for i in range(5):
    print("helloworld")
```


## Dropdowns
<details>
  <summary>
  Click here for more
  </summary>
This is more.
</details>


## Image:
You can set height, width, alignment, link, theme-sensitivity

<img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg" width="400x;" height="300px;"/>


### Alignment:
<p align="center"><a href="https://github.com/bregman-arie/system-design-notebook"><img src="https://upload.wikimedia.org/wikipedia/commons/d/d3/Albert_Einstein_Head.jpg"/></a></p>

### Theme
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
</picture>


## Button:
[![License: CC BY-NC-ND 3.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/3.0/)


## Emoji
:pencil: :) &nbsp; :bowtie:

# Table:
| Left aligned | Right aligned | Center aligned |
|:-------------|--------------:|:--------------:|
| Content Cell |  Content Cell |  Content Cell  |
| Content Cell |  Content Cell |  Content Cell  |


## Quotes
 > Blockquote
 >> Nested Blockquote
 > 


## Alerts
On GitHub these appear with a coloured bar on the left, emoji symbol and formatting.


> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.


## Escape formating
\*This is not in bold now\*


## Footnotes
Here is a simple footnote [^1].

[^1]: My footnote text.

## Markdown Comments
<!-- This content will not appear in the rendered Markdown -->

# Maths
Latex on some platforms:

When $a \ne 0$, there are two solutions to $(ax^2 + bx + c = 0)$ and they are 
$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$