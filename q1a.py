import pyomo.environ as pyo

# Criar um modelo concreto
model = pyo.ConcreteModel()

# Definir variáveis de decisão com limites
model.x1 = pyo.Var(bounds=(0, None))
model.x2 = pyo.Var(bounds=(0, None))
model.M1 = pyo.Var(bounds=(0, None))
model.x3 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x4 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x5 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x6 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x7 = pyo.Var(bounds=(0, None))  # Variável de folga
model.x8 = pyo.Var(bounds=(0, None))  # Variável de folga
model.a1 = pyo.Var(bounds=(0, None))  # Variável artificial
model.a2 = pyo.Var(bounds=(0, None))  # Variável artificial

# Definir a função objetivo
model.obj = pyo.Objective(expr= 300*model.x1 + 400*model.x2 - 50*model.M1, sense=pyo.maximize)

# Definir as restrições
model.constraint1 = pyo.Constraint(expr= 0.8*model.x1 + model.x2 - model.M1 + model.x3 == 0)
model.constraint2 = pyo.Constraint(expr= model.M1 + model.x4 == 98)
model.constraint3 = pyo.Constraint(expr= 0.6*model.x1 + 0.7*model.x2 + model.x5 == 73)
model.constraint4 = pyo.Constraint(expr= 2*model.x1 + 3*model.x2 + model.x6 == 260)
model.constraint4 = pyo.Constraint(expr= model.x1 - model.x7 + model.a1 == 88)
model.constraint4 = pyo.Constraint(expr= model.x2 - model.x8 + model.a2 == 26)

# Definir o solver
solver = pyo.SolverFactory('glpk')

# Resolver o modelo (Fase 1)
results = solver.solve(model, tee=True)

# Remover a variável artificial da função objetivo após Fase 1
model.obj.deactivate()
model.obj = pyo.Objective(expr= 300*model.x1 + 400*model.x2 - 50*model.M1, sense=pyo.maximize)

# Resolver o modelo (Fase 2)
results = solver.solve(model, tee=True)

# Carregar os resultados no modelo
model.solutions.load_from(results)

# Mostrar os resultados
model.display()

# Imprimir valores das variáveis e função objetivo
print(f"x1 = {pyo.value(model.x1)}")
print(f"x2 = {pyo.value(model.x2)}")
print(f"M1 = {pyo.value(model.M1)}")
print(f"Objective (Z) = {pyo.value(model.obj)}")
