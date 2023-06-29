# TAD Posicao

# Construtor

'''cria_posicao(x,y) recebe os valores correspondentes  as coordenadas de uma
posicao e devolve a posicao correspondente. O construtor verifica a validade
dos seus argumentos, gerando um ValueError com a mensagem 'cria posicao:
argumentos invalidos' caso os seus argumentos nao sejam validos.'''


def cria_posicao(x, y):
    if eh_posicao((x, y)):
        posicao = (x, y)
        return posicao
    else:
        raise ValueError("cria_posicao: argumentos invalidos")


'''cria copia posicao: posicao -> posicao
cria copia posicao(p) recebe uma posicao e devolve uma copia nova da posicao.'''


def cria_copia_posicao(posicao):
    tupla_copia = (posicao[0], posicao[1])
    return tupla_copia


# Seletores

'''obter pos x : posicao -> int
obter pos x(p) devolve a componente x da posicao p.'''


def obter_pos_x(posicao):
    return posicao[0]


'''obter pos y : posicao -> int
obter pos y(p) devolve a componente y da posicao p.'''


def obter_pos_y(posicao):
    return posicao[1]


# Reconhecedor

'''eh posicao: universal -> booleano
eh posicao(arg) devolve True caso o seu argumento seja um TAD posicao e
False caso contrario.'''


def eh_posicao(TAD):
    if isinstance(TAD, tuple) and len(TAD) == 2 and isinstance(TAD[0], int) and isinstance(TAD[1], int) and TAD[
        0] >= 0 and TAD[1] >= 0:
        return True
    else:
        return False


# Teste

'''posicoes iguais: posicao × posicao -> booleano
posicoes iguais(p1, p2) devolve True apenas se p1 e p2 sao posicoes e sao
iguais.'''


def posicoes_iguais(posicao1, posicao2):
    if posicao1[0] == posicao2[0] and posicao1[1] == posicao2[1]:
        return True
    else:
        return False


# Transformador

'''posicao para str : posicao -> str
posicao para str(p) devolve a cadeia de caracteres '(x, y)' que representa o
seu argumento, sendo os valores x e y as coordenadas de p.'''


def posicao_para_str(posicao):
    return "({}, {})".format(posicao[0], posicao[1])


# Funcoes alto nivel

'''obter posicoes adjacentes: posicao -> tuplo
obter posicoes adjacentes(p) devolve um tuplo com as posi coes adjacentes  a posicao
p, comecando pela posi cao acima de p e seguindo no sentido horario.'''


def obter_posicoes_adjacentes(posicao):
    list_ajd = []
    if posicao[1] - 1 >= 0:
        list_ajd.append(cria_posicao(posicao[0], posicao[1] - 1))

    list_ajd.append(cria_posicao(posicao[0] + 1, posicao[1]))

    list_ajd.append(cria_posicao(posicao[0], posicao[1] + 1))

    if posicao[0] - 1 >= 0:
        list_ajd.append(cria_posicao(posicao[0] - 1, posicao[1]))

    return tuple(list_ajd)


'''ordenar posicoes: tuplo 7 -> tuplo
ordenar posicoes(t) devolve um tuplo contendo as mesmas posicoes do tuplo fornecido
como argumento, ordenadas de acordo com a ordem de leitura do prado.'''


def ordenar_posicoes(posicoes):
    lista = [posicoes[0]]
    for p in posicoes[1:]:
        flag_maior = True
        for i, p2 in enumerate(lista):
            if obter_pos_y(p) < obter_pos_y(p2):
                lista.insert(i, p)
                flag_maior = False
                break
            elif obter_pos_y(p) == obter_pos_y(p2) and obter_pos_x(p) < obter_pos_x(p2):
                lista.insert(i, p)
                flag_maior = False
                break

        if flag_maior:
            lista.append(p)

    return tuple(lista)


# TAD Animal

# Construtor

