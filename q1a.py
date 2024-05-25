import pyomo.environ as pyo

# Primeira Fase
def PrimeiraFase():
    model = pyo.ConcreteModel()
    model.x1 = pyo.Var(bounds=(0, None))
    model.x2 = pyo.Var(bounds=(0, None))
    model.m1 = pyo.Var(bounds=(0, None))
    model.x3 = pyo.Var(bounds=(0, None)) # Variável de folga
    model.x4 = pyo.Var(bounds=(0, None)) # Variável de folga
    model.x5 = pyo.Var(bounds=(0, None)) # Variável de folga
    model.x6 = pyo.Var(bounds=(0, None)) # Variável de folga
    model.x7 = pyo.Var(bounds=(0, None)) # Variável de folga
    model.x8 = pyo.Var(bounds=(0, None)) # Variável de folga
    model.A1 = pyo.Var(bounds=(0, None)) # Variável artificial para a restrição 1
    model.A2 = pyo.Var(bounds=(0, None)) # Variável artificial para a restrição 2

    # Função artificial Z
    model.obj = pyo.Objective(expr=model.A1 + model.A2, sense=pyo.minimize)

    # Restrições
    model.constraint1 = pyo.Constraint(expr=0.8*model.x1 + model.x2 - model.m1 + model.x3 == 0)
    model.constraint2 = pyo.Constraint(expr=model.m1 + model.x4 == 98)
    model.constraint3 = pyo.Constraint(expr=0.6*model.x1 + 0.7*model.x2 + model.x5 == 73)
    model.constraint4 = pyo.Constraint(expr=2*model.x1 + 3*model.x2 + model.x6 == 260)
    model.constraint5 = pyo.Constraint(expr=model.x1 - model.x7 + model.A1 == 88)
    model.constraint6 = pyo.Constraint(expr=model.x2 - model.x8 + model.A2 == 26)

    solver = pyo.SolverFactory('glpk') # Definindo o solver
    results = solver.solve(model, tee=True)  # Resolvendo o modelo
    model.solutions.load_from(results) # Carregar os resultados no modelo
    model.display() # Exibir resultados

    return model

# Segunda Fase
def SegundaFase(x1_init, x2_init, m1_init, x3_init, x4_init, x5_init, x6_init, x7_init, x8_init):
    model = pyo.ConcreteModel()
    model.x1 = pyo.Var(bounds=(0, None), initialize=x1_init)
    model.x2 = pyo.Var(bounds=(0, None), initialize=x2_init) 
    model.m1 = pyo.Var(bounds=(0, None), initialize=m1_init)
    model.x3 = pyo.Var(bounds=(0, None), initialize=x3_init) # Variável de folga
    model.x4 = pyo.Var(bounds=(0, None), initialize=x4_init) # Variável de folga
    model.x5 = pyo.Var(bounds=(0, None), initialize=x5_init) # Variável de folga
    model.x6 = pyo.Var(bounds=(0, None), initialize=x6_init) # Variável de folga
    model.x7 = pyo.Var(bounds=(0, None), initialize=x7_init) # Variável de folga
    model.x8 = pyo.Var(bounds=(0, None), initialize=x8_init) # Variável de folga

    # Função objetivo z
    model.obj = pyo.Objective(expr=300*model.x1 + 400*model.x2 - 50*model.m1, sense=pyo.maximize)

    # Restrições
    model.constraint1 = pyo.Constraint(expr= 0.8*model.x1 + model.x2 - model.m1 + model.x3 == 0)
    model.constraint2 = pyo.Constraint(expr= model.m1 + model.x4 == 98)
    model.constraint3 = pyo.Constraint(expr= 0.6*model.x1 + 0.7*model.x2 + model.x5 == 73)
    model.constraint4 = pyo.Constraint(expr= 2*model.x1 + 3*model.x2 + model.x6 == 260)
    model.constraint5 = pyo.Constraint(expr= model.x1 - model.x7  == 88)
    model.constraint6 = pyo.Constraint(expr= model.x2 - model.x8 == 26)

    solver = pyo.SolverFactory('glpk') # Definindo o solver
    results = solver.solve(model, tee=True)  # Resolvendo o modelo
    model.solutions.load_from(results) # Carregar os resultados no modelo
    model.display() # Exibir resultados

    return model

# Executar Primeira Fase
modelo_fase1 = PrimeiraFase()
print(f"x1 = {pyo.value(modelo_fase1.x1)}")
print(f"x2 = {pyo.value(modelo_fase1.x2)}")
print(f"m1 = {pyo.value(modelo_fase1.m1)}")
print(f"x3 = {pyo.value(modelo_fase1.x3)}")
print(f"x4 = {pyo.value(modelo_fase1.x4)}")
print(f"x5 = {pyo.value(modelo_fase1.x5)}")
print(f"x6 = {pyo.value(modelo_fase1.x6)}")
print(f"x7 = {pyo.value(modelo_fase1.x7)}")
print(f"x8 = {pyo.value(modelo_fase1.x8)}")
print(f"A1 = {pyo.value(modelo_fase1.A1)}")
print(f"A2 = {pyo.value(modelo_fase1.A2)}")
print(f"Z artificial = {pyo.value(modelo_fase1.obj)}")

# Verificar se variáveis artificiais são zero
if pyo.value(modelo_fase1.A1) == 0 and pyo.value(modelo_fase1.A2) == 0:
    x1 = pyo.value(modelo_fase1.x1)
    x2 = pyo.value(modelo_fase1.x2)
    m1 = pyo.value(modelo_fase1.m1)
    x3 = pyo.value(modelo_fase1.x3)
    x4 = pyo.value(modelo_fase1.x4)
    x5 = pyo.value(modelo_fase1.x5)
    x6 = pyo.value(modelo_fase1.x6)
    x7 = pyo.value(modelo_fase1.x7)
    x8 = pyo.value(modelo_fase1.x8)

    # Executar Segunda Fase
    modelo_fase2 = SegundaFase(x1, x2, m1, x3, x4, x5, x6, x7, x8)
    print(f"x1 = {pyo.value(modelo_fase2.x1)}")
    print(f"x2 = {pyo.value(modelo_fase2.x2)}")
    print(f"M1 = {pyo.value(modelo_fase2.m1)}")
    print(f"Z objetivo = {pyo.value(modelo_fase2.obj)}")
else:
    print("O problema não tem solução viável (variáveis artificiais não são zero).")
