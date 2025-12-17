# Aula 03
📓 [Documentação Legacy Remote API Python](https://manual.coppeliarobotics.com/en/remoteApiFunctionsPython.htm)

É recomendado colocar `simRemoteApi.start(19999)` no início do script das cenas.

## Referenciar objetos na simulação
```python
simxGetObjectHandle(clientID, objectName, operationMode)
```

📝 [Operation Modes](https://manual.coppeliarobotics.com/en/remoteApiConstants.htm#operationModes)

## Acessar informações dos objetos na simulação
```python
simxGetObjectPosition   (clientID, objectHandle, relativeToObjectHandle, operationMode)
simxGetObjectOrientation(clientID, objectHandle, relativeToObjectHandle, operationMode)
simxGetObjectVelocity   (clientID, objectHandle, operationMode)
```

## Enviar comando de velocidade para objeto na simulação
```python
simxSetJointTargetVelocity(clientID, jointHandle, targetVelocity, operationMode)
```