'''cria animal: str × int × int -> animal
cria animal(s, r, a) recebe uma cadeia de caracteres nao vazia correspondente
a especie do animal e dois valores inteiros correspondentes a frequencia
de reproducao r (maior do que 0) e  a frequencia de alimentacao a (maior
ou igual que 0); e devolve o animal. Animais com frequencia de alimentacao
maior que 0 sao considerados predadores, caso contrario sao considerados
presas. O construtor verifica a validade dos seus argumentos, gerando um
ValueError com a mensagem 'cria animal: argumentos invalidos' caso
os seus argumentos nao sejam validos.'''


def cria_animal(s, r, a):
    dict_animal = {"s": s, "r": [0, r], "a": [0, a]}
    if eh_animal(dict_animal):
        return dict_animal
    else:
        raise ValueError("cria_animal: argumentos invalidos")


'''cria copia animal: animal -> animal
cria copia animal(a) recebe um animal a (predador ou presa) e devolve uma
nova copia do animal.'''


def cria_copia_animal(animal):
    dict_animal_copia = {}
    for key, value in animal.items():
        if isinstance(value, list):
            dict_animal_copia[key] = []
            for v in value:
                dict_animal_copia[key].append(v)
        else:
            dict_animal_copia[key] = value
    return dict_animal_copia


# Seletores

'''obter especie: animal -> str
obter especie(a) devolve a cadeia de caracteres correspondente  a especie do
animal.'''


def obter_especie(animal):
    return animal["s"]


'''obter freq reproducao: animal -> int
obter freq reproducao(a) devolve a frequencia de reproducao do animal a.'''


def obter_freq_reproducao(animal):
    return animal["r"][1]


'''obter freq alimentacao: animal -> int
obter freq alimentacao(a) devolve a frequencia de alimentacao do animal a
(as presas devolvem sempre 0).'''


def obter_freq_alimentacao(animal):
    return animal["a"][1]


'''obter idade: animal -> int
obter idade(a) devolve a idade do animal a.'''


def obter_idade(animal):
    return animal["r"][0]


'''obter fome: animal -> int
obter fome(a) devolve a fome do animal a (as presas devolvem sempre 0).'''


def obter_fome(animal):
    return animal["a"][0]


# Modificadores

'''aumenta idade: animal -> animal
aumenta idade(a) modifica destrutivamente o animal a incrementando o valor
da sua idade em uma unidade, e devolve o proprio animal.'''


def aumenta_idade(animal):
    animal["r"][0] += 1
    return animal


'''reset idade: animal -> animal
reset idade(a) modifica destrutivamente o animal a definindo o valor da sua
idade igual a 0, e devolve o proprio animal.'''


def reset_idade(animal):
    animal["r"][0] = 0
    return animal


'''aumenta fome: animal -> animal
aumenta fome(a) modifica destrutivamente o animal predador a incrementando
o valor da sua fome em uma unidade, e devolve o proprio animal. Esta
operacao nao modifica os animais presa.'''


def aumenta_fome(animal):
    animal["a"][0] += 1
    return animal


'''reset fome: animal -> animal
reset fome(a) modifica destrutivamente o animal predador a definindo o valor
da sua fome igual a 0, e devolve o proprio animal. Esta operacao nao modifica
os animais presa.'''


def reset_fome(animal):
    animal["a"][0] = 0
    return animal


# Reconhecedor


'''eh animal: universal -> booleano
eh animal(arg) devolve True caso o seu argumento seja um TAD animal e
False caso contrario.'''


def eh_animal(universal):
    chavetas = ["s", "r", "a"]
    if isinstance(universal, dict):
        for c in chavetas:
            if c not in universal.keys():
                return False
            elif c == "s" and (not (isinstance(universal["s"], str)) or len(universal["s"].strip()) <= 0):
                return False
            elif c == "r" and universal["r"][1] <= 0:
                return False
            elif c != "s" and (universal[c][1] < 0 or not (isinstance(universal[c][1], int))):
                return False

    else:
        return False

    return True


'''eh predador: universal -> booleano
eh predador(arg) devolve True caso o seu argumento seja um TAD animal do
tipo predador e False caso contrario.'''


def eh_predador(animal):
    if eh_animal(animal):
        return animal["a"][1] > 0
    else:
        return False


'''eh presa: universal -> booleano
eh presa(arg) devolve True caso o seu argumento seja um TAD animal do
tipo presa e False caso contrario.'''


