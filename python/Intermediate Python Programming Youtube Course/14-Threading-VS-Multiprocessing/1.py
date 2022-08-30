# Threading-VS-Multiprocessing: You can run code in parallel

# VS:

"""
Process: An instance of a program (e.g Python interpreter)
Process can have multiple thread inside

+ Takes advantage of multiple CPUs and cores
+ Seperate memory spapce -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is started independently form other processes
+ Processes are interruptable/killable
+ One GIL (Global Interpreter Lock) for each process -> avoids GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread
- More memory
- IPC (inter-process communication) is more complicated
"""

"""
Thread: An entity within a process  that that can be scheduled (also known as lightweight process)
A process can spawn multiple threads

+ All threads within a process share the same memory
+ Lightweight
+ Starting a thread is faster than starting a process
+ Great for IO-bound tasks

- Threading is limited by GIL: Only one thread at a time (There is no actual parallel computation in multi threading)
- No effect for CPU-bound tasks
- Not interuptable/killable
- Careful with race conditions (When two thread want to work/change the same memory/variable)
"""

"""
GIL: Global interpreter lock
- A lock that allows only one thread at a time to execute in Python

- Needed in CPython because memory management is not thread-safe

- Avoid:
  - Use multiprocessing
  - Use a different, free-threaded Python implementation (Jython, IronPython)
  - Use Python as a wrapper for third-party libraries (C, C++) -> numpy, scipy
"""
