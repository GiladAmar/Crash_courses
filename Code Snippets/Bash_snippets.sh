Download from URL in parallel:
    aria2c -x 16 -s 16 [url]
    -i input_filename
    -d output_dir
    -o outfile_fname

    inputfile_contents:
        url1
            -o out_fname.mp3
        url2
            -o out_fname2.mp3


Rename Files/Folders:
    rename  's/pickle/pkl/' * #change <pickle> for <pkl> in filenames


# 3. Limit memory usage for following commands
    ulimit -Sv 1000       # 1000 KBs = 1 MB
    ulimit -Sv unlimited  # Remove limit


# tar files with progress bar
    tar cf - /folder-with-big-files -P | pv -s $(du -sb /folder-with-big-files | awk '{print $1}') | gzip > big-files.tar.gz


rsync example:
    rsync -hztv --partial --progress gilad.amar@omni-intern-gpu.dp:*.jpg /home/giladamar/Documents/DISA_renders/


Delete Tiny images (empty files):
    for i in {1..35..1};
        do for j in A B C D E F G H I J K L M N O P Q R S T U V W X Y Z;
            do find chessboard_locations/$j$i/*/*/*.jpg -size -1b -delete;
        done;
    done;


Compress pdf:
    sudo apt-get install ghostscript
    ps2pdf LARGE.pdf SMALL.pdf


Splitting up mp3 files:
    mp3splt -a -t 5.10 -o Lesson_01-@n -d Lesson_01 Lesson_01.mp3
        -a tells mp3splt to auto-adjust the split point with silence detection.
        -t 5.10 tells it to make the files 5 minutes and 10 seconds long since the file is a little over 30 minutes long. (This length may vary a bit due to the -a option).
        -o Lesson_01-@n tells it to name the files as Lesson_01 followed by a track number.
        -d Lesson_01 tells it to put the files in a directory called Lesson_01.
        And finally, Lesson_01.mp3 is the file you want to split.


#Restarting bash command on failure:
until !!; do echo Command interrupted, restarting in 5s ...;sleep 5;done

#TODO
Save bash output to file:
    Yes it is possible, just redirect the output to a file:

    SomeCommand > SomeFile.txt
    Or if you want to append data:

    SomeCommand >> SomeFile.txt
    If you want stderr as well use this:

    SomeCommand &> SomeFile.txt
    or this to append:

    SomeCommand &>> SomeFile.txt
    if you want to have both stderr and output displayed on the console and in a file use this:

    SomeCommand 2>&1 | tee SomeFile.txt

    Please note that the n.e. in the syntax column means "not existing".
There is a way, but it's too complicated to fit into the column. You can find a helpful link in the List section about it.

          || visible in terminal ||   visible in file   || existing
  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  ||   file
==========++==========+==========++==========+==========++===========
    >     ||    no    |   yes    ||   yes    |    no    || overwrite
    >>    ||    no    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
   2>     ||   yes    |    no    ||    no    |   yes    || overwrite
   2>>    ||   yes    |    no    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
   &>     ||    no    |    no    ||   yes    |   yes    || overwrite
   &>>    ||    no    |    no    ||   yes    |   yes    ||  append
          ||          |          ||          |          ||
 | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
 | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    || overwrite
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
|& tee    ||   yes    |   yes    ||   yes    |   yes    || overwrite
|& tee -a ||   yes    |   yes    ||   yes    |   yes    ||  append
List:
command > output.txt

The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

command >> output.txt

The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

command 2> output.txt

The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

command 2>> output.txt

The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

command &> output.txt

Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, it gets overwritten.

command &>> output.txt

Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, the new data will get appended to the end of the file..

command | tee output.txt

The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, it gets overwritten.

command | tee -a output.txt

The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

(*)

Bash has no shorthand syntax that allows piping only StdErr to a second command, which would be needed here in combination with tee again to complete the table. If you really need something like that, please look at "How to pipe stderr, and not stdout?" on Stack Overflow for some ways how this can be done e.g. by swapping streams or using process substitution.

command |& tee output.txt

Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, it gets overwritten.

command |& tee -a output.txt

Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, the new data will get appended to the end of the file.