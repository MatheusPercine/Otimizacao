import pyomo.environ as pyo

# Modelo concreto
model = pyo.ConcreteModel()

# Variáveis de decisão
model.x1 = pyo.Var(bounds=(0, None))
model.x2 = pyo.Var(bounds=(0, None))
model.x3 = pyo.Var(bounds=(0, None))
model.x4 = pyo.Var(bounds=(0, None))

# Função objetivo
model.obj = pyo.Objective(expr=-3*model.x1 + model.x3, sense=pyo.maximize)

# Restrições
model.constraint1 = pyo.Constraint(expr=model.x1 + model.x2 + model.x3 + model.x4 == 4)
model.constraint2 = pyo.Constraint(expr=-2*model.x1 + model.x2 - model.x3 == 1)
model.constraint3 = pyo.Constraint(expr=3*model.x2 + model.x3 + model.x4 == 9)

# Solver
solver = pyo.SolverFactory('glpk')
results = solver.solve(model, tee=True)

# Carregar resultados no modelo
model.solutions.load_from(results)

# Exibir resultados
model.display()

# Imprimir valores das variáveis e função objetivo
print(f"x1 = {pyo.value(model.x1)}")
print(f"x2 = {pyo.value(model.x2)}")
print(f"x3 = {pyo.value(model.x3)}")
print(f"x4 = {pyo.value(model.x4)}")
print(f"Objective (Z) = {pyo.value(model.obj)}")
