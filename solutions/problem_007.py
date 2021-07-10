def get_message_count(code):
    digits = str(code)
	n=len(digits)
	count1=0
	count2=1

	for i in range(n):
		count=0
		# If the last digit is not 0, then last
		# digit must add to the number of words
		if digits[i]>'0':
			count=count2

		# If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
		if (digits[i - 1] == '1' or
			(digits[i - 1] == '2' and
				digits[i] < '7')):
			count+= count1
		
		count1=count2
		count2=count

		print("{}: {},{}".format(i,count1,count2))

	return count2;

assert get_message_count(81) == 1
assert get_message_count(11) == 2
assert get_message_count(111) == 3
assert get_message_count(1111) == 5
assert get_message_count(1311) == 4
