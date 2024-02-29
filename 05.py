print("Ejercicio práctico 1")
Este_curso=1.5
mínimo= 2.5
máximo= 7
promedio = 4
lista_de_otros_cursos = list([mínimo,máximo,promedio])
promedio_cursos = (mínimo + máximo + promedio + Este_curso)/4
lista_de_otros_cursos.sort()
print(f"El más rápido de los otros cursos es {lista_de_otros_cursos[0]}")
print(f"El más lento de los otros cursos es {lista_de_otros_cursos[2]} ")
print(f"el promedio de los cursos es {promedio_cursos}")
print("Ejercicio número 2 b:")
crudo_este_curso = 3.5
crudo_promedio = 5
porce_inservible_este_curso = (crudo_este_curso - Este_curso)/crudo_este_curso
print(f"el pocentaje de material inservible es: {porce_inservible_este_curso*100} %")
porce_inservible_promedio = (crudo_promedio-promedio)/crudo_promedio
print(f"el promedio de material inservible es: {porce_inservible_promedio*100}%")
parte_todo=[0,0,0]
parte_todo[0] = máximo/Este_curso
parte_todo[1] = mínimo/Este_curso
parte_todo[2] = promedio/Este_curso
for i in range(3):
    parte_todo[i] *= 10
    print(parte_todo[i])