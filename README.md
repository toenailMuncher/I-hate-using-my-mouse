
# Mediapipe & OpenCV Multi-Tool Suite

## Overview
This project is a multi-functional software suite leveraging **Mediapipe** and **OpenCV** to implement advanced face, hand, and body tracking algorithms. The suite includes tools such as a virtual mouse, body language detector, and facial ID recognition system, offering a versatile platform for creative and practical applications.

---

## Features

### 1. **Virtual Mouse**
Control your computer cursor using hand gestures tracked via Mediapipe's hand-tracking algorithms. Features include:
- Gesture-based left click, right click, and drag.
- Smooth cursor movement mapped to hand positions.
- Configurable sensitivity and gesture mapping.

### 2. **Body Language Detector**
Analyze body posture and movements to detect:
- Common gestures such as crossing arms or leaning forward.
- Real-time posture corrections.
- Potential emotional states based on detected body language patterns.

### 3. **Facial ID Recognition**
A facial recognition system that can:
- Detect and identify faces using pre-trained models.
- Track and log faces over time for security or attendance systems.
- Integrate with a custom database for facial ID matching.

---

## Requirements

### Dependencies
Ensure you have the following installed:
- **Python 3.8+**
- **Mediapipe**
- **OpenCV**
- **NumPy**
- **dlib** (for facial landmarks, optional)
- **PyAutoGUI** (for virtual mouse functionality)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/mediapipe-opencv-tools.git
   ```
2. Navigate to the project directory:
   ```bash
   cd mediapipe-opencv-tools
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. **Virtual Mouse**
Run the virtual mouse script:
```bash
python virtual_mouse.py
```
Follow on-screen instructions to use gestures for cursor control.

### 2. **Body Language Detector**
Run the body language detection script:
```bash
python body_language_detector.py
```
Stand in front of the camera, and the tool will analyze your posture and gestures.

### 3. **Facial ID Recognition**
Run the facial ID recognition script:
```bash
python facial_id_recognition.py
```
Load a database of faces, and the software will detect and identify faces in real-time.

---

## Configuration

- Adjust parameters like camera resolution, tracking sensitivity, and gesture mappings in the respective configuration files (`config_virtual_mouse.json`, `config_body_language.json`, etc.).
- Integrate custom facial databases by adding images to the `faces/` directory and updating `faces_db.json`.

---

## Contributions

Contributions are welcome! If you have ideas for new tools or improvements, feel free to fork the repository and create a pull request. Please ensure your contributions align with the coding style and include documentation.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [Mediapipe](https://google.github.io/mediapipe/) for providing powerful tracking algorithms.
- [OpenCV](https://opencv.org/) for robust computer vision tools.
- The open-source community for their contributions and support.

---

## Future Work

- Add support for voice commands integrated with gesture controls.
- Implement multi-user tracking for collaborative applications.
- Develop a desktop app for easier access and configuration.

---

Start exploring the capabilities of face, hand, and body tracking with this versatile tool suite!
