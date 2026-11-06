print("===================================")
print("        AURA HOME 2050")
print("      CASA INTELIGENTE")
print("===================================")

luz_sala = False
luz_quarto = False
luz_cozinha = False
ventilador = False
porta = False
alarme = False
temperatura = 24
presenca = False


def mostrar_estado():
    print("\n========== ESTADO DA CASA ==========")
    print("Luz da sala:", "LIGADA" if luz_sala else "DESLIGADA")
    print("Luz do quarto:", "LIGADA" if luz_quarto else "DESLIGADA")
    print("Luz da cozinha:", "LIGADA" if luz_cozinha else "DESLIGADA")
    print("Ventilador:", "LIGADO" if ventilador else "DESLIGADO")
    print("Porta:", "ABERTA" if porta else "FECHADA")
    print("Alarme:", "ATIVADO" if alarme else "DESATIVADO")
    print("Presenca:", "DETECTADA" if presenca else "NENHUMA")
    print("Temperatura:", temperatura, "graus")
    print("====================================")


def ligar_sala():
    global luz_sala
    luz_sala = True
    print("Luz da sala ligada.")


def desligar_sala():
    global luz_sala
    luz_sala = False
    print("Luz da sala desligada.")


def ligar_quarto():
    global luz_quarto
    luz_quarto = True
    print("Luz do quarto ligada.")


def desligar_quarto():
    global luz_quarto
    luz_quarto = False
    print("Luz do quarto desligada.")


def ligar_cozinha():
    global luz_cozinha
    luz_cozinha = True
    print("Luz da cozinha ligada.")


def desligar_cozinha():
    global luz_cozinha
    luz_cozinha = False
    print("Luz da cozinha desligada.")


def ligar_ventilador():
    global ventilador
    ventilador = True
    print("Ventilador ligado.")


def desligar_ventilador():
    global ventilador
    ventilador = False
    print("Ventilador desligado.")


def abrir_porta():
    global porta
    porta = True
    print("Porta aberta.")


def fechar_porta():
    global porta
    porta = False
    print("Porta fechada.")


def ativar_alarme():
    global alarme
    alarme = True
    print("Alarme ativado.")


def desativar_alarme():
    global alarme
    alarme = False
    print("Alarme desativado.")


def detectar_presenca():
    global presenca
    presenca = True
    print("Presenca detectada.")


def remover_presenca():
    global presenca
    presenca = False
    print("Nenhuma presenca detectada.")


def mudar_temperatura(novo_valor):
    global temperatura
    temperatura = int(novo_valor)
    print("Temperatura:", temperatura, "graus")


def modo_cinema():
    global luz_sala
    global luz_quarto
    global luz_cozinha
    global ventilador

    luz_sala = False
    luz_quarto = False
    luz_cozinha = False

    if temperatura >= 25:
        ventilador = True
    else:
        ventilador = False

    print("\nModo CINEMA ativado!")
    print("Luzes desligadas.")
    print("Ventilador ajustado automaticamente.")


def modo_boa_noite():
    global luz_sala
    global luz_quarto
    global luz_cozinha
    global ventilador

    luz_sala = False
    luz_quarto = False
    luz_cozinha = False
    ventilador = False

    fechar_porta()
    ativar_alarme()

    print("\nModo BOA NOITE ativado!")


def verificar_automacao():
    global ventilador

    print("\n========== AUTOMACAO ==========")

    if temperatura >= 28:
        ventilador = True
        print("Temperatura alta -> ventilador ligado.")
    elif temperatura < 24:
        ventilador = False
        print("Temperatura baixa -> ventilador desligado.")
    else:
        print("Temperatura normal.")

    if alarme and porta:
        print("ALERTA: porta aberta com alarme ativado.")

    if presenca:
        print("Sistema detectou alguem na casa.")

    print("===============================")