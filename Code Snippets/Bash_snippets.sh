Download from URL in parallel:
    aria2c -x 16 -s 16 [url]


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