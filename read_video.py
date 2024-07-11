import cv2
import os

video_path = "/Users/noahmarkowitz/Documents/Boston_University/Courses/2024_Spring/ImageProcessing_CAS-CS585/term_project/datasets/Noah_vid/IMG_8587.MOV"
output_folder = "/Users/noahmarkowitz/Documents/Boston_University/Courses/2024_Spring/ImageProcessing_CAS-CS585/term_project/datasets/Noah_vid/images"
group_text_fname = "/Users/noahmarkowitz/Documents/Boston_University/Courses/2024_Spring/ImageProcessing_CAS-CS585/term_project/datasets/Noah_vid/image_groups.txt"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Count number of frames
# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    # return 0

# Get the total number of frames in the video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))



#------------------------------------------
# Read in the images as save as jpgs

frame_count = 0

group_num = 0
group_limit = 20

image_groups_text = ""
n_images = 0

while True:

    # Read video frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        break

    if frame_count % 20 == 0:

        if n_images % group_limit == 0:
            group_num += 1

        # Save frame as JPEG file
        img_name = f"frame_{frame_count:04d}.jpg"
        frame_path = os.path.join(output_folder, img_name)
        cv2.imwrite(frame_path, frame)
        print(f"Saved {img_name}")
        n_images += 1



        image_groups_text += img_name + f" Group{group_num:04d}" + "\n"


    frame_count += 1

# Release the video capture object
cap.release()

with open(group_text_fname,"w") as f:
    f.write(image_groups_text)

#return frame_count