def eh_presa(animal):
    if eh_animal(animal):
        return animal["a"][1] == 0
    else:
        return False


# Teste


'''animais iguais: animal × animal -> booleano
animais iguais(a1, a2) devolve True apenas se a1 e a2 sao animais e sao
iguais.'''


def animais_iguais(animal1, animal2):
    return animal1 == animal2


# Transformadores


'''animal para char: animal -> str
animal para char(a) devolve a cadeia de caracteres dum unico elemento correspondente
ao primeiro caracter da especie do animal passada por argumento,
em maiuscula para animais predadores e em minuscula para animais
presa.'''


def animal_para_char(animal):
    if eh_predador(animal):
        return animal["s"][0].upper()
    elif eh_presa(animal):
        return animal["s"][0].lower()


'''animal para str : animal -> str
animal para str(a) devolve a cadeia de caracteres que representa o animal'''


def animal_para_str(animal):
    if eh_predador(animal):
        return "{} [{}/{};{}/{}]".format(animal["s"], animal["r"][0], animal["r"][1], animal["a"][0], animal["a"][1])
    else:
        return "{} [{}/{}]".format(animal["s"], animal["r"][0], animal["r"][1])


# funcoes de alto nivel


'''eh animal fertil : animal -> booleano
eh animal fertil(a) devolve True caso o animal a tenha atingido a idade de reproducao e False caso contrario.'''


def eh_animal_fertil(animal):
    if animal["r"][0] >= animal["r"][1]:
        return True
    else:
        return False


'''eh animal faminto: animal -> booleano
eh animal faminto(a) devolve True caso o animal a tenha atingindo um valor de
fome igual ou superior a sua frequencia de alimentacao e False caso contrario. As
presas devolvem sempre False.'''


def eh_animal_faminto(animal):
    if eh_predador(animal):
        if animal["a"][0] >= animal["a"][1]:
            return True
    else:
        return False


'''reproduz animal: animal -> animal
reproduz animal(a) recebe um animal a devolvendo um novo animal da mesma
especie com idade e fome igual a 0, e modificando destrutivamente o animal passado
como argumento a alterando a sua idade para 0.'''


def reproduz_animal(animal):
    cria = cria_copia_animal(animal)
    cria = reset_fome(cria)
    cria = reset_idade(cria)
    animal = reset_idade(animal)
    return cria


# TAD Prado

# Construtor


'''cria prado: posicao × tuplo × tuplo × tuplo -> prado
cria prado(d, r, a, p) recebe uma posicao d correspondente a posicao que
ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
mais posicoes correspondentes aos rochedos que nao sao as montanhas dos
limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da
mesma dimens~ao do tuplo a com as posi c~oes correspondentes ocupadas pelos
animais; e devolve o prado que representa internamente o mapa e os animais
presentes. O construtor veri ca a validade dos seus argumentos, gerando um
8
ValueError com a mensagem 'cria prado: argumentos invalidos' caso
os seus argumentos nao sejam validos.'''


def cria_prado(d, r, a, p):
    flag_erro = False
    if eh_posicao(d):
        for rocha in r:
            if not (eh_posicao(rocha)):
                flag_erro = True

        for animal_prado in a:
            if not (eh_animal(animal_prado)):
                flag_erro = True

        for posicao_animal in p:
            if not (eh_posicao(posicao_animal)):
                flag_erro = True
    else:
        flag_erro = True

    if flag_erro:
        raise ValueError("cria_prado: argumentos invalidos")
    else:
        return {"d": d, "r": r, "a": a, "p": p}


'''cria copia prado: prado -> prado
cria copia prado(m) recebe um prado e devolve uma nova copia do prado.'''


def cria_copia_prado(prado):
    dict_prado_copia = {}
    for key, value in prado.items():
        if isinstance(value, tuple):
            list_valores_tupla = []
            for v in value:
                if isinstance(v, dict):
                    dict_novo = {}
                    for key, value in v.items():
                        dict_novo[key] = value
                    list_valores_tupla.append(dict_novo)
                else:
                    list_valores_tupla.append(v)
            dict_prado_copia[key] = tuple(list_valores_tupla)
        else:
            dict_prado_copia[key] = value
    return dict_prado_copia


