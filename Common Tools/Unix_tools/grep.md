#GREP
Find search_string withing a folder or file

```grep search_string folder_or_file```

## Options
    -r      Recursive
    -R      Recursive, follow symbolic links

    -i      Ignore_case
    -v      Invert (show lines that don't match)
    -w      The match must be the full word

    -E      Use regex search_string
    -e      Add a search term
    -x      Entire line match only

    -c      Count matches
    -n      Display line number of matches
    -m      Max matches

    -A x    Show x lines after matching term
    -B x    Show x lines before matching term
    -C x    Show x lines before and after matching term

    -l      Display filenames containing matching text
    -L      Display filenames NOT containing matching text

Pipe search results into less for easier viewing and searching:
```
grep search_string *.c | less
```

Pipe results from another query to grep:
```
pip freeze | grep tensorflow
```

Find filename containing "Aug" and sort by filesize:
```
ls -l | grep "Aug" | sort +4n
```
