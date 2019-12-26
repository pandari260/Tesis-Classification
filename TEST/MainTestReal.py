from scipy.io import loadmat
import matplotlib.pyplot as plt  

f= loadmat('../../C_Easy1_noise01.mat')

print(f.keys())
print(f['data'][0][0])
print(f['spike_class'][0])
print(f['spike_times'][0][0][0][0])
print(f['data'][0])


plt.plot(f['data'][0])
plt.show()
#print(f['spike_times'])



