class DefaultDotNotationDict(dict):
	"""A Class that extends the standard 'dict' class."""
		
	class __NoDefault(object):
		"""An empty Class, used to denote no default value."""
		def __init__(self):
			super().__init__()

	def __init__(self, default=__NoDefault(), *args, **kwargs):
		super(DefaultDotNotationDict, self).__init__(*args, **kwargs)
		if isinstance(
			default, 
			DefaultDotNotationDict._DefaultDotNotationDict__NoDefault,
		):
			self.__use_default = False
		else:
			self.__use_default = True
			self.__default_value = default

	def __getattr__(self, attribute_name):
		if attribute_name in self:
			return self[attribute_name]
		elif self._DefaultDotNotationDict__use_default:
			value = self._DefaultDotNotationDict__default_value
			self[attribute_name] = value
			return self[attribute_name]
		else:
			raise AttributeError(
				f'\'DotNotationDict\' object has no attribute \'{attribute_name}\''
			)

	def __setattr__(self, attribute_name, value):
		if not '_DefaultDotNotationDict__' in attribute_name:
			self[attribute_name] = value
		else:
			super.__setattr__(self, attribute_name, value)


class DotNotationDict(DefaultDotNotationDict):
	"""A Class that extends the standard 'dict' class."""
	
	def __init__(self, *args, **kwargs):
		super(DotNotationDict, self).__init__(
			DefaultDotNotationDict._DefaultDotNotationDict__NoDefault(),
			*args,
			**kwargs,
		)
