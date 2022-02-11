from math import log2

def abrir_arquivo(arquivo):
    dados = open(arquivo, 'r')
    linha = dados.readline().split()
    informacoes = [linha[0], linha[1]] #Numero de linhas, tamanho de cada linha da memória cache em bytes
    acessos = []
    linhas_enderecos = dados.readline().strip('\n')
    while linhas_enderecos != '':
        acessos.append(linhas_enderecos)
        linhas_enderecos = dados.readline().strip('\n')
    dados.close()
    return informacoes, acessos

def verificar_memoria_cache(memoria_cache, acessos):
    for i in acessos:
        if i not in memoria_cache:
            print('MISS')
            verificar_capacidade(memoria_cache, informacoes_iniciais, entrada[1])
            memoria_cache.append(i)
        else:
            print('HIT')
    return None

def verificar_capacidade(memoria_cache, informacoes_iniciais, substituicao):
    informacoes_iniciais = list(map(int, informacoes_iniciais))
    numero_linhas, tamanho_linhas = informacoes_iniciais[0], informacoes_iniciais[1]
    numero_linhas = log2(numero_linhas) #Pegar os bits do número de linhas usando log
    tamanho_linhas = log2(tamanho_linhas) #Pegar os bits do tamanho das linhas usando log
    if (len(memoria_cache)+1) * 32  < (numero_linhas * tamanho_linhas):
        return None
    if (len(memoria_cache) + 1) * 32  > (numero_linhas * tamanho_linhas):
        if substituicao == 'FIFO':
            memoria_cache.pop(0)
            return memoria_cache
        elif substituicao == 'LRU':
            verificar_menos_acessado(memoria_cache)
            memoria_cache.pop(0)
            return memoria_cache
        elif substituicao == 'DIR':
            endereco = verificar_posicao_predefinida(memoria_cache)
            if endereco != None:
                memoria_cache.pop(endereco)
                return memoria_cache


def verificar_posicao_predefinida(memoria_cache):
    dados = open('entrada.txt', 'r')
    linha = dados.readline().split()
    informacoes = [linha[0], linha[1]]
    endereco_memoria = []
    linhas_enderecos = dados.readline().strip('\n')
    while linhas_enderecos != '':
        endereco_memoria.append(linhas_enderecos)    
        memoria_cache_bin = []
        for i in endereco_memoria:
            i_hexa = int(i, 16)
            endereco_bin = bin(i_hexa)
            for j in memoria_cache:
                j_hexa = int(j, 16)
                j_bin = bin(j_hexa)
                memoria_cache_bin.append(j_bin)
            for k in memoria_cache_bin:
                if endereco_bin[-1:-4] in k[-1:-4]:
                    dados.close()
                    index = memoria_cache_bin.index(k)
                    return index
                else:
                    return None
        linhas_enderecos = dados.readline().strip('\n')
    dados.close()
    return None

def verificar_menos_acessado(memoria_cache):
    dados = open('entrada.txt', 'r')
    endereco_memoria = []
    linhas_enderecoes = dados.readline().strip('\n')
    while linhas_enderecoes != '':
        endereco_memoria.append(linhas_enderecoes)
        for i in endereco_memoria:
            if i in memoria_cache:
                memoria_cache.remove(i) 
                memoria_cache.append(i) #O menos acessado sempre será o primeiro da lista
        linhas_enderecoes = dados.readline().strip('\n')
    dados.close()
    return memoria_cache


entrada = input().split() #entrada.txt LRU
memoria_cache = []
informacoes_iniciais, acessos = abrir_arquivo(entrada[0])
verificar_memoria_cache(memoria_cache, acessos)
