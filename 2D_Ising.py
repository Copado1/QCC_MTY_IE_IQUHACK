#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[98]:


from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from math import sin, cos, pi

# Parameters for the Hamiltonian
L = 4  # Number of qubits, for example
J = 1.0  # Coupling constant
h = 2.0  # Magnetic field strength
alpha = pi / 4  # Angle parameter

# Create a quantum circuit with L qubits
qc = QuantumCircuit(L)

# Define the time evolution parameters
t = Parameter('t')  # Time parameter for simulation

# Apply the ZZ terms in the Hamiltonian
for i in range(L - 1):
    qc.rzz(2 * J * t, i, i + 1)

# Apply the Z and X terms in the Hamiltonian
for i in range(L):
    qc.rz(2 * h * sin(alpha) * t, i)
    qc.rx(2 * h * cos(alpha) * t, i)

# Display the circuit
qc.draw('mpl')


# In[101]:


from qiskit import QuantumCircuit
from qiskit.circuit.library import RZZGate, RZGate, RXGate
from math import sin, cos

def trotter_step(circuit, L, J, h, alpha, t, n):
    # Perform the Trotter step for each term in the Hamiltonian using second-order Suzuki-Trotter.
    
    # First half of the ZZ interactions
    for i in range(L - 1):
        theta_ZZ = J * t / (2 * n)  # The factor of 1/2 for the second order
        circuit.rzz(theta_ZZ, i, i + 1)
    
    # Single-qubit Z and X rotations
    for i in range(L):
        theta_Z = h * sin(alpha) * t / n
        theta_X = h * cos(alpha) * t / n
        circuit.rz(theta_Z, i)
        circuit.rx(theta_X, i)
    
    # Second half of the ZZ interactions
    for i in range(L - 1):
        theta_ZZ = J * t / (2 * n)  # The factor of 1/2 for the second order
        circuit.rzz(theta_ZZ, i, i + 1)
    
    # No additional single-qubit Z and X rotations here

    return circuit

# Example usage
L = 4  # Number of qubits
J = -0.1  # Coupling constant for ZZ
h = 1.0  # External magnetic field strength (assumed from the circuit image)
alpha = -0.23  # Angle parameter for Z rotation (assumed from the circuit image)
t = 1.0  # Time evolution parameter
n = 1  # Number of Trotter steps (for demonstration)

# Create a new quantum circuit
qc = QuantumCircuit(L)

# Add the Trotter step to the circuit
qc = trotter_step(qc, L, J, h, alpha, t, n)

# Draw the circuit
qc.draw('mpl')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