# Seletores

'''obter tamanho x: prado -> int
obter tamanho x(m) devolve o valor inteiro que corresponde  a dimensao Nx do prado.'''


def obter_tamanho_x(prado):
    return prado["d"][0] + 1


'''obter tamanho y: prado -> int
obter tamanho y(m) devolve o valor inteiro que corresponde  a dimensao Ny
do prado.'''


def obter_tamanho_y(prado):
    return prado["d"][1] + 1


'''obter numero predadores: prado -> int
obter numero predadores(m) devolve o n mero de animais predadores no prado.'''


def obter_numero_predadores(prado):
    count_predadores = 0
    for animal in prado["a"]:
        if eh_predador(animal):
            count_predadores += 1
    return count_predadores


'''obter numero presas: prado -> int
obter numero presas(m) devolve o numero de animais presa no prado.'''


def obter_numero_presas(prado):
    count_presas = 0
    for animal in prado["a"]:
        if eh_presa(animal):
            count_presas += 1
    return count_presas


'''obter posicao animais: prado -> tuplo posicoes
obter posicao animais(m) devolve um tuplo contendo as posicoes do prado
ocupadas por animais, ordenadas em ordem de leitura do prado.'''


def obter_posicao_animais(prado):
    return prado["p"]


'''obter animal: prado × posicao -> animal
obter animal(m, p) devolve o animal do prado que se encontra na posicao p.'''


def obter_animal(prado, posicao):
    index_posicao = list(prado["p"]).index(posicao)
    return prado["a"][index_posicao]


# Modificadores


'''eliminar animal: prado × posicao -> prado
eliminar animal(m, p) modifica destrutivamente o prado m eliminando o animal
da posicao p deixando-a livre. Devolve o proprio prado.'''


def eliminar_animal(prado, posicao):
    temp_list_animais = list(prado["a"])
    temp_list_posicoes = list(prado["p"])

    index_posicao = temp_list_posicoes.index(posicao)

    del temp_list_animais[index_posicao]
    del temp_list_posicoes[index_posicao]

    prado["a"] = tuple(temp_list_animais)
    prado["p"] = tuple(temp_list_posicoes)

    return prado


'''mover animal: prado × posicao × posicao -> prado
mover animal(m, p1, p2) modifica destrutivamente o prado m movimentando
o animal da posicao p1 para a nova posicao p2, deixando livre a posicao onde
se encontrava. Devolve o proprio prado.'''


def mover_animal(prado, posicao_original, posicao_nova):
    temp_list_animais = list(prado["a"])
    temp_list_posicoes = list(prado["p"])

    index_posicao = temp_list_posicoes.index(posicao_original)

    del temp_list_posicoes[index_posicao]

    temp_list_posicoes.insert(index_posicao, posicao_nova)

    posicoes_novas = ordenar_posicoes(tuple(temp_list_posicoes))

    """
    lista_nova_animais = []
    for pn in posicoes_novas:
        animal_temp = obter_animal(prado, pn)
        lista_nova_animais.append(animal_temp)

    prado["p"] = posicoes_novas
    prado["a"] = tuple(lista_nova_animais)
    """

    prado["p"] = tuple(temp_list_posicoes)

    return prado


'''inserir animal: prado × animal × posicao -> prado
inserir animal(m, a, p) modifica destrutivamente o prado m acrescentando
na posicao p do prado o animal a passado com argumento. Devolve o proprio
prado.'''


def inserir_animal(prado, animal, posicao):
    temp_list_animais = list(prado["a"])
    temp_list_posicoes = list(prado["p"])

    temp_list_animais.append(animal)
    temp_list_posicoes.append(posicao)

    prado["a"] = tuple(temp_list_animais)
    prado["p"] = tuple(temp_list_posicoes)

    return prado


# Reconhecedores


'''eh prado: universal -> booleano
eh prado(arg) devolve True caso o seu argumento seja um TAD prado e False
caso contrario.'''


