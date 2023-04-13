def new_structure(names,score_1,score_2):
    names=names.replace("\n","").replace("'","").replace(" ","").strip().split(",")
    student_score=list(zip(names,score_1,score_2))
    return {elem[0]:(elem[1],elem[2]) for elem in student_score}

def average(dictionary):
    average=list(zip(dictionary,map(lambda x: sum(x)/len(x) if(len(x)>0) else "Notas no cargadas",dictionary.values())))
    return {elem[0]:elem[1] for elem in average}

def general_average(dictionary):
    student_average=average(dictionary)
    return sum(student_average.values())/len(student_average) if(len(student_average)>0) else "No hay notas de alumnos cargadas"

def the_best(dictionary):
    student_average=average(dictionary)
    return max(student_average.items(), key=lambda s:s[1])[0]

def the_worst(dictionary):
    return min(dictionary.items(),key=lambda s:s[1])[0]

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

diccionario=new_structure(nombres,notas_1,notas_2)

print("Promedio de cada estudante: ")
print(average(diccionario))
print(f"Promedio general del curso: {general_average(diccionario)}")
print("Estudiante con la nota promedio mas alta: " + the_best(diccionario))
print("Estudiante con la nota mas baja: " + the_worst(diccionario))