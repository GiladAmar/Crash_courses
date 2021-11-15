import sys
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")

#positional arguments:
parser.add_argument("echo",
                    help="echo the string you use here",
                    type = int, #<int/float/str/...>
                    choices=[0, 1, 2]) # limit options to these
nargs=2 #specify how many values to expect after the argument nargs=1 will make a list of len==1
        #nargs='?' will make a list unless there is one, in which case it will be that value

# To add a short version
parser.add_argument("f", "full_option", ...)

#optional arguments:
parser.add_argument("--verbosity",
                    help="increase output verbosity")

# a value of None is assigned unless a default is given
# to treat as a flag i.e assumed to be false unless the flag is present you can use:
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
# alt_actions:
# 'count' : means -vv is 2 but -v is one

# * working assumption is that arguments with - or -- are optional otherwise ir is required
# This can be changes witht the required parameter
parser.add_argument('--foo', required=True)

# Another assumptions is that the name given to the argument minus -- or -- is tha name of the variable.
# This can be changes with dest='this_var_name'

# alternatively 'store_false'

# Mutually exclusive parameters
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# add n items to argument that is a list:
parser.add_argument('--foo', action='append')
# parser.parse_args('--foo 1 --foo 2'.split())

args = parser.parse_args()

# args are treated as strings unless specified otherwise


# allow to change std input and output of files:
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=sys.stdin)

parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'),
                    default=sys.stdout)



# For short options (options only one character long), the option and its value can be concatenated:
# 
# parser.parse_args(['-xX'])



# For long options (options with names longer than a single character), the option and value can also be passed as a single command-line argument, using = to separate them:
parser.parse_args(['--foo=FOO'])


# Several short options can be joined together, using only a single - prefix, as long as only the last option (or none of them) requires a value:



# The parse_args() method by default allows long options to be abbreviated to a prefix, if the abbreviation is unambiguous (the prefix matches a unique option):



# Many programs split up their functionality into a number of sub-commands, for example, the svn program can invoke sub-commands like svn checkout, svn update, and svn commit.
subparsers = parser.add_subparsers(help='Arguments for specific dataset types.', dest='dataset_type')
subparsers.required = True

# create the parser for the "foo" command
parser_foo = subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

# create the parser for the "bar" command
parser_bar = subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(func=bar)


ArgumentParser.add_argument_group(title=None, description=None)
#group args together in help rather than letting it split into positional and optional arguments

ArgumentParser.add_mutually_exclusive_group(required=False)


#add params that dont need to be set
parser.set_defaults(bar=42, baz='badger')



# If you want comre complex criteria for allowable parameters:
def check_args(parsed_args):
    """ Function to check for inherent contradictions within parsed arguments.
    For example, batch_size < num_gpus
    Intended to raise errors prior to backend initialisation.

    Args
        parsed_args: parser.parse_args()

    Returns
        parsed_args
    """

    if parsed_args.multi_gpu > 1 and parsed_args.batch_size < parsed_args.multi_gpu:
        raise ValueError(
            "Batch size ({}) must be equal to or higher than the number of GPUs ({})".format(parsed_args.batch_size,
                                                                                             parsed_args.multi_gpu))

    if parsed_args.multi_gpu > 1 and parsed_args.snapshot:
        raise ValueError(
            "Multi GPU training ({}) and resuming from snapshots ({}) is not supported.".format(parsed_args.multi_gpu,
                                                                                                parsed_args.snapshot))

    if parsed_args.multi_gpu > 1 and not parsed_args.multi_gpu_force:
        raise ValueError("Multi-GPU support is experimental, use at own risk! Run with --multi-gpu-force if you wish to continue.")

    if 'resnet' not in parsed_args.backbone:
        warnings.warn('Using experimental backbone {}. Only resnet50 has been properly tested.'.format(parsed_args.backbone))

    return parsed_args


# to run 1 function if one arg is used or func2 if arg2 is used:
command1_parser.set_defaults(func=command1)