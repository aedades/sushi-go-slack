def get_num_args(args_spec):
        return len(args_spec[0])

def get_args(args_spec):
    return args_spec[0]

def assert_method_signature(args, args_spec):
        num_args = len(args)
        assert get_num_args(args_spec) == num_args
        assert get_args(args_spec) == args