def eh_prado(universal):
    if isinstance(universal, dict):
        keys = ["d", "r", "a", "p"]
        for k in keys:
            if k not in universal.keys():
                return False
            else:
                if k == "d":
                    if not (eh_posicao(universal[k])):
                        return False
                elif k == "r":
                    if isinstance(universal[k], tuple):
                        for valor in universal[k]:
                            if not (eh_posicao(valor)):
                                return False
                    else:
                        return False
                elif k == "a":
                    if isinstance(universal[k], tuple):
                        for valor in universal[k]:
                            if not (eh_animal(valor)):
                                return False
                    else:
                        return False
                elif k == "p":
                    if isinstance(universal[k], tuple):
                        for valor in universal[k]:
                            if not (eh_posicao(valor)):
                                return False
                    else:
                        return False
    else:
        return False

    return True


'''eh posicao animal: prado × posicao -> booleano
eh posicao animal(m, p) devolve True apenas no caso da posicao p do prado
estar ocupada por um animal.'''


def eh_posicao_animal(prado, posicao):
    if eh_posicao(posicao):
        return posicao in prado["p"]
    else:
        return False


'''eh posicao obstaculo: prado × posicao -> booleano
eh posicao obstaculo(m, p) devolve True apenas no caso da posicao p do prado
corresponder a uma montanha ou rochedo.'''


def eh_posicao_obstaculo(prado, posicao):
    if eh_posicao(posicao):
        return posicao in prado["r"]
    else:
        return False


'''eh posicao livre: prado × posicao -> booleano
eh posicao livre(m, p) devolve True apenas no caso da posicao p do prado
corresponder a um espaco livre (sem animais, nem obstaculos).'''


def eh_posicao_livre(prado, posicao):
    return not (eh_posicao_animal(prado, posicao)) and not (eh_posicao_obstaculo(prado, posicao)) and (
                0 < posicao[0] < obter_tamanho_x(prado) - 1) and (0 < posicao[1] < obter_tamanho_y(prado) - 1)


# Teste


'''prados iguais: prado × prado -> booleano
prados iguais(p1, p2) devolve True apenas se p1 e p2 forem prados e forem
iguais.'''


def prados_iguais(prado1, prado2):
    return prado1 == prado2


# Transformador


'''prado para str : prado -> str
prado para str(m) devolve uma cadeia de caracteres que representa o prado
como mostrado nos exemplos.'''


def prado_para_str(prado):
    def _cria_prado_vazio(prado):
        lista_linhas = []
        top_bottom = "+" + "-" * (obter_tamanho_x(prado) - 2) + "+"
        lista_linhas.append(top_bottom)

        for rodada in range(obter_tamanho_y(prado) - 2):
            linha_temp = "|" + "." * (obter_tamanho_x(prado) - 2) + "|"
            lista_linhas.append(linha_temp)

        lista_linhas.append(top_bottom)

        return lista_linhas

    display_prado = _cria_prado_vazio(prado)
    for obstaculo in prado["r"]:
        display_prado[obstaculo[1]] = display_prado[obstaculo[1]][:obstaculo[0]] + "@" + display_prado[obstaculo[1]][
                                                                                         obstaculo[0] + 1:]

    for index, posicao in enumerate(prado["p"]):
        display_prado[posicao[1]] = display_prado[posicao[1]][:posicao[0]] + animal_para_char(prado["a"][index]) + \
                                    display_prado[posicao[1]][posicao[0] + 1:]

    return "\n".join(display_prado)


# Funções de alto nível


'''obter valor numerico: prado × posicao -> int
obter valor numerico(m, p) devolve o valor numerico da posicao p correspondente
 a ordem de leitura no prado m.'''


def obter_valor_numerico(prado, posicao1):
    return ((obter_tamanho_x(prado) - 1) * obter_pos_y(posicao1)) + obter_pos_x(posicao1) + obter_pos_y(posicao1)


'''obter movimento: prado × posicao -> posicao
obter movimento(m, p) devolve a posicao seguinte do animal na posicao p dentro
do prado m de acordo com as regras de movimento dos animais no prado.'''


def obter_movimento(prado, posicao_entrada):
    animal = obter_animal(prado, posicao_entrada)

    if eh_presa(animal):
        return _caminho_padrao(prado, posicao_entrada)

    else:
        posicao_final = _caminho_ataque(prado, posicao_entrada)
        if posicoes_iguais(posicao_final, posicao_entrada):
            return _caminho_padrao(prado, posicao_entrada)
        else:
            return posicao_final


