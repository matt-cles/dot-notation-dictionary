from dot_notation_dictionary import DotDict, DefaultDotDict

dot_not_dict = DotDict(
	{
		'alpha': 'Value of alpha',
		'beta': 'Value of beta',
	},
	keyword_parameter_key_one=None,
	keyword_parameter_key_two='hello',
)

print(f'Values in the DotDict: {dot_not_dict}\n')

print(
	'Testing if the DotDict is still evaluated as a dict: '
	f'{isinstance(dot_not_dict, dict)}'
)

print(f'Accessing \'alpha\' with brackets: {dot_not_dict["alpha"]}')
print(f'Accessing \'alpha\' with \'.get\': {dot_not_dict.get("alpha")}')
print(f'Accessing \'alpha\' with dot notation: {dot_not_dict.alpha}\n')

print(
	'Attempting to access an element that does not exist in the dict: ', 
	end=' ',
)
try:
	print(dot_not_dict.delta)
except KeyError as err:
	print(f'raised ("{err}"), due to \'delta\' not being in dict')

print('\nAdding the element to the dict with dot notation...\n')
dot_not_dict.delta = 3

print(
	'Attempting to access the element now that it does exist in the dict: ',
	end=' ',
)
try:
	print(dot_not_dict.delta)
except KeyError as err:
	print(f'raised {err}, due to \'delta\' not being in dict')


print(f'\nValues in the DotDict: {dot_not_dict}\n')

default_dot_not_dict = DefaultDotDict(0, {'a': 1, 'c': 1,})
print(default_dot_not_dict)
print(default_dot_not_dict.b)
print(default_dot_not_dict)
print(default_dot_not_dict['d'])
print(isinstance(default_dot_not_dict, dict))
print(default_dot_not_dict)