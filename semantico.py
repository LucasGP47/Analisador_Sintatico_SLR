from typing import List, Dict, Any, Optional

NAO_TERMINAL = {
    0: 'TIPO', 1: 'PARAM', 2: 'LISTA_PARAM', 3: 'COMANDOS', 4: 'COMANDO', 5: 'ATRIBUICAO',
    6: 'PROGRAMA', 7: 'EXPRESSAO', 8: 'TERMO', 9: 'FATOR', 10: 'EXPRESSAO_BOOL',
    11: 'OPERADOR_REL', 12: 'CORPO_PROGRAMA', 13: 'COMANDO_FOR', 14: 'COMANDO_WHILE',
    15: 'LEITURA', 16: 'DECLARACAO_FUNC', 17: 'CHAMADA_FUNC', 18: 'COMANDO_IF',
    19: 'ESCRITA', 20: 'LISTA_ARGS', 21: 'ARGUMENTOS', 22: "S'"
}

class Semantico:
    def __init__(self):
        self.tabela_simbolos: Dict[str, Dict[str, Any]] = {}
        self.escopo_atual: str = "global"
        self.escopos: List[str] = ["global"]
        self.erros: List[str] = []
        self.tipos_compativeis: Dict[str, List[str]] = {
            'int': ['int'], 'char': ['char'], 'bool': ['bool'], 'float': ['float', 'int']
        }
        self.retorno_func: Optional[str] = None
        self.em_funcao: bool = False

    # ===== aux =====
    def _get_linha(self, elemento: Any) -> int:
        if hasattr(elemento, 'linha'):
            return elemento.linha
        elif isinstance(elemento, dict) and 'linha' in elemento:
            return elemento['linha']
        return 0

    def _get_type(self, elemento: Any) -> Optional[str]:
        if isinstance(elemento, dict) and 'type' in elemento:
            return elemento['type']
        elif hasattr(elemento, 'lexema') and hasattr(elemento, 'tipo'):
            if elemento.tipo in ['int', 'char', 'bool']:
                return elemento.lexema
        return None

    def _get_lexema(self, elemento: Any) -> Optional[str]:
        if hasattr(elemento, 'lexema'):
            return elemento.lexema
        elif isinstance(elemento, dict) and 'id' in elemento:
            return elemento['id']
        return None

    # ===== escopo =====
    def entrar_escopo(self, nome_escopo: str = None):
        nome_escopo = nome_escopo or f"bloco_{len(self.escopos)}"
        self.escopos.append(nome_escopo)
        self.escopo_atual = nome_escopo
        self.tabela_simbolos.setdefault(nome_escopo, {})

    def sair_escopo(self):
        if len(self.escopos) > 1:
            self.escopos.pop()
            self.escopo_atual = self.escopos[-1]

    # ===== vars =====
    def declarar_variavel(self, id: str, tipo: str, linha: int):
        escopo = self.tabela_simbolos[self.escopo_atual]
        if id in escopo:
            self.erros.append(f"erro semantico: variavel '{id}' ja declarada no escopo '{self.escopo_atual}' na linha {linha}")
        else:
            escopo[id] = {'tipo': tipo, 'declarado': True}

    def verificar_declaracao(self, id: str, linha: int) -> Optional[str]:
        for escopo in reversed(self.escopos):
            if id in self.tabela_simbolos.get(escopo, {}):
                return self.tabela_simbolos[escopo][id]['tipo']
        self.erros.append(f"erro semantico: variavel '{id}' nao declarada na linha {linha}")
        return None

    # ===== tipos =====
    def verificar_tipo(self, tipo_esq: str, tipo_dir: str, operacao: str, linha: int) -> Optional[str]:
        if tipo_dir not in self.tipos_compativeis.get(tipo_esq, []):
            self.erros.append(f"erro semantico: tipos incompativeis '{tipo_esq}' e '{tipo_dir}' na operacao '{operacao}' na linha {linha}")
            return None
        
        if tipo_esq == 'float' and tipo_dir == 'int':
            return 'float'
        if operacao in ['==', '!=', '<', '<=', '>', '>=']:
            return 'bool'
        return tipo_esq

    def verificar_expressao(self, expr_tipo: str, esperado: str, linha: int):
        if expr_tipo != esperado:
            self.erros.append(f"erro semantico: Tipo de expressao '{expr_tipo}' nao compativel com esperado '{esperado}' na linha {linha}")

    # ===== funcoes =====
    def declarar_funcao(self, id: str, tipo_retorno: str, params: List[Dict[str, str]], linha: int):
        escopo_global = self.tabela_simbolos.setdefault("global", {})
        if id in escopo_global:
            self.erros.append(f"erro semantico: funcao '{id}' ja declarada na linha {linha}")
        else:
            escopo_global[id] = {
                'tipo': 'funcao',
                'retorno': tipo_retorno,
                'params': params,
                'declarado': True
            }
        
        self.entrar_escopo(id)
        self.em_funcao = True
        self.retorno_func = tipo_retorno
        
        for param in params:
            self.declarar_variavel(param['id'], param['tipo'], linha)

    def verificar_chamada_funcao(self, id: str, args: List[str], linha: int) -> Optional[str]:
        func = self.tabela_simbolos.get("global", {}).get(id)
        if not func or func['tipo'] != 'funcao':
            self.erros.append(f"erro semantico: funcao '{id}' nao declarada na linha {linha}")
            return None
        
        if len(args) != len(func['params']):
            self.erros.append(f"erro semantico: numero de argumentos incorreto para funcao '{id}' na linha {linha}")
            return None
        
        for i, (arg_tipo, param) in enumerate(zip(args, func['params'])):
            self.verificar_tipo(param['tipo'], arg_tipo, f"argumento {i+1}", linha)
        
        return func['retorno']

    def verificar_retorno(self, tipo_ret: str, linha: int):
        if not self.em_funcao:
            self.erros.append(f"erro semantico: retorno fora de funcao na linha {linha}")
        elif tipo_ret != self.retorno_func:
            self.erros.append(f"erro semantico: tipo de retorno '{tipo_ret}' incompativel com esperado '{self.retorno_func}' na linha {linha}")

    def finalizar_funcao(self):
        self.sair_escopo()
        self.em_funcao = False
        self.retorno_func = None

    # ===== principal =====
    def perform_action(self, nt_index: int, rhs: List[Any]) -> Dict[str, Any]:
        nt = NAO_TERMINAL[nt_index]
        linha = self._get_linha(rhs[0]) if rhs else 0
        lhs = {'linha': linha}

        try:
            if nt == 'TIPO':
                lhs['type'] = rhs[0].lexema

            elif nt == 'PARAM':
                tipo = self._get_type(rhs[0]) or rhs[0].lexema
                id_lexema = self._get_lexema(rhs[1])
                if id_lexema:
                    self.declarar_variavel(id_lexema, tipo, self._get_linha(rhs[1]))
                lhs.update({'type': tipo, 'id': id_lexema})

            elif nt == 'LISTA_PARAM':
                lhs['params'] = []
                if len(rhs) == 1:
                    lhs['params'] = [rhs[0]]
                elif len(rhs) == 3:
                    lhs['params'] = rhs[0]['params'] + [rhs[2]]

            elif nt == 'ATRIBUICAO':
                id_lexema = self._get_lexema(rhs[0])
                tipo_id = self.verificar_declaracao(id_lexema, self._get_linha(rhs[0])) if id_lexema else None
                tipo_expr = self._get_type(rhs[2])
                if tipo_id and tipo_expr:
                    self.verificar_tipo(tipo_id, tipo_expr, '=', self._get_linha(rhs[1]))
                lhs['type'] = tipo_id

            elif nt in ['EXPRESSAO', 'TERMO']:
                if len(rhs) == 1:
                    lhs['type'] = self._get_type(rhs[0])
                elif len(rhs) == 3:
                    tipo_esq = self._get_type(rhs[0])
                    tipo_dir = self._get_type(rhs[2])
                    if tipo_esq and tipo_dir:
                        lhs['type'] = self.verificar_tipo(tipo_esq, tipo_dir, rhs[1].tipo, self._get_linha(rhs[1]))

            elif nt == 'FATOR':
                if len(rhs) == 1:
                    if rhs[0].tipo == 'id':
                        lhs['type'] = self.verificar_declaracao(rhs[0].lexema, self._get_linha(rhs[0]))
                    elif rhs[0].tipo == 'num':
                        lhs['type'] = 'bool' if rhs[0].lexema.lower() in ['true', 'false'] else 'int'
                elif len(rhs) == 3:
                    lhs['type'] = self._get_type(rhs[1])

            elif nt == 'EXPRESSAO_BOOL':
                if len(rhs) == 3 and rhs[1].tipo in ['==', '!=', '<', '<=', '>', '>=']:
                    tipo_esq = self._get_type(rhs[0])
                    tipo_dir = self._get_type(rhs[2])
                    if tipo_esq and tipo_dir:
                        self.verificar_tipo(tipo_esq, tipo_dir, rhs[1].tipo, self._get_linha(rhs[1]))
                    lhs['type'] = 'bool'
                elif len(rhs) == 2:  # operador '!'
                    if self._get_type(rhs[1]) != 'bool':
                        self.erros.append(f"erro semantico: operador '!' espera bool na linha {self._get_linha(rhs[0])}")
                    lhs['type'] = 'bool'

            elif nt == 'OPERADOR_REL':
                lhs['op'] = rhs[0].tipo

            elif nt in ['COMANDO_IF', 'COMANDO_WHILE']:
                tipo_expr = self._get_type(rhs[2])
                if tipo_expr:
                    self.verificar_expressao(tipo_expr, 'bool', self._get_linha(rhs[0]))

            elif nt == 'COMANDO_FOR':
                tipo_expr = self._get_type(rhs[4])
                if tipo_expr:
                    self.verificar_expressao(tipo_expr, 'bool', self._get_linha(rhs[0]))

            elif nt == 'LEITURA':
                id_lexema = self._get_lexema(rhs[2])
                if id_lexema:
                    self.verificar_declaracao(id_lexema, self._get_linha(rhs[2]))

            elif nt == 'DECLARACAO_FUNC':
                tipo_ret = self._get_type(rhs[1]) or rhs[1].lexema
                id_lexema = self._get_lexema(rhs[2])
                params = rhs[4].get('params', [])
                if id_lexema:
                    self.declarar_funcao(id_lexema, tipo_ret, params, self._get_linha(rhs[2]))

            elif nt == 'CHAMADA_FUNC':
                id_lexema = self._get_lexema(rhs[0])
                args = rhs[2].get('args', []) if len(rhs) > 2 else []
                if id_lexema:
                    lhs['type'] = self.verificar_chamada_funcao(id_lexema, args, self._get_linha(rhs[0]))

            elif nt == 'LISTA_ARGS':
                lhs['args'] = rhs[0].get('args', []) if rhs else []

            elif nt == 'ARGUMENTOS':
                if len(rhs) == 1:
                    lhs['args'] = [self._get_type(rhs[0])]
                elif len(rhs) == 3:
                    lhs['args'] = rhs[0]['args'] + [self._get_type(rhs[2])]

            elif nt == 'PROGRAMA':
                id_lexema = self._get_lexema(rhs[1])
                params = rhs[3].get('params', [])
                if id_lexema:
                    self.declarar_funcao(id_lexema, 'void', params, self._get_linha(rhs[1]))

            elif nt == 'CORPO_PROGRAMA':
                self.sair_escopo()
                lhs = rhs[1] if len(rhs) > 1 else lhs

        except Exception as e:
            self.erros.append(f"erro durante acao semantica para {nt}: {str(e)}")

        return lhs

    def get_erros(self) -> List[str]:
        return self.erros