'''Esta funcao define o movimento normal que cada animal terá de fazer'''


def _caminho_padrao(prado, posicao_entrada):
    possiveis_posicoes = obter_posicoes_adjacentes(posicao_entrada)
    possiveis_posicoes_disponiveis = list(filter(lambda x: eh_posicao_livre(prado, x), possiveis_posicoes))
    N = obter_valor_numerico(prado, posicao_entrada)

    if len(possiveis_posicoes_disponiveis) == 0:
        return posicao_entrada

    posicao_escolhida = possiveis_posicoes_disponiveis[N % len(possiveis_posicoes_disponiveis)]
    lista_N = list(range(len(possiveis_posicoes_disponiveis)))
    ordem_passeio = [N % len(possiveis_posicoes_disponiveis)]

    for num in lista_N:
        if num > N % len(possiveis_posicoes_disponiveis):
            ordem_passeio.append(num)

    for num in lista_N:
        if num < N % len(possiveis_posicoes_disponiveis):
            ordem_passeio.append(num)

    nova_pos = 0
    while not (eh_posicao_livre(prado, posicao_escolhida)):
        posicao_escolhida = possiveis_posicoes_disponiveis[ordem_passeio[nova_pos]]
        nova_pos += 1
        if nova_pos == len(possiveis_posicoes_disponiveis) + 1:
            posicao_escolhida = posicao_entrada
            break
    return posicao_escolhida


'''Esta funcao define o caminho que os predadores irao fazer para atacar uma presa'''


def _caminho_ataque(prado, posicao_entrada):
    possiveis_posicoes = obter_posicoes_adjacentes(posicao_entrada)
    possiveis_posicoes2 = []
    N = obter_valor_numerico(prado, posicao_entrada)

    for pp in possiveis_posicoes:
        try:
            animal_temp = obter_animal(prado, pp)
            possiveis_posicoes2.append(pp)
        except:
            pass

    if len(possiveis_posicoes2) == 0:
        return posicao_entrada

    posicao_escolhida = possiveis_posicoes2[N % len(possiveis_posicoes2)]
    lista_N = list(range(len(possiveis_posicoes2)))
    ordem_passeio = [N % len(possiveis_posicoes2)]

    for num in lista_N:
        if num > N % len(possiveis_posicoes2):
            ordem_passeio.append(num)

    for num in lista_N:
        if num < N % len(possiveis_posicoes2):
            ordem_passeio.append(num)

    nova_pos = 0

    while (animal_temp == "") or (not (eh_presa(animal_temp))):
        posicao_escolhida = possiveis_posicoes2[ordem_passeio[nova_pos]]
        nova_pos += 1
        if nova_pos == len(possiveis_posicoes2):
            posicao_escolhida = posicao_entrada
            break
        try:
            animal_temp = obter_animal(prado, posicao_escolhida)
        except:
            animal_temp = ""
    return posicao_escolhida


'''geracao(m) e a funcao auxiliar que modifica o prado m fornecido como argumento de
acordo com a evolucao correspondente a uma geracao completa, e devolve o proprio
prado.'''


def geracao(prado1):
    posicoes_ordenadas = ordenar_posicoes(prado1["p"])

    for posicao_original in posicoes_ordenadas:
        animal = obter_animal(prado1, posicao_original)
        posicao_nova = obter_movimento(prado1, posicao_original)

        if eh_predador(animal):
            animal = aumenta_fome(animal)
            if posicao_nova in obter_posicao_animais(prado1):
                animal = reset_fome(animal)
                prado1 = eliminar_animal(prado1, posicao_nova)

        animal = aumenta_idade(animal)

        prado1 = mover_animal(prado1, posicao_original, posicao_nova)

        if eh_animal_faminto(animal):
            prado1 = eliminar_animal(prado1, posicao_nova)

        if not (posicoes_iguais(posicao_original, posicao_nova)) and (eh_animal_fertil(animal)):
            cria = reproduz_animal(animal)
            prado1 = inserir_animal(prado1, cria, posicao_original)

    return prado1


