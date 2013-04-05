class Template(object):
	'''
		A template for senteces.
		After create a template, you can create sentences from it, using the createSentence() function.
	'''
	def __init__(self, templateString, paramTypes):				
		self._templateString = templateString
		self._paramTypes = paramTypes
		
	def createSentance(self, parametes):
		if len(parametes) != len(self._paramTypes):
			raise "error"
		
		specificParams = []
		for i in xrange(len(parametes)):
			if parametes[i] is self._paramTypes[i]:
				raise "error"
				
			specificParams.append(self._paramTypes[i](parametes[i]))
			
		return Sentence(self, specificParams)
	
	def format(self, *args, **kwargs):
		return self._templateString.format(*args, **kwargs)
	
class Sentence(object):
	def __init__(self, template, specificParams):
		self._template = template
		self._specificParams = specificParams
		
	def __str__(self):
		return self._template.format(*self._specificParams)
		
	def __add__(self, other):
		if len(self._specificParams) != len(other._specificParams):
			raise "error"
			
		specificParams = []
		for index in xrange(len(self._specificParams)):
			specificParams.append(self._specificParams[index] + other._specificParams[index])
		
		return Sentence(self._template, specificParams)

	def __getitem__(self, index):
		return self._specificParams[index]
		
class MeasurableInt(object):
	def __init__(self, value, single, plurale):
		self._single = single
		self._plurale = plurale
		self.value = value
		if value == 1:
			self.unit = single
		else:
			self.unit = plurale
		
	def __add__(self, other):
		return MeasurableInt(self.value + other.value, self._single, self._plurale)

class SMeasurableInt(MeasurableInt):
	'''
		A MeasurableInt, where the plural form the unit, is the same as the single,
		with an "s" at the end.
	'''
	def __init__(self, value, single):
		super(SMeasurableInt, self).__init__(value, single, single +"s")
	
class MinuteUnit(SMeasurableInt):
	def __init__(self, value):
		super(MinuteUnit, self).__init__(value, "minute")

class KilometerUnit(SMeasurableInt):
	def __init__(self, value):
		super(KilometerUnit, self).__init__(value, "kilometer")



		
## Example:
t = Template("I ran {0} km", [int])
s = t.createSentance([10])
s2 = t.createSentance([20])
s3 = s + s2
print(s3)

## Example:
t = Template("I ran {0.value} {0.unit} in {1.value} {1.unit}", [KilometerUnit, MinuteUnit])
s = t.createSentance([10, 1])
s2 = t.createSentance([20, 2])
s3 = s + s2
print(s3)







