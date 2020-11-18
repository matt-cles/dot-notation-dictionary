# dot-notation-dictionary

A few simple python dict subclasses.

These subclasses allow for accessing the dictionary values by using the keys as class attributes.

For example, imagine a `DotDict` class instance named `d` with key value pairs: `{'alpha': 1, 'beta': 2}`

The value of the 'alpha' key can be accessed by calling `d.alpha` as well as using the standard dict bracket notation: `d['alpha']` or the get method: `d.get('alpha')`.

## Dict Subclasses

### DotDict

Basic dict subclass. 

### DefaultDotDict

Dict subclass that allows for a default value for keys that do not have a value when they are first accessed.
 
### NestingDotDict

Dict subclass that automatically converts nested dicts to NestingDotDicts. This allows for creating a single NestingDotDict to access the value of any number of nested dicts with dot notation.
