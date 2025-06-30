from pulp import LpProblem, LpMinimize, LpVariable, value

# Crear el problema
modelo = LpProblem(name="minimizar_costos_trabajadores", sense=LpMinimize)

# Variables
a = LpVariable(name="horas_trabajador_A", lowBound=0, upBound=40)
b = LpVariable(name="horas_trabajador_B", lowBound=0, upBound=50)
c = LpVariable(name="horas_trabajador_C", lowBound=0, upBound=60)

# Función objetivo: minimizar el costo total
modelo += 20 * a + 18 * b + 15 * c, "Costo_total"

# Restricción de horas requeridas
modelo += a + b + c == 120, "Horas_totales"

# Resolver
modelo.solve()

# Resultados
print(f"Horas trabajadas por A: {a.value()}")
print(f"Horas trabajadas por B: {b.value()}")
print(f"Horas trabajadas por C: {c.value()}")
print(f"Costo mínimo total: ${value(modelo.objective)}")
