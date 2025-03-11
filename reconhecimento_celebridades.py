import face_recognition
import cv2
import numpy as np
import os

def carregar_celebridades(diretorio):
    
    celebridades = {}
    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            caminho = os.path.join(diretorio, arquivo)
            imagem = face_recognition.load_image_file(caminho)
            encodings = face_recognition.face_encodings(imagem)
            if encodings:
                
                celebridades[os.path.splitext(arquivo)[0]] = encodings[0]
            else:
                print(f"Não foi encontrado rosto na imagem {arquivo}")
    return celebridades

def reconhecer_celebridades(imagem_teste_path, base_celebridades, tolerancia=0.6):
    
    imagem_teste = face_recognition.load_image_file(imagem_teste_path)
    face_localizacoes = face_recognition.face_locations(imagem_teste)
    face_encodings = face_recognition.face_encodings(imagem_teste, face_localizacoes)

    imagem_teste_cv2 = cv2.cvtColor(imagem_teste, cv2.COLOR_RGB2BGR)

    for (top, right, bottom, left), face_encoding in zip(face_localizacoes, face_encodings):
        resultados = []
        for nome, encoding_conhecida in celebridades.items():
            
            distancia = np.linalg.norm(face_encoding - encoding_conhecida)
            resultados.append((nome, distancia))

        
        nome_reconhecido = "Desconhecido"
        confianca = None
        if resultados:
            
            resultados.sort(key=lambda x: x[1])
            melhor_match, distancia_match = resultados[0]
            if distancia_match <= tolerancia:
                nome_reconhecido = melhor_match
                
                confianca = (1 - distancia_match) * 100 

        # Desenha um retângulo e o nome na imagem para visualização
        cv2.rectangle(imagem_teste_cv2, (left, top), (right, bottom), (0, 255, 0), 2)
        texto = nome_reconhecido
        if confianca is not None:
            texto += f" ({confianca:.2f}%)"
        cv2.putText(imagem_teste_cv2, texto, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print(f"Rosto detectado: {nome_reconhecido} - Distância: {distancia_match:.4f}" if confianca is not None else f"Rosto detectado: {nome_reconhecido}")

    
    cv2.imshow("Reconhecimento de Celebridades", imagem_teste_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    
    diretorio_celebridades = 'celebridades'
    # Imagem de teste
    imagem_teste_path = 'test2.jpeg'

   
    celebridades = carregar_celebridades(diretorio_celebridades)
    print("Base de celebridades:")
    for nome in celebridades:
        print(f" - {nome}")

    reconhecer_celebridades(imagem_teste_path, celebridades)

