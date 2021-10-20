import cv2

print(cv2.__version__)

source_video = "sources/mario.mp4"
cap = cv2.VideoCapture(source_video)

if __name__ == "__main__":

    img_mario = cv2.imread("sources/captura.png")  # import img
    # ret,first_frame = cap.read() ... não precisa mais do print pois ira pegar o primeiro frame do video,
    # mas só é possivel pois o objeto a ser selecionado está no primeiro frame
    
    box = cv2.selectROI("select roi",img_mario,fromCenter=False,showCrosshair=False)  # o próprio select ja tem o imshow
    print(box)  # (365, 268, 133, 207) -> (Altura,Largura,X,Y) ... Localização do Roi selecionado na img

    tracker = cv2.TrackerCSRT_create()  # Criando o Tracking
    tracker.init(img_mario,box)  # Inicializando o tracking

    while cap.isOpened():
        ret,frame = cap.read()

        if not ret:
            break

        ok,box = tracker.update(frame)  # Sempre que passar um novo frame para o tracker ele vai procurar 

        if ok:
            pt1 = (box[0],box[1])  # Passando a altura e largura do box
            pt2 = (box[0]+box[2],box[1]+box[3])  # Onde começa e termina o retângulo ... (altura+x,largura+y)
            cv2.rectangle(frame,pt1,pt2,(255,0,0),2,1)
        else:
            print("ERROR")

        cv2.imshow("Tracking",frame)

        if cv2.waitKey(1) == 27:
            break

        cv2.destroyAllWindows()