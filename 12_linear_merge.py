"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""
from heapq import merge


def linear_merge_easy(list1, list2):
    new_list = []
    new_list = list(merge(list1, list2))
    return new_list


def linear_merge(list1, list2):
    new_list = []
    pos1, pos2 = 0, 0
    while True:
        if (pos1 <= len(list1) - 1) and (pos2 <= len(list2) - 1):
            if list1[pos1] < list2[pos2]:
                new_list.append(list1[pos1])
                pos1 += 1
            else:
                new_list.append(list2[pos2])
                pos2 += 1
        elif pos1 <= len(list1) - 1:
            new_list.append(list1[pos1])
            pos1 += 1
        elif pos2 <= len(list2) - 1:
            new_list.append(list2[pos2])
            pos2 += 1
        else:
            return new_list
    return new_list


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
