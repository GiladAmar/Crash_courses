def get_relationships(df, columns=None):
    columns = columns if columns is not None else df.columns
    from itertools import product
    for col_i, col_j in product(columns, columns):
        if col_i == col_j:
            continue
        print(col_i, col_j, get_relation(df, col_i, col_j))


def get_relation(df, col1, col2):
    first_max = df[[col1, col2]].groupby(col1).count().max()[0]
    second_max = df[[col1, col2]].groupby(col2).count().max()[0]
    if first_max == 1:
        if second_max == 1:
            return 'one-to-one'
        else:
            return 'one-to-many'
    else:
        if second_max == 1:
            return 'many-to-one'
        else:
            return 'many-to-many'


def find_matches(df, col1, col2):
    #find relationships between category columns
    
    unique_matches_df = df[col1, col2].drop_duplicates()
    
    unique_matches_df.sort_values([col1. col2]).reset_index()
    return 
    

def to_sig_figures(x, n_sig):
    return np.format_float_positional(x, 
                                      precision=n_sig, 
                                      unique=False, 
                                      fractional=False,
                                      trim='k')

# Preprocessing


#Int defects

#painting

#mould_production

#baking

#melting

# furnace

# green sand

#pouring

#sand prep

#merging
