# Estudos-Python

Uma coleção de pequenos projetos e exercícios que fiz enquanto estava aprendendo Python. Nada de produção aqui - só códigos simples para praticar conceitos básicos da linguagem.

## O que você vai encontrar aqui

- **Exemplos/** - Scripts pequenos e independentes que fiz para praticar coisas como:
  - Manipulação de strings e arquivos
  - Uso de bibliotecas externas (requests, matplotlib, etc)
  - Algoritmos simples (jogo de adivinhação, gerador de senhas)
  - Integração com APIs (conversor de moedas)
  - Automação básica (WhatsApp bot - use com extrema cautela!)

- **Segurança da Informação/** - Alguns scripts bem simples de teste de rede (apenas ping, nada sofisticado)

- **Sistema de envio de mensagem em massa/** - Um exemplo de como automatizar o WhatsApp usando pywhatkit. **ATENÇÃOBSERVAÇÃO IMPORTANTE:** Este é apenas para fins educacionais. Usar para spam pode te causar problemas sérios.

## Como usar

Cada script é independente e pode ser executado diretamente:

```bash
python caminho/para/o/script.py
```

Alguns podem precisar de bibliotecas extras. Se você vir um `ModuleNotFoundError`, basta instalar:

```bash
pip install nome-da-biblioteca
```

Bibliotecas comuns que aparecem aqui:
- `requests` - para fazer requisições HTTP
- `matplotlib` - para fazer gráficos simples
- `pywhatkit`, `pyautogui`, `pandas` - para o WhatsApp bot
- `PyPDF2` - para ler PDFs

## Uma observação importante sobre o "LimparArquivosTemp.py"

Esse script **apaga arquivos do seu computador**. Ele foi escrito como exercício de automação, mas **nunca** execute ele em uma máquina de produção ou com dados importantes. Ele tem comentários de aviso no código - por favor, leia-os antes de pensar em rodar algo assim.

## Sobre o código

Você vai notar que alguns scripts são bem simples (quase ingênuos) - isso é proposital. Eles representam meu processo de aprendizado em diferentes momentos. Alguns têm:
- Funções bem definidas com `main()`
- Outros são scripts diretos (quando fazia mais sentido assim)
- Comentários explicativos em alguns lugares
- Pouca ou nenhuma tratamento de erro em muitos casos (mais um indicativo de que eram exercícios)

Se você está aprendendo Python, sinta-se à vontade para copiar, modificar, quebrar e consertar esses códigos. É assim que se aprende mesmo.

## Licença

Não há licença formal aqui. Considere tudo como domínio público para fins educacionais.