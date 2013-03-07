Simple module to wrap a method with another methid pre-entry, designed to be used at runtime in conjunction with code.interact() to assist in debugging python applications.


```python
...after code.interact()
def my_wrapper(*args, **kwargs):
	print "I'm a wrapper"
	return args, kwargs

>>> infection.infect(original_function, my_wrapper, local=globals())
>>> original_function()
"I'm a wrapper!"
<original function called>
>>> infection.list_infected()
Infected methods:
original_function -> my_wrapper
>>> infection.clear_infected()
Clearing infections:
Removing original_function -> my_wrapper
Infection removed: original_function
>>> original_function()
<original function called>
>>> ^Z
```

Primary use is for light function call inspection, modification of input arguments for testing and will eventually support inspection of wrapped function return values.