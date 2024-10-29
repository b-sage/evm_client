from evm_client.parsers.utils import underscore_to_camelcase

class ParsedObject:

    def as_dict(self):
        return {underscore_to_camelcase(k).rstrip('_'): v for k,v in vars(self).items()}

    def to_dict(self):
        d = self.as_dict()
        return {k: v for k, v in d.items() if v is not None}
