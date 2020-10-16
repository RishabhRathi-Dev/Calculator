
import math as m

# TO DO : -
# Add brackets
# Continuous loop untill asked for exit


# Done : - 
# Create error when no symbol is entered i.e. only number is given as an input
# Factorial
# Primitive Preventive method to stop exiting in default console
# Make it work in the ide (it works I was just executing wrong tab)


# OPENING AND INSTRUCTIONS
print('Multiple operations in one line can be performed\nBODMAS IS NOT FOLLOWED!!!!')
#print("Please don't use equal sign at end")
print('Following operations can be performed : -\nADD(+)\nSUB(-)\nDIVIDE(/)\nMULTIPLY(*)\nORDER(^)\nTRIGNOMETRIC FUNCTIONS(SINE(s), COSINE(c), TANGENT(t)) in Degrees\nFactorial (f, before)\nDecimals and Negative number support is available\n\n')

# CALCULATION PROCESS
def add(n1, n2):
	return n1+n2
	
def sub(n1, n2):
	return n1-n2
	
def mul(n1, n2):
	return n1*n2
	
def div(n1, n2):
	return n1/n2
	
def exponent(n1, n2):
	return n1**n2

def sin(n1):
	return m.sin(m.radians(n1))
	
def cos(n1):
	return m.cos(m.radians(n1))
	
def tan(n1):
	return m.tan(m.radians(n1))
	
def fac(n1):
	return m.factorial(n1)
	


line = str(input(''))     #FUNCTION
num = []                      #number on which operation is to be performed
sym = []                      #list on operations

# For reference
line_list = [k for k in line]

#print(line_list)

# Adding equal in line (if not present)
if line.count('=') == 0 :
	line = line+'='
	
negative_sign = 0 														#To count negative sign for activation it at right place
trigno_sign = 0   														#To count trignometric sign for activating it at right place

