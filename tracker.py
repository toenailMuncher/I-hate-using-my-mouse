import mediapipe as mp
import cv2

class HolisticTracker:
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.mp_face_mesh = mp.solutions.face_mesh
        self.cap = cv2.VideoCapture(0)

    def process_frame(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.holistic.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        return image, results

    def draw_landmarks(self, image, results):
        if results.face_landmarks:
            self.mp_drawing.draw_landmarks(image, results.face_landmarks, self.mp_face_mesh.FACEMESH_TESSELATION)
        if results.right_hand_landmarks:
            self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
        if results.left_hand_landmarks:
            self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS)
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS)

    def run(self):
        with self.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as self.holistic:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break
                image, results = self.process_frame(frame)
                self.draw_landmarks(image, results)
                cv2.imshow('Raw Webcam Feed', image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tracker = HolisticTracker()
    tracker.run()