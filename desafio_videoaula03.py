#variavel que define horario
horario = 24
#schema de condições para mensagens programadas de cumprimento!
if horario >= 5.0 and horario <= 11.0:
    print("Bom dia!")
elif horario >= 12.0 and horario <= 18.0:
    print("Boa tarde!")
elif horario >= 19.0 and horario <= 23.0:
    print("Boa noite!")
else:
    print("Boa madrugada!")