from tqdm import tqdm

# Basic
for i in tqdm(range(10)):
    do_something()


# In a map
from tqdm.contrib.concurrent import process_map

process_map(some_function, some_iterable, max_workers=2, desc="MyProcess")


# Multiprocessing
import multiprocessing as mp

def my_process(pos: int) -> None:
    with tqdm(desc=f"Process {pos}", total=100, position=pos) as progress:
        for _ in range(100):
            progress.update(1)

    # `tqdm` needs to get the global lock to avoid the progress bars 'jumping'
with mp.Pool(processes=n_cpu,
             initializer=tqdm.set_lock,
             initargs=(tqdm.get_lock(),)) as pool:
    pool.map(my_process, 8) # 8 CPUS


# Pandas Integration
tqdm.pandas(desc="Applying Transformation")
df.progress_apply(lambda x: x)


# In a Jupyter Notebook:
from tqdm.notebook import tnrange, tqdm

for i in tnrange(10):
    do_something()