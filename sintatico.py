NAO_TERMINAL = {
    0: 'TIPO',
    1: 'PARAM',
    2: 'LISTA_PARAM',
    3: 'COMANDOS',
    4: 'COMANDO',
    5: 'ATRIBUICAO',
    6: 'PROGRAMA',
    7: 'EXPRESSAO',
    8: 'TERMO',
    9: 'FATOR',
    10: 'EXPRESSAO_BOOL',
    11: 'OPERADOR_REL',
    12: 'CORPO_PROGRAMA',
    13: 'COMANDO_FOR',
    14: 'COMANDO_WHILE',
    15: 'LEITURA',
    16: 'DECLARACAO_FUNC',
    17: 'CHAMADA_FUNC',
    18: 'COMANDO_IF',
    19: 'ESCRITA',
    20: 'LISTA_ARGS',
    21: 'ARGUMENTOS',
    22: "S'"
}

class SLR:
    def __init__(self):
        self.afd = {
            0: {'ACTION': {'program': 'S 2'}, 'GOTO': {22: {'$': 1}, 6: {'$': 1}}},
            1: {'ACTION': {'$': 'ACC'}, 'GOTO': {}},
            2: {'ACTION': {'id': 'S 3'}, 'GOTO': {}},
            3: {'ACTION': {'ap': 'S 4'}, 'GOTO': {}},
            4: {'ACTION': {'int': 'S 5', 'char': 'S 6', 'bool': 'S 7', 'fp': 'R 0 2'}, 'GOTO': {0: {'id': 8}, 1: {'v': 10, 'fp': 10, 'pv': 10}, 2: {'v': 13, 'fp': 15, 'ab': 15}}},
            5: {'ACTION': {'id': 'R 1 0'}, 'GOTO': {}},
            6: {'ACTION': {'id': 'R 1 0'}, 'GOTO': {}},
            7: {'ACTION': {'id': 'R 1 0'}, 'GOTO': {}},
            8: {'ACTION': {'id': 'S 9'}, 'GOTO': {}},
            9: {'ACTION': {'pv': 'R 2 1', 'fp': 'R 2 1', '=': 'R 2 1', 'v': 'R 2 1'}, 'GOTO': {}},
            10: {'ACTION': {'fp': 'R 1 2', 'v': 'R 1 2'}, 'GOTO': {}},
            11: {'ACTION': {'fp': 'R 3 2', 'v': 'R 3 2'}, 'GOTO': {}},
            12: {'ACTION': {'pv': 'S 37'}, 'GOTO': {}},
            13: {'ACTION': {'v': 'S 14'}, 'GOTO': {}},
            14: {'ACTION': {'int': 'S 17', 'char': 'S 6', 'bool': 'S 7', 'id': 'S 24'}, 'GOTO': {0: {'id': 8}, 2: {'v': 11, 'pv': 11}, 8: {'menos': 20}, 9: {}}},
            15: {'ACTION': {'fp': 'S 16'}, 'GOTO': {}},
            16: {'ACTION': {'ab': 'S 17'}, 'GOTO': {}},
            17: {'ACTION': {'id': 'S 18', 'int': 'S 5', 'char': 'S 6', 'bool': 'S 7', 'ap': 'S 21', 'func': 'S 69', 'if': 'S 41', 'while': 'S 54', 'for': 'S 53', 'read': 'S 65', 'write': 'S 81', 'ab': 'S 17'}, 'GOTO': {0: {'id': 8}, 1: {'v': 12, 'fp': 12, 'pv': 12, '=': 18}, 3: {'fb': 32, 'int': 34, 'char': 34, 'bool': 34, 'id': 34, 'func': 34, 'if': 34, 'while': 34, 'for': 34, 'read': 34, 'write': 34, 'ab': 34}, 4: {'id': 36, 'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'ab': 36}, 5: {'pv': 39}, 7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            18: {'ACTION': {'=': 'S 19', 'pv': 'R 1 5'}, 'GOTO': {}},
            19: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}, 20: {'fp': 31}, 21: {'fp': 31}}},
            20: {'ACTION': {'fp': 'R 1 9', 'pv': 'R 1 9', 'mais': 'R 1 9', 'menos': 'R 1 9', 'multiplicacao': 'R 1 9', 'divisao': 'R 1 9', '=': 'S 19', '==': 'S 48', '!=': 'S 48', '<': 'S 48', '<=': 'S 48', '>': 'S 48', '>=': 'S 48'}, 'GOTO': {}},
            21: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 22, 'pv': 22}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}, 20: {'fp': 22}, 21: {'fp': 22}}},
            22: {'ACTION': {'fp': 'S 23'}, 'GOTO': {}},
            23: {'ACTION': {'fp': 'R 3 9', 'pv': 'R 3 9', 'mais': 'R 3 9', 'menos': 'R 3 9', 'multiplicacao': 'R 3 9', 'divisao': 'R 3 9'}, 'GOTO': {}},
            24: {'ACTION': {'fp': 'R 1 8', 'pv': 'R 1 8', 'mais': 'R 1 8', 'menos': 'R 1 8', 'multiplicacao': 'S 45', 'divisao': 'S 46'}, 'GOTO': {}},
            25: {'ACTION': {'mais': 'S 26', 'menos': 'S 26'}, 'GOTO': {}},
            26: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 27, 'pv': 27}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}}},
            27: {'ACTION': {'fp': 'R 3 7', 'pv': 'R 3 7', 'mais': 'R 3 7', 'menos': 'R 3 7'}, 'GOTO': {}},
            28: {'ACTION': {'fp': 'R 1 7', 'pv': 'R 1 7', 'mais': 'R 1 7', 'menos': 'R 1 7'}, 'GOTO': {}},
            29: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {8: {'mais': 28, 'menos': 29, 'fp': 31, 'pv': 31}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}}},
            30: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {9: {'mais': 31, 'menos': 31, 'fp': 31, 'pv': 31}}},
            31: {'ACTION': {'fp': 'R 3 8', 'pv': 'R 3 8', 'mais': 'R 3 8', 'menos': 'R 3 8', 'multiplicacao': 'R 3 8', 'divisao': 'R 3 8'}, 'GOTO': {}},
            32: {'ACTION': {'fb': 'S 33', 'if': 'S 41', 'else': 'S 51'}, 'GOTO': {3: {'fb': 32}}},
            33: {'ACTION': {'$': 'ACC', 'fb': 'R 0 3'}, 'GOTO': {3: {'fb': 32}, 12: {'$': 1}}},
            34: {'ACTION': {'id': 'S 18', 'int': 'S 5', 'char': 'S 6', 'bool': 'S 7'}, 'GOTO': {0: {'id': 35}, 2: {'v': 11, 'pv': 11}}},
            35: {'ACTION': {'id': 'R 2 3', 'int': 'R 2 3', 'char': 'R 2 3', 'bool': 'R 2 3', 'fb': 'R 2 3'}, 'GOTO': {}},
            36: {'ACTION': {'id': 'R 1 3', 'int': 'R 1 3', 'char': 'R 1 3', 'bool': 'R 1 3', 'fb': 'R 1 3'}, 'GOTO': {}},
            37: {'ACTION': {'id': 'R 2 4', 'int': 'R 2 4', 'char': 'R 2 4', 'bool': 'R 2 4', 'fb': 'R 2 4'}, 'GOTO': {}},
            38: {'ACTION': {'pv': 'R 3 5', 'fp': 'R 3 10'}, 'GOTO': {}},
            39: {'ACTION': {'pv': 'S 39', 'if': 'S 41', 'while': 'S 54', 'for': 'S 53', 'read': 'S 65', 'write': 'S 81', 'func': 'S 69', 'id': 'S 70', 'fb': 'R 0 3'}, 'GOTO': {3: {'fb': 32}, 4: {'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'id': 36}, 5: {'pv': 39}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            40: {'ACTION': {'id': 'R 2 4', 'int': 'R 2 4', 'char': 'R 2 4', 'bool': 'R 2 4', 'fb': 'R 2 4'}, 'GOTO': {}},
            41: {'ACTION': {'ap': 'S 42'}, 'GOTO': {10: {'fp': 62}}},
            42: {'ACTION': {'id': 'S 20', 'num': 'S 77', 'ap': 'S 21', '!': 'S 49'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}, 10: {'fp': 62}, 11: {'fp': 50, 'pv': 50}}},
            43: {'ACTION': {'else': 'S 51', 'fb': 'S 85'}, 'GOTO': {}},
            44: {'ACTION': {'pv': 'S 43'}, 'GOTO': {}},
            45: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {8: {'mais': 28, 'menos': 29, 'fp': 31, 'pv': 31}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}}},
            46: {'ACTION': {'id': 'S 20', 'ap': 'S 21', 'num': 'S 77'}, 'GOTO': {8: {'mais': 28, 'menos': 29, 'fp': 31, 'pv': 31}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}}},
            47: {'ACTION': {'multiplicacao': 'R 3 8', 'divisao': 'R 3 8', 'fp': 'R 3 8', 'pv': 'R 3 8'}, 'GOTO': {}},
            48: {'ACTION': {'id': 'S 20', 'num': 'S 77', 'ap': 'S 21'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}, 10: {'fp': 50}}},
            49: {'ACTION': {'ap': 'S 21', 'id': 'S 20', 'num': 'S 77'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}, 10: {'fp': 50, 'pv': 50}}},
            50: {'ACTION': {'fp': 'R 3 10', 'pv': 'R 3 10'}, 'GOTO': {}},
            51: {'ACTION': {'ab': 'S 17'}, 'GOTO': {3: {'fb': 52}, 4: {'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'id': 36}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            52: {'ACTION': {'fb': 'R 7 18'}, 'GOTO': {}},
            53: {'ACTION': {'ap': 'S 55'}, 'GOTO': {}},
            54: {'ACTION': {'ap': 'S 42'}, 'GOTO': {10: {'fp': 62}}},
            55: {'ACTION': {'int': 'S 5', 'char': 'S 6', 'bool': 'S 7', 'id': 'S 18'}, 'GOTO': {0: {'id': 8}, 5: {'pv': 56}}},
            56: {'ACTION': {'pv': 'S 57'}, 'GOTO': {10: {'pv': 58}}},
            57: {'ACTION': {'id': 'S 18'}, 'GOTO': {5: {'fp': 59}}},
            58: {'ACTION': {'fp': 'S 60'}, 'GOTO': {}},
            59: {'ACTION': {'ab': 'S 17'}, 'GOTO': {3: {'fb': 61}, 4: {'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'id': 36}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            60: {'ACTION': {'ab': 'S 17'}, 'GOTO': {3: {'fb': 61}, 4: {'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'id': 36}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            61: {'ACTION': {'fb': 'R 5 13'}, 'GOTO': {}},
            62: {'ACTION': {'fp': 'S 63'}, 'GOTO': {}},
            63: {'ACTION': {'ab': 'S 17'}, 'GOTO': {3: {'fb': 64}, 4: {'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'id': 36}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            64: {'ACTION': {'fb': 'R 5 14'}, 'GOTO': {}},
            65: {'ACTION': {'ap': 'S 66'}, 'GOTO': {}},
            66: {'ACTION': {'id': 'S 67'}, 'GOTO': {}},
            67: {'ACTION': {'fp': 'S 68'}, 'GOTO': {}},
            68: {'ACTION': {'pv': 'R 4 15'}, 'GOTO': {}},
            69: {'ACTION': {'int': 'S 5', 'char': 'S 6', 'bool': 'S 7'}, 'GOTO': {0: {'id': 71}}},
            71: {'ACTION': {'id': 'S 72'}, 'GOTO': {}},
            72: {'ACTION': {'ap': 'S 4'}, 'GOTO': {2: {'fp': 73}}},
            73: {'ACTION': {'fp': 'S 74'}, 'GOTO': {}},
            74: {'ACTION': {'ab': 'S 17'}, 'GOTO': {3: {'fb': 75}, 4: {'fb': 36, 'int': 36, 'char': 36, 'bool': 36, 'func': 36, 'if': 36, 'while': 36, 'for': 36, 'read': 36, 'write': 36, 'id': 36}, 13: {'fb': 61}, 14: {'fb': 64}, 15: {'pv': 68}, 16: {'fb': 75}, 18: {'fb': 43}, 19: {'pv': 83}}},
            75: {'ACTION': {'fb': 'R 6 16'}, 'GOTO': {}},
            70: {'ACTION': {'ap': 'S 76', 'pv': 'R 1 5'}, 'GOTO': {}},
            76: {'ACTION': {'id': 'S 20', 'num': 'S 77', 'fp': 'R 0 20'}, 'GOTO': {7: {'v': 78, 'fp': 79}, 20: {'fp': 79}, 21: {'fp': 79, 'v': 78}}},
            77: {'ACTION': {'fp': 'R 1 9', 'pv': 'R 1 9', 'mais': 'R 1 9', 'menos': 'R 1 9', 'multiplicacao': 'R 1 9', 'divisao': 'R 1 9', 'v': 'R 1 9'}, 'GOTO': {}},
            78: {'ACTION': {'v': 'R 2 21', 'fp': 'R 2 21'}, 'GOTO': {}},
            79: {'ACTION': {'fp': 'S 80'}, 'GOTO': {}},
            80: {'ACTION': {'pv': 'R 3 17', 'v': 'R 3 17'}, 'GOTO': {}},
            81: {'ACTION': {'ap': 'S 82'}, 'GOTO': {}},
            82: {'ACTION': {'id': 'S 20', 'num': 'S 77', 'ap': 'S 21'}, 'GOTO': {7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}}},
            83: {'ACTION': {'fp': 'S 84'}, 'GOTO': {}},
            84: {'ACTION': {'pv': 'R 4 19'}, 'GOTO': {}}
        }

        self.afd[24]['ACTION'].update({'==': 'S 48', '!=': 'S 48', '<': 'S 48', '<=': 'S 48', '>': 'S 48', '>=': 'S 48'})
        self.afd[41]['ACTION'].update({'==': 'S 48', '!=': 'S 48', '<': 'S 48', '<=': 'S 48', '>': 'S 48', '>=': 'S 48'})
        self.afd[48]['GOTO'].update({7: {'mais': 25, 'menos': 25, 'fp': 38, 'pv': 38}, 8: {'mais': 28, 'menos': 29, 'fp': 28, 'pv': 28}, 9: {'mais': 24, 'menos': 24, 'fp': 24, 'pv': 24}})

        self.afd[20]['ACTION'].update({'multiplicacao': 'R 1 9', 'divisao': 'R 1 9'})
        self.afd[23]['ACTION'].update({'multiplicacao': 'R 3 9', 'divisao': 'R 3 9'})
        self.afd[31]['ACTION'].update({'multiplicacao': 'R 3 8', 'divisao': 'R 3 8'})

    def parser(self, entrada):
        pilha = [0]
        print("\nPilha: " + ' '.join(map(str, pilha)))
        i = 0
        while i < len(entrada):
            estado_atual = pilha[-1]
            token = entrada[i]
            if token not in self.afd.get(estado_atual, {}).get('ACTION', {}):
                print(f"Erro: Nenhuma acao para o token '{token}' no estado {estado_atual}")
                return False
            movimento = self.afd[estado_atual]['ACTION'][token]
            print(f" | Acao: {movimento}")
            acao = movimento.split(' ')
            if acao[0] == 'S':
                pilha.append(int(acao[1]))
                i += 1
            elif acao[0] == 'R':
                for j in range(int(acao[1])):
                    pilha.pop()
                print(f' | Reduziu para {NAO_TERMINAL[int(acao[2])]}')
                estado_atual = pilha[-1]
                nt = int(acao[2])
                if nt not in self.afd.get(estado_atual, {}).get('GOTO', {}):
                    print(f"Erro: Nenhuma transiçao GOTO para o nao-terminal {nt} no estado {estado_atual}")
                    return False
                prox = '$' if i >= len(entrada) else entrada[i]
                if prox not in self.afd[estado_atual]['GOTO'][nt]:
                    print(f"Erro: Nenhuma transicao GOTO para o prox '{prox}' no estado {estado_atual}, nao-terminal {nt}")
                    return False
                desvio = self.afd[estado_atual]['GOTO'][nt][prox]
                pilha.append(int(desvio))
            elif acao[0] == 'ACC':
                print('Aceito')
                return True
            else:
                print(f"Erro: Açao invalida {acao[0]}")
                return False
            print("\nPilha: " + ' '.join(map(str, pilha)))
        print('Erro')
        return False

if __name__ == "__main__":
    sintatico = SLR()
    # ok
    entrada = ["program", "id", "ap", "fp", "ab", "int", "id", "pv", "fb", "$"]
    entrada_while = ["program", "id", "ap", "fp", "ab",
            "while", "ap", "id", "==", "num", "fp", "ab",
            "id", "=", "num", "pv",
            "fb",
            "fb", "$"]
    entrada_if = ["program", "id", "ap", "fp", "ab",
            "if", "ap", "id", "!=", "num", "fp", "ab",
            "id", "=", "num", "pv",
            "fb", "fb", "fb", "fb",
            "fb", "$"]
    
    #erro
    entrada_erro = ["program", "ap", "fp", "ab", "fb", "$"]
    sintatico .parser(entrada_if)