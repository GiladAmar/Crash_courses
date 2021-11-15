## Compression:

```bash
tar -cvf "compress, verbose, file/archive"
    -z -> tar.gz
    -j -> bz2
```
e.g.
```bash
tar -cvzf output.tar folder_contents/ another_whole_folder
```

In terms of archive size:

    tar > zip > gz > bz2

gz - a compressed collection. Requires whole file to be extracted together
zip -  a collection of separately compressed files
### Add specific file

```bash
tar -r it.tar add_this_file.doc
```

## Extraction

```bash 
tar -xvf Extract
    -t   List content
```

e.g.

```bash 
tar -xvf input.tar
```

### Extract specific file

```bash 
tar -xvf it.tar it.doc  #or *.doc
```