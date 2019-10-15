from scipy.io import loadmat

f= loadmat('../INPUT/REAL/C_Easy1_noise01.mat')

print(f.keys())
print(f['data'][0][0])
print(f['spike_class'][0][0][0][0])
print(f['spike_times'][0][0][0][0])
#print(f['spike_times'])
