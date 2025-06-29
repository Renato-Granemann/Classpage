def criar_secao_tabela():
    string = ''
    for i in range(int(input("Quantas anotações precisa? "))) :
        string += f'''
        <tr> 
            <td>{input(f"Insira a matéria da {i+1}° prova >>> ")}</td>
            <td>{input(f"Insira a data (Ex.: 03/05) da {i+1}° prova >>> ")}</td>
            <td>{input(f"Insira o conteúdo da {i+1}° prova >>> ")}</td>
            <td>{input(f'Insira o método de avaliação da {i+1}° prova >>> ')}</td>
        </tr>
        '''
    return string


print(criar_secao_tabela())