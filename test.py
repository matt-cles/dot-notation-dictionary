from dot_notation_dictionary import DotNotationDict

dot_not_dict = DotNotationDict(
	{
		'alpha': 'Value of alpha',
		'beta': 'Value of beta',
	},
	keyword_parameter_key_one=None,
	keyword_parameter_key_two='hello',
)

print(f'Values in the DotNotationDict: {dot_not_dict}\n')

print(f'Accessing \'alpha\' with brackets: {dot_not_dict["alpha"]}')
print(f'Accessing \'alpha\' with \'.get\': {dot_not_dict.get("alpha")}')
print(f'Accessing \'alpha\' with dot notation: {dot_not_dict.alpha}\n')

print(
	'Attempting to access an element that does not exist in the dict: ', 
	end=' ',
)
try:
	print(dot_not_dict.delta)
except AttributeError as err:
	print(f'raised ("{err}"), due to \'delta\' not being in dict')

print('\nAdding the element to the dict with dot notation...\n')
dot_not_dict.delta = 3

print(
	'Attempting to access the element now that it does exist in the dict: ',
	end=' ',
)
try:
	print(dot_not_dict.delta)
except AttributeError as err:
	print(f'raised {err}, due to \'delta\' not being in dict')


print(f'\nValues in the DotNotationDict: {dot_not_dict}\n')
print(dot_not_dict)
