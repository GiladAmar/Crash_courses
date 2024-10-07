## Download from URL in parallel:
    aria2c -x 16 -s 16 [url]
    -i input_filename
    -d output_dir
    -o outfile_fname

input_filename contents:
```text
url1--no-cache-dir
    -o out_fname.mp3
url2
    -o out_fname2.mp3
```

## Rename Files/Folders:
change <pickle> for <pkl> in filenames
```bash
rename  's/pickle/pkl/' *
```

## Limit memory usage for following commands
```bash
ulimit -Sv 1000       # 1000 KBs = 1 MB
ulimit -Sv unlimited  # Remove limit
```

## tar files with progress bar
```bash
tar cf - /folder-with-big-files -P | pv -s $(du -sb /folder-with-big-files | awk '{print $1}') | gzip > big-files.tar.gz
```

## Delete Tiny images (empty files):
```bash
for i in {1..35..1};
    do for j in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z;
        do find chessboard_locations/$j$i/*/*/*.jpg -size -1b -delete;
    done;
done;
```

## Compress pdf
```bash
sudo apt-get install ghostscript
ps2pdf LARGE.pdf SMALL.pdf
```

Alternative:
```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=compressed_PDF_file.pdf input_PDF_file.pdf
```

dPDFSETTINGS	Description

    /prepress (default) Higher quality output (300 dpi) but bigger size
    /ebook              Medium quality output (150 dpi) with moderate output file size
    /screen             Lower quality output (72 dpi) but smallest possible output file size

## Splitting up mp3 files:
```bash
mp3splt -a -t 5.10 -o Lesson_01-@n -d Lesson_01 Lesson_01.mp3
```
```bash
-a              mp3splt auto-adjusts the split point with silence detection.
-t 5.10         Make files 5min 10s long
                (This length may vary a bit due to the -a option).
-o Lesson_01-@n Name the files as Lesson_01 followed by a track number.
-d Lesson_01    Put the files in a directory Lesson_01.
``````
And finally, Lesson_01.mp3 is the file you want to split.

## Restarting bash command on failure:
```bash
until !!; do echo Command interrupted, restarting in 5s ...; sleep 5; done
```

## Save bash output to file:
```bash
SomeCommand > SomeFile.txt
```
    |           || In terminal ||   In file   || existing  |
    |-----------||-------------||-------------||-----------|
    |   Syntax  ||StdOut|StdErr||StdOut|StdErr||   file    |
    |-----------||-------------||-------------||-----------|
    | >         ||  no  | yes  || yes  |  no  || overwrite |
    | >>        ||  no  | yes  || yes  |  no  ||  append   |
    |-----------||-------------||-------------||-----------|
    | 2>        || yes  |  no  ||  no  | yes  || overwrite |
    | 2>>       || yes  |  no  ||  no  | yes  ||  append   |
    |-----------||-------------||-------------||-----------|
    | &>        ||  no  |  no  || yes  | yes  || overwrite |
    | &>>       ||  no  |  no  || yes  | yes  ||  append   |
    |-----------||-------------||-------------||-----------|
    | | tee     || yes  | yes  || yes  |  no  || overwrite |
    | | tee -a  || yes  | yes  || yes  |  no  ||  append   |
    |-----------||-------------||-------------||-----------|
    | |& tee    || yes  | yes  || yes  | yes  || overwrite |
    | |& tee -a || yes  | yes  || yes  | yes  ||  append   |
    |-----------||-------------||-------------||-----------|


# What is using the camera:
```bash
lsof /dev/video0
```


```wc -l``` counts the number of ```\n```. So if your file doesn't end on one the count will not match up with the actual number or rows.