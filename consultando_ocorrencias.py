import sqlalchemy as sa
import sqlalchemy.orm as orm
import pandas as pd
import create_delegacias_db as bddp

engine = sa.create_engine("sqlite:///delegacias_db")

Sessao = orm.sessionmaker(bind=engine)
sessao = Sessao()

RankOcorrencias =  pd.DataFrame(sessao.query(
                    bddp.DelegaciaPolicia.nome.label('Delegacia'),                    
                    bddp.DelegaciaPolicia.id_dp,
                    bddp.Ocorrencia.nome_ocorrencia,
                    sa.func.sum(bddp.Ocorrencia.quantidade).label('Volume de Ocorrencia')                   
                    ).join(                        
                      bddp.DelegaciaPolicia,
                      bddp.Ocorrencia.id_dp == bddp.DelegaciaPolicia.id_dp
                    ).filter(bddp.DelegaciaPolicia.id_dp == 59).group_by(
                      bddp.Ocorrencia.nome_ocorrencia
                    ).all()
)

print(RankOcorrencias)