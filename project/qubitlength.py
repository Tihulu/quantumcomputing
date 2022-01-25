text=input('N = p*q, type N or bitlength of rsa:\n 1 for N, 2 for bitl. (format: 1, N):')
txt=text.split(',')
select , val = txt
if select==1:
	n=math.ceil(math.log2(val))
	bitn=2*n+3
	print (bitn,' qubits are needed')
if select==2:
	bitn=2*val+3
	print (bitn,' qubits are needed')
