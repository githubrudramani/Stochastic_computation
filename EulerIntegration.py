###### Euler Method for PDE integration
dt, tmin, tmax = 0.001,0.0,10.0
step = int((tmax-tmin)/dt)
t = np.linspace(tmin,tmax,step)
y = np.zeros(step)
ya = np.exp(-t)
plt.plot(t,ya,label='Exact', lw=5)
y[0] = 1.0
for i in range(step-1):
    y[i+1] = y[i]-dt*y[i]
plt.plot(t,y,ls='--', lw =3, label ='Numerical')
plt.plot(t,y/ya, lw=3, label = 'Ratio')
plt.legend()
plt.show()


####### Damped harmonic ossilator by Euler approximation
'''
R(i+1) = R(i) + V[i]*Dt    #### Dt time step, R[i] position at time t[i]
V[i+1] = (1-(z/m) * Dt)V[i - (k/m) * R[i]* Dt #### z dampped constant, k spring constant
'''
dt, tmin, tmax = 0.01, 0,100
step = int((tmax-tmin)/dt)
t = np.linspace(tmin,tmax,step)
R = np.zeros(step)
R[0] = 1
V = np.zeros(step)
V[0] = 1
z, m, k = 0.1,2, 3
for i in range(step-1):
    R[i+1] = R[i] + V[i]*dt
    V[i+1] = (1-(z/m)*dt)* V[i] - (k/m) * R[i]*dt

Et = 0.5*m* V*V + 0.5*k*R*R


plt.plot(t,R, lw = 3, label ="Position")
plt.plot(t,V, lw = 3, ls = '--', label = "Velocity")
plt.plot(t,Et, lw = 3, ls = '--', label = "Energy")
plt.legend()
plt.plot()
