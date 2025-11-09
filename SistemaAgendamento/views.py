from models.profissional import Profissional, ProfissionalDAO
from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.receita import Receita, ReceitaDAO
from models.medicamento import Medicamento, MedicamentoDAO
from datetime import datetime

class View:

    def cliente_criar_admin():
        list = View.cliente_listar()
        for c in list:
            if c.get_email() == "admin" and c.get_nome() == "admin": return
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
    '''def horario_ministrar():
        HORARIOS = HorarioDAO.listar() #confirma a lista
        if len(HORARIOS) != 0:
            for Hora in HORARIOS:
                if Hora.get_data() < datetime.now():
                    View.horario_excluir(Hora.get_id()) #exclui os antigos'''
    def horario_listar_id(id):
        horario = HorarioDAO.listar_id(id)
        return horario
    def horario_listar_id_cliente(id):
        horario = HorarioDAO.listar_id_cliente(id)
        return horario
    def horario_listar_id_profissional(id):
        horario = HorarioDAO.listar_id_profissional(id)
        return horario
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data())
        return r
    
    '''def receita_ministrar(): #excluir receitas vencidas do json
        RECEITAS = ReceitaDAO.listar() #confirma a lista
        if len(RECEITAS) != 0:
            for receita in RECEITAS:
                if receita.get_data() < datetime.now():
                    View.receita_excluir(receita.get_id()) #exclui os antigos'''
    def receita_listar():
        return ReceitaDAO.listar
    def receita_excluir(id):
        reci = Receita(id, "", "", "", "", "", None)
        ReceitaDAO.excluir(reci)
    def receita_listar_id(id):
        return ReceitaDAO.listar_id(id)
    def receita_listar_id_cliente(id): #ver as receitas de cada cliente
        return ReceitaDAO.listar_id_cliente(id)
    def receita_inserir(id_medicamento, id_profissional, id_cliente, periodo, dosagem):
        try:
            receita = Receita(0, id_medicamento, id_profissional, id_cliente, periodo, dosagem)
            receita.set_emissao(datetime.now())
            ReceitaDAO.inserir(receita)
        except ValueError: return

    def Estar(algo, apli):
        lit = View.medicamento_listar()
        for i in lit:
            if i.get_nome() == algo: 
                if i.get_aplicacao() == apli: return True
        return False
    def medicamento_listar():
        return MedicamentoDAO.listar()
    def medicamento_excluir(id):
        medi = Medicamento(id, "n", "n", "n")
        MedicamentoDAO.excluir(medi)
    def medicamento_atualizar(id, nome, objetivo, aplicacao):
        medicamento = Medicamento(id, nome, objetivo, aplicacao)
        MedicamentoDAO.atualizar(medicamento)
    def medicamento_listar_id(id):
        return MedicamentoDAO.listar_id(id)
    def medicamento_inserir(nome, objetivo, aplicacao):
        try:
            medicamento = Medicamento(0, nome, objetivo, aplicacao)
            MedicamentoDAO.inserir(medicamento)
        except ValueError: return

View.cliente_criar_admin() # verifica se existe o usuário admin