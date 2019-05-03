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
until !!; do echo Command interrupted, restarting in 5s ...; sleep 5; done


Save bash output to file:
e.g.
    SomeCommand > SomeFile.txt

    ||          || visible in terminal ||   visible in file   || existing
    ||  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  ||   file
    ||==========++==========+==========++==========+==========++===========
    ||    >     ||    no    |   yes    ||   yes    |    no    || overwrite
    ||    >>    ||    no    |   yes    ||   yes    |    no    ||  append
    ||          ||          |          ||          |          ||
    ||   2>     ||   yes    |    no    ||    no    |   yes    || overwrite
    ||   2>>    ||   yes    |    no    ||    no    |   yes    ||  append
    ||          ||          |          ||          |          ||
    ||   &>     ||    no    |    no    ||   yes    |   yes    || overwrite
    ||   &>>    ||    no    |    no    ||   yes    |   yes    ||  append
    ||          ||          |          ||          |          ||
    || | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
    || | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append
    ||          ||          |          ||          |          ||
    || |& tee   ||   yes    |   yes    ||   yes    |   yes    || overwrite
    || |& tee -a||   yes    |   yes    ||   yes    |   yes    ||  append
