    ¢z¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢{
    ¢x                 ¡E MobaXterm Personal Edition v23.4 ¡E                 ¢x
    ¢x               (SSH client, X server and network tools)               ¢x
    ¢x                                                                      ¢x
    ¢x ? SSH session to E94124094@192.168.137.109                           ¢x
    ¢x   ¡E Direct SSH      :  ?                                             ¢x
    ¢x   ¡E SSH compression :  ?                                             ¢x
    ¢x   ¡E SSH-browser     :  ?                                             ¢x
    ¢x   ¡E X11-forwarding  :  ?  (remote display is forwarded through SSH)  ¢x
    ¢x                                                                      ¢x
    ¢x ? For more info, ctrl+click on help or visit our website.            ¢x
    ¢|¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢w¢}

Linux raspberrypi 6.1.0-rpi4-rpi-v8 #1 SMP PREEMPT Debian 1:6.1.54-1+rpt2 (2023-10-05) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Dec  4 11:22:15 2023 from 192.168.137.1
E94124094@raspberrypi:~ $ pwd
/home/E94124094
E94124094@raspberrypi:~ $ cd python_work/
E94124094@raspberrypi:~/python_work $ python lab09.py
Traceback (most recent call last):
  File "/home/E94124094/python_work/lab09.py", line 7, in <module>
    s.bind((HOST, PORT)) #?socket?????
    ^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 99] Cannot assign requested address
E94124094@raspberrypi:~/python_work $ python lab09.py
Waiting for connection...
Add connection from ('192.168.137.1', 64100)
Receive from ('192.168.137.1', 64100) : 1
send to ('192.168.137.1', 64100) : 1
Receive from ('192.168.137.1', 64100) : 2
send to ('192.168.137.1', 64100) : 1
Receive from ('192.168.137.1', 64100) : 3
send to ('192.168.137.1', 64100) : 2
Receive from ('192.168.137.1', 64100) : 5
send to ('192.168.137.1', 64100) : 5
Receive from ('192.168.137.1', 64100) : 6
send to ('192.168.137.1', 64100) : 8
^CTraceback (most recent call last):
  File "/home/E94124094/python_work/lab09.py", line 25, in <module>
    indata = c.recv(1024).decode() #????????????
             ^^^^^^^^^^^^
KeyboardInterrupt

E94124094@raspberrypi:~/python_work $ python lab09.py
Traceback (most recent call last):
  File "/home/E94124094/python_work/lab09.py", line 7, in <module>
    s.bind((HOST, PORT)) #?socket?????
    ^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 98] Address already in use
E94124094@raspberrypi:~/python_work $ python lab09.py
Traceback (most recent call last):
  File "/home/E94124094/python_work/lab09.py", line 7, in <module>
    s.bind((HOST, PORT)) #?socket?????
    ^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 98] Address already in use
E94124094@raspberrypi:~/python_work $ python lab09.py
Waiting for connection...
Add connection from ('192.168.137.1', 64202)
Receive from ('192.168.137.1', 64202) : 6
send to ('192.168.137.1', 64202) : 8
Receive from ('192.168.137.1', 64202) : exit
connection closed
Waiting for connection...
Add connection from ('192.168.137.1', 64445)
