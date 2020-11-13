

class DotNotationDict(dict):
		
	class __NoDefault(object):
		def __init__(self):
			super().__init__()
		
	"""docstring for DotNotationDict"""
	def __init__(self, *args, **kwargs):
		super(DotNotationDict, self).__init__(*args, **kwargs)
		

	def __getattr__(self, attribute_name):
		if attribute_name in self:
			return self[attribute_name]
		else:
			raise AttributeError(
				f'\'DotNotationDict\' object has no attribute \'{attribute_name}\''
			)


	def __setattr__(self, attribute_name, value):
		self[attribute_name] = value
