
import matplotlib.pyplot as plt





import math
import numpy as np


G = 6.6743 * 10**(-11)
mode = input("enter the mode(3d or 2d): ")
if mode != "2d" and mode != "3d":
	mode = "2d"

try:
	pause = int(input("enter updates per second"))
except ValueError:
	pause = False
try:
	dt = float(input("enter minimum time step in seconds"))
except ValueError:
	dt = 1/100
try:
	size = int(input("enter size of the graph"))
except ValueError:
	size = 1000
try:
	pt = int(input("enter polling interval"))
except ValueError:
	pt = 1

if pause == 0:
	pause = False



if mode == "2d":
	try:
		num_objects = int(input("enter the number of objects"))
	except ValueError:
		num_objects = 2

	if num_objects == 2:
		m1 = int(input("what is mass1?"))
		m2 = int(input("what is mass2?"))
		x1 = int(input("what is x1?"))
		y1 = int(input("what is y1?"))
		x2 = int(input("what is x2?"))
		y2 = int(input("what is y2?"))
		v1 = (float(input("what is speed1?")), float(input("what is the direction of speed1?")))
		v2 = (float(input("what is speed2?")), float(input("what is the direction of speed2?")))
		print("waiting...")
		xs1 = [x1,x1+ v1[0]*dt]
		ys1 = [y1,y1+ v1[1]*dt]
		xs2 = [x2,x2+ v2[0]*dt]
		ys2 = [y2,y2+ v2[1]*dt]
		rs = [math.sqrt(abs((x1 - x2) ** 2 + (y1 - y2) ** 2))]
		plus = 0
		plus2 = 0
		f = G * (m1*m2)/(rs[0]**2)
		vel1 = (f/m1)
		vel2 = (f/m2)
		vel1v1 = (vel1*(x2-x1))/rs[0]
		vel1v2 = (vel1*(y2-y1))/rs[0]
		vel2v1 = (vel2*(x1-x2))/rs[0]
		vel2v2 = (vel2*(y1-y2))/rs[0]

		v1xl = [v1[0],v1[0]+vel1v1*dt]
		v1yl = [v1[1],v1[1]+vel1v2*dt]
		v2xl = [v2[0],v2[0]+vel2v1*dt]
		v2yl = [v2[1],v2[1]+vel2v2*dt]

		for i in range(1000000):
			plus += 1

			rs.append(math.sqrt(abs((xs1[plus] - xs2[plus]) ** 2 + (ys1[plus] - ys2[plus]) ** 2)))

			f = G*m1*m2/(rs[plus]**2)
			vel1 = (f/m1)
			vel2 = (f/m2)
			vel1v1 = (vel1*(xs2[plus]-xs1[plus]))/rs[plus]
			vel1v2 = (vel1*(ys2[plus]-ys1[plus]))/rs[plus]
			vel2v1 = (vel2*(xs1[plus]-xs2[plus]))/rs[plus]
			vel2v2 = (vel2*(ys1[plus]-ys2[plus]))/rs[plus]

			v1xl.append(v1xl[plus] + vel1v1 * dt)
			v1yl.append(v1yl[plus] + vel1v2 * dt)
			v2xl.append(v2xl[plus] + vel2v1 * dt)
			v2yl.append(v2yl[plus] + vel2v2 * dt)

			xs1.append(xs1[0 + plus] + v1xl[plus]*dt)
			ys1.append(ys1[0 + plus] + v1yl[plus]*dt)
			xs2.append(xs2[0 + plus] + v2xl[plus]*dt)
			ys2.append(ys2[0 + plus] + v2yl[plus]*dt)




		plt.ion()
		fig, ax = plt.subplots(figsize=(12,12))
		object1 = plt.Circle((x1, y1), size/100, color='red', ec='black')
		object2 = plt.Circle((x2, y2), size/100, color='blue', ec='black')
		ax.plot(xs1, ys1,  color='red', alpha=0.3, linestyle="--")
		ax.plot(xs2, ys2, color='blue', alpha=0.3, linestyle="--")
		line1, = ax.plot([], [],  color='red', linestyle='-')
		line2, = ax.plot([], [],  color='blue', linestyle='-')

		ax.add_patch(object1)
		ax.add_patch(object2)

		ax.set_aspect('equal')
		plt.xlim(0, size)
		plt.ylim(0, size)
		plt.grid(True)
		dx1 = []
		dy1 = []
		dx2 = []
		dy2 = []




		while True:
			while plus2 < len(xs1) and plt.fignum_exists(fig.number):
				object1.set_center((xs1[plus2], ys1[plus2]))
				object2.set_center((xs2[plus2],ys2[plus2]))
				ax.plot(xs1[plus2], ys1[plus2], color='red')
				ax.plot(xs2[plus2], ys2[plus2], color="blue")
				dx1.append(xs1[plus2])
				dy1.append(ys1[plus2])
				dx2.append(xs2[plus2])
				dy2.append(ys2[plus2])
				line1.set_data(dx1, dy1)


				line2.set_data(dx2, dy2)




				fig.canvas.draw_idle()
				fig.canvas.flush_events()

				if pause != False:
					plt.pause(1 / pause)

				plus2 += pt
	else:



		positionsx = [[] for _ in range(num_objects)]
		positionsy = [[] for _ in range(num_objects)]


		masses = np.zeros(num_objects)
		spositionsx = np.zeros(num_objects)
		spositionsy = np.zeros(num_objects)

		rss = [[[] for _ in range(num_objects)] for _ in range(num_objects)]
		fs = np.zeros((num_objects, num_objects, 3))
		vels = np.zeros((num_objects, num_objects))
		velv1s = np.zeros(num_objects)
		velv2s = np.zeros(num_objects)


		vxls = [[] for _ in range(num_objects)]
		vyls = [[] for _ in range(num_objects)]

		speeds = [[] for _ in range(num_objects)]
		rssx = [[[] for _ in range(num_objects)] for _ in range(num_objects)]
		rssy = [[[] for _ in range(num_objects)] for _ in range(num_objects)]

		for i in range(num_objects):
			masses[i] = int(input(f"what is mass{i + 1}"))
			spositionsx[i] = int(input(f"what is x{i + 1}"))
			spositionsy[i] = int(input(f"what is y{i + 1}"))

			speeds[i] = [float(input(f"what is speed{i + 1}")), float(input(f"what is the direction of speed{i + 1}?")),
						]
		print("waiting...")

		for i in range(num_objects):
			positionsx[i] = [spositionsx[i], spositionsx[i] + speeds[i][0] * dt]
			positionsy[i] = [spositionsy[i], spositionsy[i] + speeds[i][1] * dt]

		for i in range(num_objects):
			velv1st = 0
			velv2st = 0

			for a in range(num_objects):
				if i == a:
					continue
				if i == num_objects and a == i:
					break
				rss[i][a] = [math.sqrt(
					abs((spositionsx[a] - spositionsx[i]) ** 2 + (spositionsy[a] - spositionsy[i]) ** 2))
								]
				rssx[i][a] = spositionsx[a] - spositionsx[i]
				rssy[i][a] = spositionsy[a] - spositionsy[i]


			for a in range(num_objects):
				if i == a:
					continue
				if i == num_objects and a == i:
					break

				for j in range(2):
					f_total = G * (masses[i] * masses[a]) / (rss[i][a][0] ** 2)
					if j == 0:
						fsx = ((f_total * rssx[i][a]) / rss[i][a][0])
						fs[i, a, j] += fsx
						velv1s[i] = fs[i][a][j] / masses[i]
						fs[i, a, j] = 0
						velv1st += velv1s[i]
					if j == 1:
						fsy = ((f_total * rssy[i][a]) / rss[i][a][0])
						fs[i, a, j] += fsy
						velv2s[i] = fs[i][a][j] / masses[i]
						fs[i, a, j] = 0
						velv2st += velv2s[i]


					vxls[i] = [speeds[i][0], speeds[i][0] + velv1st * 1 / 100]
					vyls[i] = [speeds[i][1], speeds[i][1] + velv2st * 1 / 100]

		plus = 0
		plus2 = 0
		for o in range(1000000):
			plus += 1
			for i in range(num_objects):
				velv1st = 0
				velv2st = 0


				for a in range(num_objects):
					if i == a:
						continue
					if i == num_objects and a == i:
						break
					rss[i][a].append(math.sqrt(abs((positionsx[a][plus] - positionsx[i][plus]) ** 2 + (
								positionsy[a][plus] - positionsy[i][plus]) ** 2 )))

					rssx[i][a] = positionsx[a][plus] - positionsx[i][plus]
					rssy[i][a] = positionsy[a][plus] - positionsy[i][plus]


				for a in range(num_objects):

					fsx = 0
					fsy = 0

					if i == a:
						continue
					if i == num_objects and a == i:
						break

					for j in range(2):

						f_total = G * (masses[i] * masses[a]) / (rss[i][a][plus] ** 2)
						if j == 0:
							fsx = ((f_total * rssx[i][a]) / rss[i][a][plus])
							fs[i, a, j] += fsx
							velv1s[i] = fs[i][a][j] / masses[i]
							fs[i, a, j] = 0
							velv1st += velv1s[i]

						if j == 1:
							fsy = ((f_total * rssy[i][a]) / rss[i][a][plus])
							fs[i, a, j] += fsy
							velv2s[i] = fs[i][a][j] / masses[i]
							fs[i, a, j] = 0
							velv2st += velv2s[i]



				vxls[i].append(vxls[i][plus] + velv1st * dt)
				vyls[i].append(vyls[i][plus] + velv2st * dt)


				positionsx[i].append(positionsx[i][plus] + vxls[i][plus] * dt)
				positionsy[i].append(positionsy[i][plus] + vyls[i][plus] * dt)

		plt.ion()
		fig = plt.figure(figsize=(12, 12))
		ax = fig.add_subplot(111)
		plt.grid(True)
		ax.set_xlim(0, size)
		ax.set_ylim(0, size)

		colors = [
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0'

		]
	objects = []
	dx = [[] for _ in range(num_objects)]
	dy = [[] for _ in range(num_objects)]
	line = []

	for i in range(num_objects):

		circle = plt.Circle((spositionsx[i], spositionsy[i]), size/100, color=colors[i], ec='black')
		objects.append(circle)
		ax.add_patch(circle)

		ax.plot(positionsx[i], positionsy[i], color=colors[i], alpha=0.3, linestyle="--")


		line_object, = ax.plot([], [], color=colors[i], linestyle='-')
		line.append(line_object)

	while True:
		while plus2 < len(positionsx[0]) and plt.fignum_exists(fig.number):
			for i in range(num_objects):
				objects[i].set_center((positionsx[i][plus2], positionsy[i][plus2]))

				dx[i].append(positionsx[i][plus2])
				dy[i].append(positionsy[i][plus2])


				line[i].set_data(dx[i], dy[i])

			fig.canvas.draw_idle()
			fig.canvas.flush_events()

			if pause != False:
				plt.pause(1 / pause)

			plus2 += pt


