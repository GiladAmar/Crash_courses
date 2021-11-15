from pathlib import Path

# OS insensitive
data_folder = Path("source_data/text_files/")

# Easy append not os.join(a,b)
file_to_open = data_folder / "raw_data.txt"

#Easy read contents
print(file_to_open.read_text())


filename.posix() -> string path
filename.name -> "raw_data.txt"

filename.suffix -> "txt"

filename.stem -> "raw_data"

filename.exists() -> True/False

filename.absolute() -> '/Desktop/source_data/text_files/raw_data.txt'

filename.isdir() -> True/False
filename.home()
cwd
is_file

mkdir
rename
rmdir


p.glob('**/*.py') -> iterator

p = Path('.')

p.parts()

# Pathlib
from pathlib import Path
from typing import Union

PathLike = Union[str, Path]

output_dir = Path(output_dir) / "bob_stats" / current_time

model_dir = Path(model_dir)
scaler_path = model_dir.parent / "standard_scaler.joblib"
encoder_file = model_dir / "encoder.h5"
train_file = model_dir / "train.parquet"
