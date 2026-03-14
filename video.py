import cv2
import glob

images = sorted(glob.glob("paint_*.png"))

frame = cv2.imread(images[0])
h, w, _ = frame.shape

video = cv2.VideoWriter(
    "spray_simulation.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    30,
    (w, h)
)

for img in images:
    video.write(cv2.imread(img))

video.release()

print("Video created")