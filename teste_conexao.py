'''
The Legacy Remote API is one of the several ways an application can connect with CoppeliaSim.
It is deprecated as per CoppeliaSim V4.4 in favor of the ZeroMQ Remote API.

The CoppeliaSim Legacy Remote API is composed by approximately one hundred specific functions and one generic function
that can be called from a C/C++ application, a Python script, a Java application or a MATLAB/Octave program.

The legacy remote API functions are interacting with CoppeliaSim via socket communication (or, optionally, via shared memory).
All this happens in a hidden fashion to the user.

https://manual.coppeliarobotics.com/en/legacyRemoteApiOverview.htm
'''

import sim   # Biblioteca simulação CoppeliaSim

print("[COM] Iniciando a thread de comunicação com o servidor CoppeliaSim.")
sim.simxFinish(-1)   # Fecha conexões antigas, se houver
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)   # https://manual.coppeliarobotics.com/en/remoteApiFunctionsPython.htm#simxStart
# string   connectionAddress                The ip address where the server is located (i.e. CoppeliaSim)
# number   connectionPort                   Port number. Specify a negative port number in order to use shared memory instead of socket communication
# bool     waitUntilConnected               If `True`: the function blocks until connected (or timed out)
# bool     doNotReconnectOnceDisconnected   If `True`: the communication thread will not attempt a second connection if a connection was lost
# number   timeOutInMs                      If positive: sets timeout for first connection attempt. If negative: sets timeout for blocking calls
# number   commThreadCycleInMs              Indicates how often data packets are sent back and forth. Reducing this number improves responsiveness, and a default value of 5 is recommended

print("[COM] clientID = ", clientID)

if clientID != -1:
    print("[COM] OK. Tentativa de conexão bem sucedida! :)")
    sim.simxFinish(clientID)   # Ends the communication thread. This should be the very last remote API function called on the client side
else:
    print("[COM] ERRO. Tentativa de conexão má sucedida. :(")
