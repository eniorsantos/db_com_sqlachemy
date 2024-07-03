import sqlalchemy as sa
import sqlalchemy.orm as orm
import pandas as pd
import create_delegacias_db as bddp

endereco_uf = "uf.xlsx"
endereco_mesoregiao = "mesoregiao.xlsx"
endereco_distrito = "distrito.xlsx"
endereco_municipio = "municipio.xlsx"
endereco_delegados = "delegados.xlsx"
endereco_delegacias = "delegacias.xlsx"
endereco_ocorrencia = "ocorrencias.xlsx"


dfUf = pd.DataFrame(pd.read_excel(endereco_uf, sheet_name="Uf"))
dfMesoregiao = pd.DataFrame(pd.read_excel(endereco_mesoregiao, sheet_name="Mesoregiao"))
dfDistrito = pd.DataFrame(pd.read_excel(endereco_distrito, sheet_name="Distrito"))
dfMunicipio = pd.DataFrame(pd.read_excel(endereco_municipio, sheet_name="Municipio"))
dfDelegados = pd.DataFrame(pd.read_excel(endereco_delegados, sheet_name="Delegados"))
dfDelegacias = pd.DataFrame(pd.read_excel(endereco_delegacias, sheet_name="Delegacias"))
dfOcorrencia = pd.DataFrame(pd.read_excel(endereco_ocorrencia, sheet_name="Ocorrencia"))



engine = sa.create_engine("sqlite:///delegacias_db")

Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

conn = engine.connect()
metadata = sa.schema.MetaData()
metadata.reflect(bind=engine)



dados_delegacias = dfUf.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.Uf.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela UF. Dados inseridos com sucesso!")



dados_delegacias = dfMesoregiao.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.Mesoregiao.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela Mesorregiao. Dados inseridos com sucesso!")



dados_delegacias = dfDistrito.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.Distrito.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela Distrito. Dados inseridos com sucesso!")



dados_delegacias = dfMunicipio.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.Municipio.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela Municipio. Dados inseridos com sucesso!")



dados_delegacias = dfDelegados.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.Delegado.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela Delegados. Dados inseridos com sucesso!")



dados_delegacias = dfDelegacias.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.DelegaciaPolicia.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela Delegacias. Dados inseridos com sucesso!")



dados_delegacias = dfOcorrencia.to_dict(orient='records')
meta_delegacias = sa.Table(bddp.Ocorrencia.__tablename__,metadata, autoload=True)

try:
    conn.execute(meta_delegacias.insert(), dados_delegacias)
    sessao.commit()
    conn.commit()

except ValueError:
    ValueError()

print("Tabela Ocorrencias. Registradas com sucesso!")

conn.close()

sessao.close_all()

engine.dispose()