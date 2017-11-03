aria2c -x 16 -s 16 [url] # Download from URL in parallel


rename  's/pickle/pkl/' * #change <pickle> for <pkl> in filenames


3. Limit memory usage for following commands
ulimit -Sv 1000       # 1000 KBs = 1 MB
ulimit -Sv unlimited  # Remove limit
