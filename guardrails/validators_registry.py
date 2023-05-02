from collections import defaultdict
from typing import Union, List

from guardrails.datatypes import registry as types_registry

validators_registry = {}
types_to_validators = defaultdict(list)


def register_validator(name: str, data_type: Union[str, List[str]]):
    """Register a validator for a data type."""

    def decorator(cls: type):
        """Register a validator for a data type."""
        nonlocal data_type
        if isinstance(data_type, str):
            data_type = (
                list(types_registry.keys()) if data_type == "all" else [data_type]
            )
        # Make sure that the data type string exists in the data types registry.
        for dt in data_type:
            if dt not in types_registry:
                raise ValueError(f"Data type {dt} is not registered.")

            types_to_validators[dt].append(name)

        validators_registry[name] = cls
        cls.rail_alias = name
        return cls

    return decorator
