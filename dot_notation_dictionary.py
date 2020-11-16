
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
