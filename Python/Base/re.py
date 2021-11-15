r"""test_emails.txt
$"""

import re
re.findall(pattern, string)

re.search()
# matches the first instance of a pattern in a string, and returns it as a re match object.
# we can’t display the name and email address by printing it directly.
# Instead, we have to apply the group() function to it first.
# We’ve printed both their types out in the code above.
# As we can see, group() converts the match object into a string.
# We can also see that printing match displays properties beyond the string itself, whereas printing match.group() displays only the string.

re.split("@", line)


re.sub()
# takes three arguments. The first is the substring to substitute, the second is a string we want in its place, and the third is the main string itself.
