import pyomo.environ as pyo

# Primeira Fase
def PrimeiraFase():
    model = pyo.ConcreteModel()
    model.x1 = pyo.Var(bounds=(0, None))
    model.x2 = pyo.Var(bounds=(0, None))
    model.x3 = pyo.Var(bounds=(0, None)) 
    model.x4 = pyo.Var(bounds=(0, None))
    model.A1 = pyo.Var(bounds=(0, None)) # Variável artificial
    model.A2 = pyo.Var(bounds=(0, None)) # Variável artificial
    model.A3 = pyo.Var(bounds=(0, None)) # Variável artificial

    # Função artificial Z
    model.obj = pyo.Objective(expr=model.A1 + model.A2 + model.A3, sense=pyo.minimize)

    # Restrições
    model.constraint1 = pyo.Constraint(expr=model.x1 + model.x2 + model.x3 + model.x4 + model.A1 == 4)
    model.constraint2 = pyo.Constraint(expr=-2*model.x1 + model.x2 - model.x3 + model.A2 == 1)
    model.constraint3 = pyo.Constraint(expr=3*model.x2 + model.x3 + model.x4 + model.A3 == 9)

    solver = pyo.SolverFactory('glpk') # Definindo o solver
    results = solver.solve(model, tee=True)  # Resolvendo o modelo
    model.solutions.load_from(results) # Carregar os resultados no modelo
    model.display() # Exibir resultados

    return model

# Segunda Fase
def SegundaFase(x1_init, x2_init, x3_init, x4_init):
    model = pyo.ConcreteModel()
    model.x1 = pyo.Var(bounds=(0, None), initialize=x1_init)
    model.x2 = pyo.Var(bounds=(0, None), initialize=x2_init) 
    model.x3 = pyo.Var(bounds=(0, None), initialize=x4_init)
    model.x4 = pyo.Var(bounds=(0, None), initialize=x3_init)

    # Função objetivo z
    model.obj = pyo.Objective(expr=-3*model.x1 + model.x3, sense=pyo.maximize)

    # Restrições
    model.constraint1 = pyo.Constraint(expr=model.x1 + model.x2 + model.x3 + model.x4 == 4)
    model.constraint2 = pyo.Constraint(expr=-2*model.x1 + model.x2 - model.x3 == 1)
    model.constraint3 = pyo.Constraint(expr=3*model.x2 + model.x3 + model.x4 == 9)

    solver = pyo.SolverFactory('glpk') # Definindo o solver
    results = solver.solve(model, tee=True)  # Resolvendo o modelo
    model.solutions.load_from(results) # Carregar os resultados no modelo
    model.display() # Exibir resultados

    return model

# Executar Primeira Fase
modelo_fase1 = PrimeiraFase()
print(f"x1 = {pyo.value(modelo_fase1.x1)}")
print(f"x2 = {pyo.value(modelo_fase1.x2)}")
print(f"x3 = {pyo.value(modelo_fase1.x3)}")
print(f"x4 = {pyo.value(modelo_fase1.x4)}")
print(f"A1 = {pyo.value(modelo_fase1.A1)}")
print(f"A2 = {pyo.value(modelo_fase1.A2)}")
print(f"A3 = {pyo.value(modelo_fase1.A3)}")
print(f"Z artificial = {pyo.value(modelo_fase1.obj)}")

# Verificar se variáveis artificiais são zero
if pyo.value(modelo_fase1.A1) == 0 and pyo.value(modelo_fase1.A2) == 0 and pyo.value(modelo_fase1.A3) == 0:
    x1 = pyo.value(modelo_fase1.x1)
    x2 = pyo.value(modelo_fase1.x2)
    x3 = pyo.value(modelo_fase1.x3)
    x4 = pyo.value(modelo_fase1.x4)

    # Executar Segunda Fase
    modelo_fase2 = SegundaFase(x1, x2, x3, x4)
    print(f"x1 = {pyo.value(modelo_fase2.x1)}")
    print(f"x2 = {pyo.value(modelo_fase2.x2)}")
    print(f"x3 = {pyo.value(modelo_fase2.x3)}")
    print(f"x4 = {pyo.value(modelo_fase2.x4)}")
    print(f"Z objetivo = {pyo.value(modelo_fase2.obj)}")
else:
    print("O problema não tem solução viável (variáveis artificiais não são zero).")
