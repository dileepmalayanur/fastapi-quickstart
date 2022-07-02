
def repeat_to_at_least_length(s, wanted):
    return s * (wanted//len(s) + 1)

def parse_boolean(str_val: str):
    return str_val in ['True', 'true', True]