'''Esta funcao abre e le o ficheiro, retornando o prado da configuracao do ficheiro'''


def inicia_ecosistema(f):
    ficheiro = open(f)

    linha = ficheiro.readline()
    while len(linha) <= 2:
        linha = ficheiro.readline()
        if len(linha) == 0:
            break

    x, y = linha.split(",")
    x = int(x[1:])
    y = int(y[:y.find(")")])
    dim = cria_posicao(x, y)

    linha = ficheiro.readline()
    while len(linha) <= 2:
        linha = ficheiro.readline()
        if len(linha) == 0:
            break

    list_obs = linha.split(",")
    obs = []
    while len(list_obs) > 0:
        x = int(list_obs[0].replace("(", ""))
        y = int(list_obs[1][:list_obs[1].find(")")])
        obs_temp = cria_posicao(x, y)
        del list_obs[0:2]
        obs.append(obs_temp)

    obs = tuple(obs)

    an = []
    pos = []

    for linha in ficheiro:
        if len(linha) > 2:
            info_animal = linha.split(",")
            especie_animal = info_animal[0]
            especie_animal = especie_animal.split("'")[1]
            r = int(info_animal[1])
            a = int(info_animal[2])
            x = info_animal[3]
            y = info_animal[4]
            x = int(x[2:])
            y = int(y[:y.find(")")])
            posicao_animal = cria_posicao(x, y)

            an.append(cria_animal(especie_animal, r, a))
            pos.append(posicao_animal)

    an = tuple(an)
    pos = tuple(pos)

    prado = cria_prado(dim, obs, an, pos)

    return prado


'''simula ecossitema(f, g, v)  e a funcao principal que permite simular o ecossistema de um
prado. A funcao recebe uma cadeia de caracteres f, um valor inteiro g e um valor booleano
v e devolve o tuplo de dois elementos correspondentes ao numero de predadores e
presas no prado no  m da simulacao. A cadeia de caracteres f passada por argumento
corresponde ao nome do  cheiro de configuracao da simulacao. O valor inteiro g corresponde
ao numero de geracoes a simular. O argumento booleano v ativa o modo verboso
(True) ou o modo quiet (False). No modo quiet mostra-se pela saida standard o prado,
o numero de animais e o numero de geracao no inicio da simulacao e apos a ultima
geracao. No modo verboso, apos cada geracao, mostra-se tambem o prado, o numero de
animais e o numero de geracao, apenas se o numero de animais predadores ou presas se
tiver alterado.'''


def simula_ecossistema(f, g, v):
    prado = inicia_ecosistema(f)

    qtd_predadores = len(list(filter(lambda x: eh_predador(x), prado["a"])))
    qtd_presas = len(list(filter(lambda x: eh_presa(x), prado["a"])))

    print("Predadores: {} vs Presas: {} (Gen. 0)".format(qtd_predadores, qtd_presas))
    print(prado_para_str(prado))

    qtd_predadores_anterior = qtd_predadores
    qtd_presas_anterior = qtd_presas

    if v:
        for ger in range(1, g):
            prado = geracao(prado)

            qtd_predadores_atual = len(list(filter(lambda x: eh_predador(x), prado["a"])))
            qtd_presas_atual = len(list(filter(lambda x: eh_presa(x), prado["a"])))

            if qtd_predadores_anterior != qtd_predadores_atual or qtd_presas_anterior != qtd_presas_atual:
                print("Predadores: {} vs Presas: {} (Gen. {})".format(qtd_predadores_atual, qtd_presas_atual, ger))

                qtd_predadores_anterior = qtd_predadores_atual
                qtd_presas_anterior = qtd_presas_atual
                print(prado_para_str(prado))

        return (qtd_predadores_atual, qtd_presas_atual)

    else:
        for ger in range(1, g):
            prado = geracao(prado)

        qtd_predadores = len(list(filter(lambda x: eh_predador(x), prado["a"])))
        qtd_presas = len(list(filter(lambda x: eh_presa(x), prado["a"])))

        print("Predadores: {} vs Presas: {} (Gen. {})".format(qtd_predadores, qtd_presas, g))
        print(prado_para_str(prado))

        return (qtd_predadores, qtd_presas)


