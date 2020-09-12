import sys

num_to_word_list = [
	['صفر','واحد','إثنان','ثلاثة','أربعة','خمسة','ستة','سبعة','ثمانية','تسعة'],
	['عشرة','عشرون','ثلاثون','أربعون','خمسون','ستون','سبعون','ثمانون','تسعون'],
	['مئة','مئتان','ثلاثة مئة','أربعة مئة','خمسة مئة','ستة مئة','سبعة مئة','ثمانية مئة','تسعة مئة'],
	['ألف','ألفان','ثلاثة آلاف','أربعة آلاف','خمسة آلاف','ستة آلاف','سبعة آلاف','ثمانية آلاف','تسعة آلاف']
	]
def ones(number, location=0):
	result = num_to_word_list[location][number]
	return result
def tens(number):
	if number < 10:
		result = ones(number)
	elif number % 10 == 0:
		result = ones((number // 10)-1, 1)
	elif number == 11:
		result = 'أحد عشر'
	elif number == 12:
		result = 'إثنا عشر'
	else:
		result = ones(number % 10)+' و '+ ones((number // 10)-1, 1)
	return result
def hundreds(number):
	if number < 100:
		result = tens(number)
	elif number % 100 == 0:
		result = ones((number // 100)-1, 2)
	else:
		result = ones((number // 100)-1, 2)+' و '+tens(number % 100)
	return result
def number_to_word(number):
	if number < 1000:
		result = hundreds(number)
	elif number % 100 == 0:
		result = ones((number // 1000)-1, 3)
	else:
		result = ones((number // 1000)-1, 3)+' و '+hundreds(number % 1000)
	# return result

	return result.encode('utf-8')

sys.stdout.buffer.write(number_to_word(1212))