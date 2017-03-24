import numpy as np
import cv2
import sys
import dlib
from skimage import io
import tensorflow as tf

imagePath = '/home/iot/Downloads/images.jpeg'
modelFullPath = '/home/iot/Desktop/FaceDetection/DataSet/Emotions/output_graph.pb'
labelsFullPath = '/home/iot/Desktop/FaceDetection/DataSet/Emotions/output_labels.txt'

# You can download the required pre-trained face detection model here:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)

f = open(labelsFullPath, 'rb')
lines = f.readlines()

def create_graph():
    """Creates a graph from saved GraphDef file and returns a saver."""
    # Creates graph from saved graph_def.pb.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image(image_data):
    answer = None

    
    

    with tf.Session() as sess:

        image_data = cv2.resize(image_data,dsize=(299,299), interpolation = cv2.INTER_CUBIC)
        image_data = np.asarray(image_data)
        image_data = cv2.normalize(image_data.astype('float'),None,-0.5,0.5,cv2.NORM_MINMAX)
            
        image_data = np.expand_dims(image_data,axis=0)
                

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'Mul:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-1:][::-1]  # Getting top 5 predictions

        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        return answer

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    # Creates graph from saved GraphDef.
    create_graph()

    while(True):
        # Capture frame-by-frame
        ret, image = cap.read()

        # Run the HOG face detector on the image data
        detected_faces = face_detector(image, 1)

        print("Found {} faces in the image file ".format(len(detected_faces)))

        # Loop through each face we found in the image
        for i, face_rect in enumerate(detected_faces):

            Face = image[(face_rect.top() - 20):(face_rect.bottom() + 20),(face_rect.left() - 20):(face_rect.right() + 20)]#Crop Face outoff Image
            cv2.imshow('frame',Face)
            




            run_inference_on_image(Face)

            
            # Detected faces are returned as an object with the coordinates
            # of the top, left, right and bottom edges
            #print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(),face_rect.right(), face_rect.bottom()))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
