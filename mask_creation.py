from cgi import test
import cv2
import face_recognition
import xml.etree.ElementTree as ET
import numpy as np



cap = cv2.VideoCapture("Video.mp4")
face_locations = []

M = []
face_locations = []
# Compteur pour stocker une frame sur cent
i = 0
#Extraction du fichier txt
def extract_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Supprimer les espaces blancs en début et fin de ligne
            if line.isdigit():  # Vérifier si la ligne contient uniquement des chiffres
                numbers.append(int(line))
    return numbers

liste_text = [] 
liste_text = extract_numbers_from_file("Videoiframe.txt") 


while True:
    # Grab a single frame of video
    ret, frame = cap.read()

    if not ret:
        break

    # Convertion de l'image BGR color en RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Detectioon des visages
    face_locations = face_recognition.face_locations(rgb_frame)
    # Create a matrix to store the rectangles for the current frame  # ATTTTENTION AVENT np.zeros_like(frame[:, :, 0])
    current_frame_matrix = np.zeros((frame.shape[0], frame.shape[1], 1))

    if i in liste_text:


        # Initialisation de la matrice pour la frame courante
        matrix = np.zeros((frame.shape[0], frame.shape[1], 1))

        for (top, right, bottom, left) in face_locations:
            # Tracer de rectangle pour le visage
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Rempli la matrice de 1 pour le visage detecte
            current_frame_matrix[top:bottom, left:right] = 1

         
       

        # Ajout de la matrice de la frame courante dans la matrice M
        print(np.shape(current_frame_matrix))
        M.append(current_frame_matrix)
        print(i)
          
    
    # Incrémentation du compteur
    i += 1



    
    # Affichage de l'image
    cv2.imshow("Binaire", np.where(current_frame_matrix > 0, 255, 0).astype('uint8'))



    # Wait for Enter key to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
cap.release()

# Enregistrement de la matrice M dans un fichier numpy
M=np.reshape(M,(np.shape(M)[0],np.shape(M)[1],np.shape(M)[2],1))
np.save("M.npy", M[:,:,8:712,:])

