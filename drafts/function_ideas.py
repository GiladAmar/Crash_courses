def load_latest(folder, matching, reading_func, specific_date):
    if specific_date is None:
        fname = latest matching decription
    else:
        fname = fname with specific_date
    
    try:
        if os.path.exists(fname):
            results = reading_func(fname)
        else:
            print(fname does not exist) + diagnose what dir fails
            raise Exception
    except Exception as e:
        print(failed to read file{fname} with error {e}.\n)
        raise Exception
    print(model loaded from fname)


from datetime import datetime


def save_dated(data, save_func, base_name, suffix, specific_date=None, description):

    if folder of base name does not exist:
        create it

    try:
        if specific-date is None:
            fname = f'{base_name}_{datetime.now()}{suffix}'
            save_func(data, fname)
    except Exception as e:
        print('data failed to save to {fname} from error {e}.\n')

    print(model/data saved as fname)

