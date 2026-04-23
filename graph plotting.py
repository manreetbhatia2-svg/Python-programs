import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
plt.clf()

#Accepting peak value
Amplitude = int(input("Enter the peak value of the wave "))

#Accepting frequency
Frequency = int(input("Enter the frequency of the wave "))

#Accepting phase angle
phase = int(input("Enter the phase angle of the wave in degrees "))
phase = np.deg2rad(phase)

#Plotting the sine wave
xsin = np.linspace(0,2*np.pi,1000)
ysin = Amplitude*np.sin(Frequency*xsin + phase)

#Plotting the cosine wave
xcos = np.linspace(0,2*np.pi,1000)
ycos = Amplitude*np.cos(Frequency*xcos + phase)

#Plotting the square wave
x = np.linspace(0,2*np.pi,1000)
y = Amplitude*scipy.signal.square(Frequency*x)

#Plotting the sawtooth wave
xsaw = np.linspace(0,2*Frequency*np.pi,1000)
ysaw = Amplitude*scipy.signal.sawtooth(Frequency*x)

#Plotting the triangular wave
xtri = np.linspace(0,2*Frequency*np.pi,1000)
ytri = Amplitude*scipy.signal.sawtooth(Frequency*x,width = 0.5)

#Creating plot
# sin wave
plt.subplot(2,3,1)
plt.plot(xsin,ysin)
plt.title("Simple sin wave")
plt.xlabel("Time(radians)")
plt.ylabel("Amplitude")
plt.grid(True)

# cos wave
plt.subplot(2,3,2)
plt.plot(xcos,ycos)
plt.title("Simple cos wave")
plt.xlabel("Time(radians)")
plt.ylabel("Amplitude")
plt.grid(True)


# square wave
plt.subplot(2,3,3)
plt.plot(x,y)
plt.title("Square wave")
plt.xlabel("Time(radians)")
plt.ylabel("Amplitude")
plt.grid(True)

# sawtooth wave
plt.subplot(2,3,4)
plt.plot(xsaw,ysaw)
plt.title("Sawtooth wave")
plt.xlabel("Time(radians)")
plt.ylabel("Amplitude")
plt.grid(True)

# triangular wave
plt.subplot(2,3,5)
plt.plot(xtri,ytri)
plt.title("Triangular wave")
plt.xlabel("Time(radians)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()