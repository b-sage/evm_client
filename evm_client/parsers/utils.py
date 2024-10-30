
def assert_int(item):
    assert type(item) == int or item is None

def assert_str(item):
    assert type(item) == str or item is None

def underscore_to_camelcase(value):
    def camelcase(): 
        yield str.lower
        while True:
            yield str.capitalize

    c = camelcase()
    return "".join(next(c)(x) if x else '_' for x in value.split("_"))

