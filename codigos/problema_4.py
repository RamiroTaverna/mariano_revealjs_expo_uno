from pulp import LpMaximize, LpProblem, LpVariable, value

# Crear el problema
modelo = LpProblem(name="joyas-beneficio-maximo", sense=LpMaximize)

# Variables: cantidad de joyas tipo A (x) y tipo B (y)
x = LpVariable(name="joyas_tipo_A", lowBound=0, cat='Integer')
y = LpVariable(name="joyas_tipo_B", lowBound=0, cat='Integer')

# Función objetivo: maximizar beneficio
modelo += 40 * x + 50 * y, "Beneficio_total"

# Restricciones de recursos
modelo += x + 1.5 * y <= 750, "Oro_disponible"
modelo += 1.5 * x + y <= 750, "Plata_disponible"

# Resolver el modelo
modelo.solve()

# Resultados
print(f"Cantidad de joyas tipo A: {x.value()}")
print(f"Cantidad de joyas tipo B: {y.value()}")
print(f"Beneficio máximo: {value(modelo.objective)} €")
