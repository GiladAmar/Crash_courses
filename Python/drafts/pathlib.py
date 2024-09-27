from pathlib import Path

# OS Insensitive and nicer than os.path
Path.home()
Path.cwd()

# OS insensitive
folder = Path("source_data/text_files/")
file = folder / "texty.txt" # Easy append not os.join(a,b)

##  Attributes
file.name # "texty.txt"
file.stem # "texty"
file.suffix # ".txt"
file.parents # Generator going up one each time

file.stat().st_size # Filesize (For a link this is just the name size, use st_rsize instead)
file.stat().st_mtime # modified time



# Methods
file.mkdir(parents=True, exist_ok=True)

file.exists()
file.absolute() # '/Desktop/source_data/text_files/raw_data.txt'

file.isdir()
file.isfile()
file.posix() # string path
file.parts() # break up path into parts

# Search
path.glob('**/*.py')
path.rglob("*.txt") # Recursive Glob
folder.iterdir() # Generator listing all folders/files in path

# Rename / Delete / Move
file.rename()
folder.rmdir() # Delete did, but only if empty
file.match(pattern, case_sensitive=None) # See if the path matches some regex

# To refer to another file in the same directory easily
with_stem("other_file")
with_suffix(".other_suffix")
with_name("whole_name_altogether.tar.gz")


## Reading and writing:

# Read
file_to_open.read_text()
image_file.read_bytes()

# Write
file.write_text(b'Binary file contents')
file.write_bytes(b'Binary file contents')

# Opening
with p.open(mode='r') as f:
    f.readline()

# Ownership
file.owner()
file.group()
file.chmod() # Change permissions
