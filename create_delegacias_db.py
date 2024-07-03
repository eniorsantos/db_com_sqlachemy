import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///delegacias_db")

base = orm.declarative_base()

class Delegado(base):
                __tablename__ = "tbDelegados"

                id_delegado = sa.Column(sa.CHAR(4),primary_key=True, index=True)
                nome = sa.Column(sa.VARCHAR(100), nullable=False)

class Uf(base):
          __tablename__ = "tbUf"

          cod_uf = sa.Column(sa.CHAR(2), primary_key=True, index=True)
          nome = sa.Column(sa.VARCHAR(50), unique=True)

class Mesoregiao(base):
          __tablename__ = "tbMesoregiao"

          cod_mesoregiao = sa.Column(sa.CHAR(2), primary_key=True, index=True)
          nome = sa.Column(sa.VARCHAR(50), unique=True)
          cod_uf = sa.Column(sa.CHAR(2), sa.ForeignKey("tbUf.cod_uf", ondelete="NO ACTION", onupdate="CASCADE"), index=True)

          
class Distrito(base):
          __tablename__ = "tbDistrito"

          cod_distrito = sa.Column(sa.CHAR(9), primary_key=True, index=True)
          nome = sa.Column(sa.VARCHAR(50), nullable=False)
          cod_mesoregiao = sa.Column(sa.CHAR(2), sa.ForeignKey("tbMesoregiao.cod_mesoregiao", ondelete="NO ACTION", onupdate="CASCADE"), index=True)



class Municipio(base):
          __tablename__ = "tbMunicipio"

          cod_municipio = sa.Column(sa.CHAR(7), primary_key=True, index=True)
          nome = sa.Column(sa.VARCHAR(50), nullable=False)
          num_municipio = sa.Column(sa.CHAR(5), nullable=False)
          cod_distrito = sa.Column(sa.CHAR(2), sa.ForeignKey("tbDistrito", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
          cod_mesoregiao = sa.Column(sa.CHAR(2), sa.ForeignKey("tbMesoregiao", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
          cod_uf = sa.Column(sa.CHAR(2), sa.ForeignKey("tbUf", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
          

class DelegaciaPolicia(base):
          __tablename__ = "tbDelegaciaPolicia"

          id_dp = sa.Column(sa.CHAR(3), primary_key=True, index=True)
          nome = sa.Column(sa.VARCHAR(100), nullable=False, unique=True)
          rua = sa.Column(sa.VARCHAR(100), nullable=False)
          bairro = sa.Column(sa.VARCHAR(50), nullable=False)     
          cod_municipio = sa.Column(sa.CHAR(7), sa.ForeignKey("tbMunicipio.cod_municipio", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
          uf = sa.Column(sa.CHAR(2), nullable=False)
          cep = sa.Column(sa.CHAR(8), nullable=False)
          tel = sa.Column(sa.CHAR(10), nullable=False)
          email = sa.Column(sa.CHAR(50), nullable=False)
          uf = sa.Column(sa.VARCHAR(50), nullable=False)
          id_delegado = sa.Column(sa.CHAR(4),sa.ForeignKey("tbDelegados.id_delegado", ondelete="NO ACTION", onupdate="CASCADE"), index=True)


class Ocorrencia(base):
          __tablename__ = "tbOcorrencia"

          id_ocorrencia = sa.Column(sa.CHAR(5), primary_key=True, index=True)
          cod_ocorrencia = sa.Column(sa.CHAR(5), nullable=False)
          data = sa.Column(sa.DATETIME, nullable=False)
          nome_ocorrencia = sa.Column(sa.VARCHAR(100), nullable=False)
          quantidade = sa.Column(sa.INTEGER, nullable=False) 
          descricao = sa.Column(sa.VARCHAR(500), nullable=False)
          id_dp = sa.Column(sa.CHAR(3), sa.ForeignKey("tbDelegaciaPolicia.id_dp", ondelete="NO ACTION", onupdate="CASCADE"), index=True)
          id_delegado = sa.Column(sa.CHAR(4),sa.ForeignKey("tbDelegados.id_delegado", ondelete="NO ACTION", onupdate="CASCADE"), index=True)



try:
        base.metadata.create_all(engine)
        #print("Banco de dados criado com sucesso!")
except ValueError:
        ValueError()

engine.dispose()