from pwn import *
sh = remote('pwnable.kr', 9007)
sh.recv(10024)
for _ in range(100):
	tmp = sh.recv(1024).strip().split(' ')
	n = int(tmp[0].split('=')[1])
	c = int(tmp[1].split('=')[1])
	s = 0
	e = n
	for _ in range(c):
		sh.sendline(' '.join(str(e) for e in range(s, (e+s)/2)))
		a = sh.recv(1024, timeout=0.2).strip()
		i = int(a)
		if i == ((e+s)/2-s)*10:
        		s = (e+s)/2
    		else:
        		e = (e+s)/2
	sh.sendline(str(s))
	#print sh.recv(1024, timeout=0.2)
print sh.recv(1024, timeout=1)