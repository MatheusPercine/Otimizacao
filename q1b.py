import pyomo.environ as pyo

# Modelo concreto
model = pyo.ConcreteModel()

# Variáveis de decisão
model.x1 = pyo.Var(bounds=(0, None))
model.x2 = pyo.Var(bounds=(0, None))
model.M1 = pyo.Var(bounds=(0, None))
model.x3 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x4 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x5 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x6 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x7 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x8 = pyo.Var(bounds=(0, None))  # Variável de folga

# Função objetivo
model.obj = pyo.Objective(expr= 310*model.x1 + 400*model.x2 - 50*model.M1, sense=pyo.maximize)

# Restrições
model.constraint1 = pyo.Constraint(expr= 0.8*model.x1 + model.x2 - model.M1 + model.x3 == 0)
model.constraint2 = pyo.Constraint(expr= model.M1 + model.x4 == 98)
model.constraint3 = pyo.Constraint(expr= 0.6*model.x1 + 0.7*model.x2 + model.x5 == 73)
model.constraint4 = pyo.Constraint(expr= 2*model.x1 + 3*model.x2 + model.x6 == 260)
model.constraint5 = pyo.Constraint(expr= model.x1 - model.x7 == 88)
model.constraint6 = pyo.Constraint(expr= model.x2 - model.x8 == 26)

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
print(f"M1 = {pyo.value(model.M1)}")
print(f"Objective (Z) = {pyo.value(model.obj)}")
