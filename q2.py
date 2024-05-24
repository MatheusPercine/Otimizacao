import pyomo.environ as pyo

# Criar um modelo concreto
model = pyo.ConcreteModel()

# Definir variáveis de decisão com limites
model.x1 = pyo.Var(bounds=(0, None))
model.x2 = pyo.Var(bounds=(0, None))
model.x3 = pyo.Var(bounds=(0, None)) 
model.x4 = pyo.Var(bounds=(0, None))
model.a1 = pyo.Var(bounds=(0, None))  # Variável artificial
model.a2 = pyo.Var(bounds=(0, None))  # Variável artificial
model.a3 = pyo.Var(bounds=(0, None))  # Variável artificial

# Definir a função objetivo
model.obj = pyo.Objective(expr= -3*model.x1 + model.x3, sense=pyo.maximize)

# Definir as restrições
model.constraint1 = pyo.Constraint(expr= model.x1 + model.x2 + model.x3 + model.x4 + model.a1 == 4)
model.constraint1 = pyo.Constraint(expr= -2*model.x1 + model.x2 - model.x3 + model.a2 == 1)
model.constraint1 = pyo.Constraint(expr= 3*model.x2 + model.x3 + model.x4 + model.a3 == 4)

# Definir o solver
solver = pyo.SolverFactory('glpk')

# Resolver o modelo (Fase 1)
results = solver.solve(model, tee=True)

# Remover a variável artificial da função objetivo após Fase 1
model.obj.deactivate()
model.obj = pyo.Objective(expr= -3*model.x1 + model.x3, sense=pyo.maximize)

# Resolver o modelo (Fase 2)
results = solver.solve(model, tee=True)

# Carregar os resultados no modelo
model.solutions.load_from(results)

# Mostrar os resultados
model.display()

# Imprimir valores das variáveis e função objetivo
print(f"x1 = {pyo.value(model.x1)}")
print(f"x2 = {pyo.value(model.x2)}")
print(f"Objective (Z) = {pyo.value(model.obj)}")
