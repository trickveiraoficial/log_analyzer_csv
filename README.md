# Analisador de Logs do Process Monitor

Esta ferramenta analisa arquivos CSV exportados do Process Monitor, identificando erros específicos como `ACCESS DENIED`, `FILE NOT FOUND` e `BUFFER OVERFLOW`. Além disso, ela fornece feedbacks úteis para cada erro, auxiliando na resolução de problemas relacionados à execução de jogos ou outros aplicativos no Windows 11. O resultado é uma análise detalhada e visualmente agradável dos logs.

## Requisitos

- **Python 3.x**
- **Bibliotecas Python:**
  - [pandas](https://pandas.pydata.org/)
  - [colorama](https://pypi.org/project/colorama/)

## Instalação

1. **Clone ou baixe o repositório.**
2. **Instale as dependências utilizando o pip:**

   ```bash
   pip install pandas colorama
   ```

## Uso

Para executar o script, abra o terminal e forneça o caminho do arquivo CSV:

```bash
python log_analyzer.py caminho/para/seu/log.csv
```

A ferramenta exibirá os erros encontrados, os feedbacks correspondentes e um resumo da análise.

## Personalização

- **Lista de Erros:**  
  Edite a variável `ERROR_LIST` no script para incluir ou remover os erros que deseja monitorar.
  
- **Feedbacks:**  
  Modifique o dicionário `FEEDBACK_DICT` para ajustar as mensagens de feedback exibidas para cada erro.

## Exemplo de Saída

A saída da ferramenta é formatada para facilitar a leitura, com cores e alinhamento para destacar informações importantes:

```
===== Análise Iniciada =====
Valores em 'Result': ['SUCCESS', 'ACCESS DENIED', 'FILE NOT FOUND']
Procurando por: ['ACCESS DENIED', 'FILE NOT FOUND', 'BUFFER OVERFLOW']
===== Erros Encontrados =====
Linha | Tipo de Erro   | Feedback
-------------------------------------------
Linha 2   | ACCESS DENIED  | Verifique permissões.
Linha 5   | FILE NOT FOUND | Confirme o caminho.
===== Resumo =====
Total de erros: 2
===== Análise Concluída =====
```

## Solução de Problemas

- **Apenas um erro é exibido:**  
  Verifique se os outros erros estão presentes no arquivo CSV e se a normalização da coluna `Result` está funcionando corretamente.
  
- **Erros não encontrados:**  
  Confirme se a coluna `Result` existe no CSV e se ela contém os erros esperados.
  
- **Problemas de codificação:**  
  Se o CSV foi gerado por outro sistema, tente especificar a codificação ao carregar o arquivo, por exemplo:

  ```python
  df = pd.read_csv(file_path, encoding='utf-8')
  ```

## Considerações Finais

Esta ferramenta foi projetada para ser simples de usar e adaptar, proporcionando uma análise eficiente e visualmente atraente dos logs do Process Monitor.  