# PROCESS LOOP
while True :
	
	trigno_operation = False								            #To know the status of operation trignometric expression to adjust poping accordingly
	trig_ans = False													#To make sure single operation of trignometry gives result
	
	# Explanation :- 

	# a is empty string, used to constantly update and add operation to the list of operation 'sym' and add number on which number is to be operated in 'num'.
	
	# Mid is the intermiadiate answer and the final answer(after the last operation). 
	
	# mid is an interger f which is obtained as an intermediate, it is used to update num as the operations are done and give the final result.
	
	# Symbol k is inserted as an neutral sign, inserted in symbol list when two operation are performed in one turn.
	
	mid = 0
	
	a = ''	
	
	# FOR SEPARATION OF OPERATION FROM THE FUNCTION 
	for i in line:
		
		# FOR PLACING NEGATIVE SIGN AND RIGHT LOCATION
		if (i == '-' and line[0] == '-' and negative_sign == 0) or (i == '-' and line_list[line_list.index(i)-1].isdigit() == False) :
			a+=i
			negative_sign+=1
			
		else :
			
			# FOR MAKING NUMBER
			if i.isdigit() == True or i=='.' :
				a+=i
			
				# for debugging /////////
				#print('Numbers being made', a, file==sys.stderr)
			
			
			else:
				if len(a) > 0 :
					num.append(float(a))
				a = ''
				sym.append(i)
			
				#for debugging /////////
				#print('Symbols',i, file==sys.stderr)
	
			
	#for debugging ///////////
	#print('Num list' ,num, file==sys.stderr)
	#print('Sym list',sym, file==sys.stderr)
	#print(len(sym))
	#print(len(num))
	
	
	# ERROR MESSAGE WHEN NO SYMBOL ENTERED
	if len(sym) == 1 or sym[0] == '=' :
		print('ERROR : No operation entered')
		break
	
	
	# IDENTIFICATION OF OPERATION AND SENDING INSTRUCTION FOR CALCULATION TO CALCULATION PROCESS
	for j in range(len(sym)-1):
		
		
		#for debugging ////////////
		#print('\nCalulation loop\nStart\n')
		#print(sym[j], 'Calculation for symbol\n')
		#print('Num list' ,num, file==sys.stderr)
		#print('Sym list',sym, file==sys.stderr)
		
		
		
		n1 = num[0]
		
		
		
		#mid is n1 below so that single operation in trignometry can be handled
		
		if line[0] == 's' and trigno_sign == 0:
			n1 = sin(n1)
			mid = n1
			trigno_sign+=1
			trigno_operation = True
			
			# for debugging ///////////
			#print(n1, 'Sin activated', file == sys.stderr)
		
		if line[0] == 'c' and trigno_sign == 0:
			n1 = cos(n1)
			mid = n1
			trigno_sign+=1
			trigno_operation = True
			
			# for debugging ///////////
			#print(n1, 'Cos activated', file == sys.stderr)
		
		if line[0] == 't' and trigno_sign == 0:
			n1 = tan(n1)
			mid = n1
			trigno_sign+=1
			trigno_operation = True
			
		if line[0] == 'f' and trigno_sign == 0:
			n1 = fac(n1)
			mid = n1
			trigno_sign+=1
			trigno_operation = True
			
			# for debugging ///////////
			#print(n1,'Tangent activated', file == sys.stderr)
		
		
		# for debugging  //////////
		#print('mid146', mid, file==sys.stderr) 
		
		
		# K is the neutral symbol, it is inserted when two operation are performed in one go.
	
		if sym[j] == '+' : 
			
			trigno_operation = False
			
			if sym[j+1] == 's' :
				n2 = num[num.index(n1)+1]
				mid = add(n1, sin(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ////////////
				#print(n1, sin(n2), 'Sum with sine activated', file==sys.stderr)
				
			elif sym[j+1] == 'c' :
				n2 = num[num.index(n1)+1]
				mid = add(n1, cos(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, cos(n2), 'Sum with cosine activated', file==sys.stderr)
				
			elif sym[j+1] == 't' :
				n2 = num[num.index(n1)+1]
				mid = add(n1, tan(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, tan(n2), 'Sum with tangent activated', file==sys.stderr)
				
			elif sym[j+1] == 'f' :
				n2 = num[num.index(n1)+1]
				mid = add(n1, fac(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
				
				# for debugging /////////
				#print(n1, fac(n2), 'Sum with factorial activated')
				
				
			else :
				n2 = num[num.index(n1)+1]
				mid = add(n1, n2)
				
				#for debugging //////////
				#print(n1, n2, 'Sum activated', file==sys.stderr)
		
		
		if sym[j] == '-':
			
			trigno_operation = False
			
			if sym[j+1] == 's' :
				n2 = num[num.index(n1)+1]
				mid = sub(n1, sin(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ///////////
				#print(n1, sin(n2), 'Subtraction with sine activated', file==sys.stderr)
				
			elif sym[j+1] == 'c' :
				n2 = num[num.index(n1)+1]
				mid = sub(n1, cos(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ///////////
				#print(n1, cos(n2), 'Subtraction with cosine activated', file==sys.stderr)
				
			elif sym[j+1] == 't' :
				n2 = num[num.index(n1)+1]
				mid = sub(n1, tan(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ///////////
				#print(n1, tan(n2), 'Subtraction with tangent activated', file==sys.stderr)
				
			elif sym[j+1] == 'f' :
				n2 = num[num.index(n1)+1]
				mid = sub(n1, fac(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
				
				# for debugging /////////
				#print(n1, fac(n2), 'Subtraction with factorial activated')
				
			
			else:
				n2 = num[num.index(n1)+1]
				mid = sub(n1, n2)
			
				# for debuggging //////////
				#print(n1, n2, 'Subtraction activated', file==sys.stderr)
			
		if sym[j] == '*':
			
			trigno_operation = False
			
			if sym[j+1] == 's' :
				n2 = num[num.index(n1)+1]
				mid = mul(n1, sin(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ///////////
				#print(n1, sin(n2), 'Multiply with sine activated', file==sys.stderr)
				
			elif sym[j+1] == 'c' :
				n2 = num[num.index(n1)+1]
				mid = mul(n1, cos(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ////////////
				#print(n1, cos(n2), 'Multiply with cosine activated', file==sys.stderr)
				
			elif sym[j+1] == 't' :
				n2 = num[num.index(n1)+1]
				mid = mul(n1, tan(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging ///////////
				#print(n1, tan(n2), 'Multiply with tangent activated', file==sys.stderr)
				
			elif sym[j+1] == 'f' :
				n2 = num[num.index(n1)+1]
				mid = mul(n1, fac(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
				
				# for debugging /////////
				#print(n1, fac(n2), 'Multiply with factorial activated')
				
			
			else:
				n2 = num[num.index(n1)+1]
				mid = mul(n1, n2)
			
				# for debuggging ///////////
				#print(n1, n2, 'Multiply activated', file==sys.stderr)
			
			
		if sym[j] == '/':
			
			trigno_operation = False
			
			if sym[j+1] == 's' :
				n2 = num[num.index(n1)+1]
				mid = div(n1, sin(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, sin(n2), 'Division with sine activated', file==sys.stderr)
				
			elif sym[j+1] == 'c' :
				n2 = num[num.index(n1)+1]
				mid = div(n1, cos(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, cos(n2), 'Division with cosine activated', file==sys.stderr)
				
			elif sym[j+1] == 't' :
				n2 = num[num.index(n1)+1]
				mid = div(n1, tan(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging  //////////
				#print(n1, tan(n2), 'Division with tangent activated', file==sys.stderr)
				
			elif sym[j+1] == 'f' :
				n2 = num[num.index(n1)+1]
				mid = div(n1, fac(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
				
				# for debugging /////////
				#print(n1, fac(n2), 'Division with factorial activated')
				
			
			else:
				n2 = num[num.index(n1)+1]
				mid = div(n1, n2)
			
				# for debuggging //////////
				#print(n1, n2, 'Division activated', file==sys.stderr)
			
		if sym[j] == '^':
			
			trigno_operation = False
			
			if sym[j+1] == 's' :
				n2 = num[num.index(n1)+1]
				mid = exponent(n1, sin(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, sin(n2), 'Order with sine activated', file==sys.stderr)
				
			elif sym[j+1] == 'c' :
				n2 = num[num.index(n1)+1]
				mid = exponent(n1, cos(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, cos(n2), 'Order with cosine activated', file==sys.stderr)
				
			elif sym[j+1] == 't' :
				n2 = num[num.index(n1)+1]
				mid = exponent(n1, tan(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
			
			
				# for debuggging //////////
				#print(n1, tan(n2), 'Order with tangent activated', file==sys.stderr)
				
			elif sym[j+1] == 'f' :
				n2 = num[num.index(n1)+1]
				mid = exponent(n1, fac(n2))
				sym.pop(j+1)
				sym.insert(len(sym)-1, 'k')
				
				# for debugging /////////
				#print(n1, fac(n2), 'Order with factorial activated')
				
			
			else:
				n2 = num[num.index(n1)+1]
				mid = n1**n2
			
				# for debuggging //////////
				#print(n1, n2, 'Exponent activated', file==sys.stderr)
		
		
			
		# for debugging //////////
		#print('mid', mid, file == sys.stderr)
		#print(num, file == sys.stderr)
		#print(sym, file == sys.stderr)
		#print(trigno_operation, file == sys.stderr)
		
		
			
		
		# UPDATION IN NUM FOR INTERMIDIATE RESULTS (A+B+C+D THEN INTERMIDIATE WILL BE A+B (LET IT BE X) THEN x+C AND SO ON)	
		if len(num)>=2 and trigno_operation == False:
			num.pop(0)
			num.pop(0)
			num.insert(0, mid)
			trig_ans = False
			
			# for debugging /////////
			#print('Pop activated twice', file == sys.stderr)
		
		elif len(num)>=1 and trigno_operation == True :
			num.pop(0)
			num.insert(0, mid)
			trig_ans = True
			
			# for debugging ////////
			#print('Pop activated once', file == sys.stderr)
			
		else :
			break
			
			
	
	# for debugging /////////
	#print(num, sym, file==sys.stderr)
	#print(trig_ans)
	
	# ANSWER (OUTPUT)
	if len(num) <= 2 and trig_ans == False and len(sym)>0:   #General answer
		print('ANSWER :- '+str(mid))
		break
	elif len(num)<=2 and trig_ans == True and len(sym)>0 :  #For single operation on trigno
		print('ANSWER :- '+str(mid))
		break
	
	
	
	# For debugging	////////
	#print('END OF LOOP')		#Mark the end of loop
	#break
		


# Just to stop console from closing, in case it does like in that of diredct python console
#input()