if mode == "3d":
	try:
		num_objects = int(input("what is number of objects?"))
	except ValueError:
		num_objects = 2
	if num_objects == 2:



		m1 = int(input("what is mass1?"))
		m2 = int(input("what is mass2?"))
		x1 = int(input("what is x1?"))
		y1 = int(input("what is y1?"))
		z1 = int(input("what is z1?"))
		x2 = int(input("what is x2?"))
		y2 = int(input("what is y2?"))
		z2 = int(input("what is z2?"))
		v1 = (float(input("what is speed1?")), float(input("what is the direction of speed1?")), float(input("what is the tilt of speed1?")))
		v2 = (float(input("what is speed2?")), float(input("what is the direction of speed2?")),float(input("what is the tilt of speed2?")))
		print("waiting...")
		xs1 = [x1, x1 + v1[0] * dt]
		ys1 = [y1, y1 + v1[1] * dt]
		zs1 = [z1, z1 + v1[2] * dt]
		xs2 = [x2, x2 + v2[0] * dt]
		ys2 = [y2, y2 + v2[1] * dt]
		zs2 = [z2, z2 + v2[2] * dt]
		rs = [math.sqrt(abs((x1 - x2) ** 2 + (y1 - y2) ** 2)+((z1 - z2) ** 2))]
		plus = 0
		plus2 = 0
		f = G * (m1 * m2) / (rs[0] ** 2)
		vel1 = (f / m1)
		vel2 = (f / m2)
		vel1v1 = (vel1 * (x2 - x1)) / rs[0]
		vel1v2 = (vel1 * (y2 - y1)) / rs[0]
		vel1v3 = (vel1 * (z2 - z1)) / rs[0]
		vel2v1 = (vel2 * (x1 - x2)) / rs[0]
		vel2v2 = (vel2 * (y1 - y2)) / rs[0]
		vel2v3 = (vel2 * (z1 - z2)) / rs[0]
		v1xl = [v1[0], v1[0] + vel1v1 * dt]
		v1yl = [v1[1], v1[1] + vel1v2 * dt]
		v1zl = [v1[2], v1[2] + vel1v3 * dt]
		v2xl = [v2[0], v2[0] + vel2v1 * dt]
		v2yl = [v2[1], v2[1] + vel2v2 * dt]
		v2zl = [v2[2], v2[2] + vel2v3 * dt]
		d = 1000

		for i in range(1000000):
			plus += 1

			rs.append(math.sqrt(abs((xs1[plus] - xs2[plus]) ** 2 + (ys1[plus] - ys2[plus]) ** 2+((zs1[plus] - zs2[plus]) ** 2))))



			f = G * m1 * m2 / (rs[plus] ** 2)
			vel1 = (f / m1)
			vel2 = (f / m2)
			vel1v1 = (vel1 * (xs2[plus] - xs1[plus])) / rs[plus]
			vel1v2 = (vel1 * (ys2[plus] - ys1[plus])) / rs[plus]
			vel1v3 = (vel1 * (zs2[plus] - zs1[plus])) / rs[plus]
			vel2v1 = (vel2 * (xs1[plus] - xs2[plus])) / rs[plus]
			vel2v2 = (vel2 * (ys1[plus] - ys2[plus])) / rs[plus]
			vel2v3 = (vel2 * (zs1[plus] - zs2[plus])) / rs[plus]

			v1xl.append(v1xl[plus] + vel1v1 * dt)
			v1yl.append(v1yl[plus] + vel1v2 * dt)
			v1zl.append(v1zl[plus] + vel1v3 * dt)
			v2xl.append(v2xl[plus] + vel2v1 * dt)
			v2yl.append(v2yl[plus] + vel2v2 * dt)
			v2zl.append(v2zl[plus] + vel2v3 * dt)

			xs1.append(xs1[0 + plus] + v1xl[plus] * dt)
			ys1.append(ys1[0 + plus] + v1yl[plus] * dt)
			zs1.append(zs1[0 + plus] + v1zl[plus] * dt)
			xs2.append(xs2[0 + plus] + v2xl[plus] * dt)
			ys2.append(ys2[0 + plus] + v2yl[plus] * dt)
			zs2.append(zs2[0 + plus] + v2zl[plus] * dt)

		plt.ion()
		fig = plt.figure(figsize=(12, 12))
		ax = fig.add_subplot(111, projection='3d')

		object1 = ax.scatter(x1, y1, z1, c='red',s=d)
		object2 = ax.scatter(x2, y2, z2, c='blue',s=d)
		ax.plot(xs1, ys1, zs1, color='red', alpha=0.3, linestyle="--")
		ax.plot(xs2, ys2, zs2, color='blue', alpha=0.3, linestyle="--")
		ax.set_xlim(0, size)
		ax.set_ylim(0, size)
		ax.set_zlim(0, size)
		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Z')
		dx1 = []
		dy1 = []
		dz1 = []
		dx2 = []
		dy2 = []
		dz2 = []
		line1, = ax.plot([], [], [], color='red', linestyle='-')
		line2, = ax.plot([], [], [], color='blue', linestyle='-')



		while True:
			while plus2 < len(xs1) and plt.fignum_exists(fig.number):
				object1.set_offsets(np.c_[[xs1[plus2]], [ys1[plus2]]])
				object1.set_3d_properties([zs1[plus2]], 'z')

				object2.set_offsets(np.c_[[xs2[plus2]], [ys2[plus2]]])
				object2.set_3d_properties([zs2[plus2]], 'z')

				dx1.append(xs1[plus2])
				dy1.append(ys1[plus2])
				dz1.append(zs1[plus2])
				dx2.append(xs2[plus2])
				dy2.append(ys2[plus2])
				dz2.append(zs2[plus2])

				line1.set_data(dx1, dy1)
				line1.set_3d_properties(dz1)

				line2.set_data(dx2, dy2)
				line2.set_3d_properties(dz2)




				fig.canvas.draw_idle()
				fig.canvas.flush_events()

				if pause != False:
					plt.pause(1 / pause)


				plus2 += pt
	else:


		positionsx = [[] for _ in range(num_objects)]
		positionsy = [[] for _ in range(num_objects)]
		positionsz = [[] for _ in range(num_objects)]

		masses = np.zeros(num_objects)
		spositionsx = np.zeros(num_objects)
		spositionsy = np.zeros(num_objects)
		spositionsz = np.zeros(num_objects)

		rss = [[[] for _ in range(num_objects)] for _ in range(num_objects)]
		fs = np.zeros((num_objects, num_objects, 3))
		vels = np.zeros((num_objects, num_objects))
		velv1s = np.zeros(num_objects)
		velv2s = np.zeros(num_objects)
		velv3s = np.zeros(num_objects)

		vxls = [[] for _ in range(num_objects)]
		vyls = [[] for _ in range(num_objects)]
		vzls = [[] for _ in range(num_objects)]
		speeds = [[] for _ in range(num_objects)]
		rssx = [[[] for _ in range(num_objects)] for _ in range(num_objects)]
		rssy = [[[] for _ in range(num_objects)] for _ in range(num_objects)]
		rssz = [[[] for _ in range(num_objects)] for _ in range(num_objects)]
		for i in range(num_objects):
			masses[i] = int(input(f"what is mass{i+1}"))
			spositionsx[i] = int(input(f"what is x{i+1}"))
			spositionsy[i] = int(input(f"what is y{i+1}"))
			spositionsz[i] = int(input(f"what is z{i+1}"))
			speeds[i] = [float(input(f"what is speed{i+1}")), float(input(f"what is the direction of speed{i+1}?")), float(input(f"what is the tilt of speed{i+1}?"))]
		print("waiting...")

		for i in range(num_objects):
			positionsx[i] = [spositionsx[i], spositionsx[i] + speeds[i][0] * dt]
			positionsy[i] = [spositionsy[i], spositionsy[i] + speeds[i][1] * dt]
			positionsz[i] = [spositionsz[i], spositionsz[i] + speeds[i][2] * dt]
		for i in range(num_objects):
			velv1st = 0
			velv2st = 0
			velv3st = 0
			for a in range(num_objects):
				if i == a:
					continue
				if i == num_objects and a == i:
					break
				rss[i][a] = [math.sqrt(abs((spositionsx[a] - spositionsx[i]) ** 2 + (spositionsy[a] - spositionsy[i]) ** 2) + ((spositionsz[a] - spositionsz[i]) ** 2))]
				rssx[i][a] = spositionsx[a] - spositionsx[i]
				rssy[i][a] = spositionsy[a] - spositionsy[i]
				rssz[i][a] = spositionsz[a] - spositionsz[i]

			for a in range(num_objects):
				if i == a:
					continue
				if i == num_objects and a == i:
					break

				for j in range(3):
					f_total = G * (masses[i] * masses[a]) / (rss[i][a][0] ** 2)
					if j == 0:
						fsx = ((f_total*rssx[i][a])/rss[i][a][0])
						fs[i,a,j] += fsx
						velv1s[i] = fs[i][a][j]/masses[i]
						fs[i,a,j] = 0
						velv1st += velv1s[i]
					if j == 1:
						fsy = ((f_total * rssy[i][a]) / rss[i][a][0])
						fs[i,a,j] += fsy
						velv2s[i] = fs[i][a][j] / masses[i]
						fs[i, a, j] = 0
						velv2st += velv2s[i]
					if j == 2:
						fsz = ((f_total * rssz[i][a]) / rss[i][a][0])
						fs[i,a,j] += fsz
						velv3s[i] = fs[i][a][j] / masses[i]
						fs[i, a, j] = 0
						velv3st += velv3s[i]


					vxls[i] = [speeds[i][0], speeds[i][0] + velv1st * dt]
					vyls[i] = [speeds[i][1], speeds[i][1] + velv2st * dt]
					vzls[i] = [speeds[i][2], speeds[i][2] + velv3st * dt]
		plus = 0
		plus2 = 0
		for o in range(1000000):
			plus += 1
			for i in range(num_objects):
				velv1st = 0
				velv2st = 0
				velv3st = 0



				for a in range(num_objects):
					if i == a:
						continue
					if i == num_objects and a == i:
						break
					rss[i][a].append(math.sqrt(abs((positionsx[a][plus] - positionsx[i][plus]) ** 2 + (positionsy[a][plus] - positionsy[i][plus]) ** 2+((positionsz[a][plus] - positionsz[i][plus]) ** 2))))
					rssx[i][a] = positionsx[a][plus] - positionsx[i][plus]
					rssy[i][a] = positionsy[a][plus] - positionsy[i][plus]
					rssz[i][a] = positionsz[a][plus] - positionsz[i][plus]

				for a in range(num_objects):

					fsx = 0
					fsy = 0
					fsz = 0


					if i == a:
						continue
					if i == num_objects and a == i:
						break

					for j in range(3):

						f_total = G * (masses[i] * masses[a]) / (rss[i][a][plus] ** 2)
						if j == 0:
							fsx =  ((f_total * rssx[i][a]) / rss[i][a][plus])
							fs[i, a, j] += fsx
							velv1s[i] = fs[i][a][j] / masses[i]
							fs[i, a, j] = 0
							velv1st += velv1s[i]


						if j == 1:
							fsy = ((f_total * rssy[i][a]) / rss[i][a][plus])
							fs[i,a,j] += fsy
							velv2s[i] = fs[i][a][j] / masses[i]
							fs[i, a, j] = 0
							velv2st += velv2s[i]


						if j == 2:
							fsz = ((f_total * rssz[i][a]) / rss[i][a][plus])
							fs[i,a,j] += fsz
							velv3s[i] = fs[i][a][j] / masses[i]
							fs[i, a, j] = 0
							velv3st += velv3s[i]


				vxls[i].append(vxls[i][plus] + velv1st * dt)
				vyls[i].append(vyls[i][plus] + velv2st * dt)
				vzls[i].append(vzls[i][plus] + velv3st * dt)




				positionsx[i].append(positionsx[i][plus] + vxls[i][plus] * dt)
				positionsy[i].append(positionsy[i][plus] + vyls[i][plus] * dt)
				positionsz[i].append(positionsz[i][plus] + vzls[i][plus] * dt)
		plt.ion()
		fig = plt.figure(figsize=(12, 12))
		ax = fig.add_subplot(111, projection='3d')
		ax.set_xlim(0, size)
		ax.set_ylim(0, size)
		ax.set_zlim(0, size)
		colors = [
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0',
			'#139EEB', '#EB5813', '#13EB13', '#EB1313', '#9A3EF0'

]
		objects = [ ]
		dx =[[]for _ in range(num_objects)]
		dy = [[]for _ in range(num_objects)]
		dz = [[] for _ in range(num_objects)]
		line = []


		for i in range(num_objects):
			scat = ax.scatter(spositionsx[i], spositionsy[i], color=colors[i],s=1000)
			objects.append(scat)
			ax.plot(positionsx[i], positionsy[i], positionsz[i], color=colors[i], alpha=0.3, linestyle="--")
			line.append(ax.plot([], [], [], color=colors[i], linestyle='-')[0])
		while True:
			while plus2 < len(positionsx[0]) and plt.fignum_exists(fig.number):
				for i in range(num_objects):
					objects[i].set_offsets(np.c_[[positionsx[i][plus2]], [positionsy[i][plus2]]])
					objects[i].set_3d_properties([positionsz[i][plus2]], 'z')
					dx[i].append(positionsx[i][plus2])
					dy[i].append(positionsy[i][plus2])
					dz[i].append(positionsz[i][plus2])


					line[i].set_data(dx[i], dy[i])
					line[i].set_3d_properties(dz[i])









				fig.canvas.draw_idle()
				fig.canvas.flush_events()

				if pause != False:
					plt.pause(1 / pause)


				plus2 += pt












