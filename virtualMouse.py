import cv2
import mediapipe as mp
import pyautogui
from tracker import HolisticTracker

class VirtualMouse:
    def __init__(self):
        # Initialize the HolisticTracker and get screen dimensions
        self.tracker = HolisticTracker()
        self.screen_width, self.screen_height = pyautogui.size()

    def process_frame_for_mouse(self, frame):
        # Process the frame to get landmarks and draw only right hand landmarks
        image, results = self.tracker.process_frame(frame)
        self.tracker.draw_right_hand_landmarks(image, results)
        return image, results

    def move_mouse_based_on_right_hand_landmarks(self, results, frame, frame_width, frame_height):
        # Control the mouse cursor based on right hand landmarks
        if results.right_hand_landmarks:
            landmarks = results.right_hand_landmarks.landmark
            index_finger_tip = landmarks[mp.solutions.holistic.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = landmarks[mp.solutions.holistic.HandLandmark.THUMB_TIP]

            index_x = int(index_finger_tip.x * frame_width)
            index_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            cv2.circle(img=frame, center=(index_x, index_y), radius=10, color=(0, 255, 255), thickness=-1)
            cv2.circle(img=frame, center=(thumb_x, thumb_y), radius=10, color=(0, 255, 255), thickness=-1)

            screen_index_x = self.screen_width / frame_width * index_x
            screen_index_y = self.screen_height / frame_height * index_y
            screen_thumb_y = self.screen_height / frame_height * thumb_y

            #click on current position
            if abs(screen_index_y - screen_thumb_y) < 20:
                pyautogui.click()
                pyautogui.sleep(1)
            #move the mouse
            elif abs(screen_index_y - screen_thumb_y) < 100:
                pyautogui.moveTo(screen_index_x, screen_index_y)
            #scroll up
            elif screen_index_y - screen_thumb_y > 100:
                pyautogui.scroll(10)
            
    def run_virtual_mouse(self):
        # Capture video from the webcam and process each frame
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)  # Flip the frame horizontally
            frame_height, frame_width, _ = frame.shape
            image, results = self.process_frame_for_mouse(frame)
            self.move_mouse_based_on_right_hand_landmarks(results, frame, frame_width, frame_height)
            cv2.imshow('Virtual Mouse', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an instance of VirtualMouse and run it
    virtual_mouse = VirtualMouse()
    virtual_mouse.run_virtual_mouse()