<p align="center">
<a href="https://dio.me/"><img src="https://img.shields.io/badge/DIO-Project-FED564?logo=vimeo" alt="DIO - Project"></a>
<a href="https://en.wikipedia.org/wiki/Artificial_intelligence"><img src="https://img.shields.io/badge/AI-Project-FED564?logo=openai" alt="AI - Project"></a>
<a href="https://www.gnu.org/software/bash/" title="Vá para a página inicial do Bash"><img src="https://img.shields.io/badge/Prompt-Project-FED564?logo=gnu-bash&amp;logoColor=white" alt="Feito com Bash"></a>
 <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Code-Project-FED564?logo=Python " alt="Python - Project"></a>
 
# Detecção de Celebridades em Imagens com AWS Rekognition

Este projeto explora a detecção de rostos de celebridades em imagens utilizando a API do AWS Rekognition. Embora o projeto tenha sido planejado para ser executado na nuvem, a implementação foi realizada localmente devido à falta de acesso a uma conta da AWS.

## Descrição do Projeto

O objetivo deste projeto é demonstrar como o AWS Rekognition pode ser utilizado para identificar celebridades em imagens. O sistema foi projetado para carregar uma imagem de entrada e, em seguida, utilizar a API do Rekognition para detectar e reconhecer rostos de celebridades presentes na imagem.

### Funcionalidades

- **Reconhecimento Facial**: O sistema foi desenvolvido para identificar rostos de celebridades em uma imagem fornecida.
- **Resultados de Confiança**: Para cada celebridade reconhecida, o sistema retornaria um nível de confiança que indicaria a precisão da identificação.

## Estrutura do Projeto
```
face_recognition/
├── celebridades/               
│   ├── gigi_hadid.jpeg
│   └── kaia_gerber.jpeg
│   ├── miranda_kerr.jpeg
├── test1.jpeg 
├── test2.jpeg
├── test3.jpeg
└── reconhecimento_celebridades.py 
```

## Considerações

- **Execução Local**: O projeto foi implementado localmente utilizando bibliotecas como `face_recognition` e `OpenCV` para simular a funcionalidade do AWS Rekognition. Isso permitiu a realização de testes e validações sem a necessidade de uma conta na AWS.
- **Dependências**: O projeto requer as seguintes bibliotecas:
  - `face_recognition`
  - `opencv-python`

  As bibliotecas podem ser instaladas via pip.

## Resultados Esperados

Ao executar o código, espera-se que o sistema retorne os nomes das celebridades reconhecidas na imagem de teste, juntamente com os níveis de confiança. Um exemplo de saída pode ser:

### Resultado 1

<img width="752" alt="kaia" src="https://github.com/user-attachments/assets/b4dfa6eb-a8d3-437a-a85a-d16de256fe2d" />

### Resultado 2

<img width="612" alt="miranda" src="https://github.com/user-attachments/assets/e4cecf2e-6508-47ba-84e0-0f17ea079b53" />

### Resultado 3

<img width="720" alt="gigi" src="https://github.com/user-attachments/assets/63ab724f-a1e7-4b11-b8d6-d754cdb85ad6" />

## Conclusão

Este projeto ilustra a aplicação do reconhecimento facial para identificar celebridades em imagens. Embora a implementação tenha sido realizada localmente, a estrutura e a lógica do projeto estão preparadas para uma futura integração com o AWS Rekognition, caso o acesso à conta da AWS seja obtido.

## Licença

Este projeto é de uso pessoal e educacional. Consulte as políticas da AWS para mais informações sobre o uso do Rekognition.
