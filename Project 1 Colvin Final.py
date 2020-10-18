import numpy as np
ntrials=5000
mu = 0
sd = 1
listOfAvg = []
for N in range(1,201):
    sum=0
    for trial in range(1,ntrials):
        rdist= np.random.normal(mu, sd, size=N)
        rdist.sort()
        sum+=rdist[N-1]
    sum/=ntrials
    listOfAvg.append(sum)
    print(N,listOfAvg[N-1])


def ext_file(filename,stackedarray,):
    external_file = np.savetxt(filename, stackedarray)
    return external_file

ext_file("Project_one.txt", listOfAvg)
print(ext_file)

#Proceeded to gnuplot in terminal and plotted this .txt file using the command below:
# plot  'Project_one.txt' title 'x= N  y= max_ avg ' w l
