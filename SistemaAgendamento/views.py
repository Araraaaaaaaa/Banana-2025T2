from models.profissional import Profissional, ProfissionalDAO
from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO

class View:

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha: return{"id": c.get_id(), "nome": c.get_nome(), "email": c.get_email}
        return None
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
    def email_duplicado_cliente(email):
        for dup in View.cliente_listar():
            if dup.get_email() == email: return True
        return False


    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        profissio = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissio)
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        profissio = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissio)
    def profissional_excluir(id):
        profissio = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(profissio)
    def profissional_listar_id(id):
        profissio = ProfissionalDAO.listar_id(id)
        return profissio
    def profissional_autenticar(email, senha):
        for c in View.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha: return{"id": c.get_id(), "nome": c.get_nome(), "email": c.get_email}
        return None
    def email_duplicado_profissional(email):
        for dup in View.profissional_listar():
            if dup.get_email() == email: return True
        return False
    

    def servico_listar():
        return ServicoDAO.listar()
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissio):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissio)
        HorarioDAO.inserir(c)
    def horario_listar():
        return HorarioDAO.listar()
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissio):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissio)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    def horario_listar_id(id):
        horario = HorarioDAO.listar_id(id)
        return horario