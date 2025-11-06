from models.profissional import Profissional, ProfissionalDAO
from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.receita import Receita, ReceitaDAO
from models.medicamento import Medicamento, MedicamentoDAO
from datetime import datetime

class View:

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def usuario_nunca_admin(testando):
        admins = ["admin", "admin1"]
        return testando.lower() in admins

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha: return{"id": c.get_id(), "nome": c.get_nome(), "email": c.get_email}
        return None
    def cliente_inserir(nome, email, fone, senha):
        try:  
            cliente = Cliente(0, nome, email, fone, senha)
            ClienteDAO.inserir(cliente)
        except ValueError: return
    def cliente_atualizar(id, nome, email, fone, senha):
        try:
            cliente = Cliente(id, nome, email, fone, senha)
            ClienteDAO.atualizar(cliente)
        except ValueError: return
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
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r

    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        try:
            profissio = Profissional(0, nome, especialidade, conselho, email, senha)
            ProfissionalDAO.inserir(profissio)
        except ValueError: return
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        try:
            profissio = Profissional(id, nome, especialidade, conselho, email, senha)
            ProfissionalDAO.atualizar(profissio)
        except ValueError: return
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
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
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
        try:
            c = Horario(0, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            c.set_id_profissional(id_profissio)
            HorarioDAO.inserir(c)
        except ValueError: return
    def horario_listar():
        View.horario_ministrar()
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissio):
        try:
            c = Horario(id, data)
            c.set_confirmado(confirmado)
            c.set_id_cliente(id_cliente)
            c.set_id_servico(id_servico)
            c.set_id_profissional(id_profissio)
            HorarioDAO.atualizar(c)
        except ValueError: return
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    def horario_ministrar():
        HORARIOS = HorarioDAO.listar() #confirma a lista
        if len(HORARIOS) != 0:
            for Hora in HORARIOS:
                if Hora.get_data() < datetime.now():
                    View.horario_excluir(Hora.get_id()) #exclui os antigos
    def horario_listar_id(id):
        View.horario_ministrar()
        horario = HorarioDAO.listar_id(id)
        return horario
    def horario_listar_id_cliente(id):
        View.horario_ministrar()
        horario = HorarioDAO.listar_id_cliente(id)
        return horario
    def horario_listar_id_profissional(id):
        View.horario_ministrar()
        horario = HorarioDAO.listar_id_profissional(id)
        return horario
    def horario_agendar_horario(id_profissional):
        View.horario_ministrar()
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    
    def receita_ministrar(): #excluir receitas vencidas do json
    def receita_listar():
    def receita_excluir():
    def receita_listar_id():
    def receita_listar_id_cliente(): #ver as receitas de cada cliente
    def receita_inserir():

    def medicamento_listar():
    def medicamento_excluir():
    def medicamento_atualizar():
    def medicamento_listar_id():
    def medicamento_inserir():