
class DotDict(dict):
    """A class that extends dict to allow accessing keys as attributes."""

    def __init__(self, *args, **kwargs):
        """Initalize the DotDict.
        
        This method does nothing other that initialize the parent dict 
        with the passed args and kwargs.
        """
        super(DotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, attribute_name):
        """Get the dict value of the key where the attribute_name == key."""
        try:
            return self[attribute_name]
        except AttributeError:
            raise KeyError(
                f'KeyError: \'{attribute_name}\''
            )

    def __setattr__(self, attribute_name, attribute_value):
        """Set the dict value of the key where the attribute_name == key."""
        self[attribute_name] = attribute_value

class DefaultDotDict(dict):
    """A class that extends dict to allow accessing keys as attributes, 
    with a default values for keys when they are accessed but not assigned.
    """

    def __init__(self, default_value=None, *args, **kwargs):
        """Initalize the DefaultDotDict.
        
        This method sets the default value with the first argument then 
        initialize the parent dict with the remaining passed args and kwargs.
        """
        super(DefaultDotDict, self).__init__(*args, **kwargs)
        self.__default_value = default_value

    def __getattr__(self, attribute_name):
        """Get the dict value of the key where the attribute_name == key."""
        if '_DefaultDotDict__default_value' == attribute_name:
            super.__setattr__(self, attribute_name, attribute_value)
        else:
            return self[attribute_name]

    def __setattr__(self, attribute_name, attribute_value):
        """Set the dict value of the key where the attribute_name == key."""
        if '_DefaultDotDict__default_value' == attribute_name:
            super.__setattr__(self, attribute_name, attribute_value)
        else:
            self[attribute_name] = attribute_value

    def __missing__(self, key):
        """Set the missing key to the default value if it does not exist."""
        self[key] = self.__default_value
        return self[key]

class NestingDotDict(dict):
    """A class that extends dict to allow accessing keys as attributes.
    
    This class automatically converts and dict class to NestingDotDicts 
    when accessed from this class. 
    """

    def __init__(self, *args, **kwargs):
        """Initalize the NestingDotDict.
        
        This method does nothing other that initialize the parent dict 
        with the passed args and kwargs.
        """
        super(NestingDotDict, self).__init__(*args, **kwargs)

    def __getattr__(self, attribute_name):
        """Get the dict value of the key where the attribute_name == key."""
        try:
            value = self[attribute_name]
            if (
                not isinstance(value,   NestingDotDict) and
                isinstance(value, dict)
            ):
                # If the attribute is a dict, but not already a 
                # NestingDotDict, then convert it to a NestingDotDict 
                # and override the current attribute.
                value = NestingDotDict(value)
                self[attribute_name] = value
            return value
        except AttributeError:
            raise KeyError(
                f'KeyError: \'{attribute_name}\''
            )

    def __setattr__(self, attribute_name, attribute_value):
        """Set the dict value of the key where the attribute_name == key."""
        if (
            not isinstance(attribute_value,   NestingDotDict) and
            isinstance(attribute_value, dict)
        ):
            attribute_value = NestingDotDict(attribute_value)
        self[attribute_name] = attribute_value
