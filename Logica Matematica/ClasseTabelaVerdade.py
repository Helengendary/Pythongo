class TabelaVerdade:
    def atribuicao_valores_tabela(self):

        tabela = [
            [True, True],   
            [True, False],
            [False, True], 
            [False, False] 
        ]
        
        print("p\tq\t~p\t~q\tp->q\tp^q\tpvq\tp<->q")
        for linha in tabela:
            p = "V" if linha[0] else "F"
            q = "V" if linha[1] else "F"
            negadop = "F" if linha[0] else "V"
            negadoq = "F" if linha[1] else "V"
            seentao = "F" if linha[0] and not linha[1] else "V"
            eind = "F" if linha[0] and linha[1] else "V"
            ouu = "V" if linha[0] or linha[1] else "F"
            somente = "V" if linha[0] == linha[1] else "F"
            print(f"{p}\t{q}\t{negadop}\t{negadoq}\t {seentao}\t {eind}\t {ouu}\t  {somente}")
            
            
class Principal:
    def main(self):
        tabela_verdade = TabelaVerdade()
        tabela_verdade.atribuicao_valores_tabela()

if __name__ == "__main__":
    principal = Principal()
    principal.main()