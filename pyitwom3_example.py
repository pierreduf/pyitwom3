import pyitwom3 as itwom

print ("Using ITWOM Version: {}".format(itwom.ITWOMVersion()))


# copy elevation data from python list into native array
points = [165.0,166.0, 163.0, 163.0, 158.0, 155.0, 155.0, 154.0, 155.0]
delta_dist = 70.0

x=[len(points)-1, delta_dist]

for point in points:
	x.append(point)

# allocate native array
elev = itwom.doubleArray(len(x))
for i in range(len(x)):
	elev[i] = x[i]

# create native pointers for outputs
errnum = itwom.intp()
loss = itwom.doublep()

tht = 7.62
rht = 6.09
eps_dielect = 15
sgm_conductivity = 0.005
eno_ns_surfref = 301
freq = 900
climate = 5
pol = 0
conf = 0.5
rel = 0.5


mode = itwom.point_to_point(elev, tht, rht, eps_dielect, sgm_conductivity, eno_ns_surfref, freq, climate, pol, conf, rel, loss, errnum)

# access native pointer values.
print("dbloss: {:8.2f}, mode: {}, errno: {}".format(itwom.doublep.value(loss), mode, itwom.intp.value(errnum)))

# check result.
#assert (abs(itwom.doublep.value(loss) - 90.44) < 0.01)
