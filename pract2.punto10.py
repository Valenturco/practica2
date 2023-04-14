nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica',
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge'
'JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo',
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12,
13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18,
74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64,
87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15,
39, 15, 74, 33, 57, 10]

nombres=nombres.split()
DicAlumno = dict(zip(nombres,(zip(notas_1,notas_2))))



DicProm= {}
DicProm=dict(map(lambda minimo:(minimo[0],sum(minimo[1])/2),DicAlumno.items()))
for e in DicProm:
    print(e,DicProm[e])



a  = sum(DicProm.values())/ len(nombres)
print (f"el promedio de todos los alumnos es de {a}")



mx=0
nomb=""
for i in DicProm:
    if mx<DicProm[i]:
        mx=DicProm[i]
        nomb= i

print(f"el promedio mas alto fue de {nomb} con una puntuacion de {mx}")        



nmb=""
minimo=999
for o in DicAlumno:
    if minimo > min(DicAlumno[o]):
        minimo= min(DicAlumno[o])
        nmb=o
print(f"el alumno con nota mas baja fue {nmb} con una nota de {minimo}")
