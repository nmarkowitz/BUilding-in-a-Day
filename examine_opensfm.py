import numpy as np
import cv2
import os.path as op
import glob

dataset = "marsh_chapel_step_by_step"
pdir = "/Users/noahmarkowitz/Documents/Boston_University/Courses/2024_Spring/ImageProcessing_CAS-CS585/term_project"
dataset_dir = op.join(pdir, "datasets", dataset)

#region look at features
features_dir = op.join(dataset_dir, "features")
features_files = glob.glob(op.join(features_dir, "*.npz"))
features_files = sorted(features_files)

f = features_files[0]
features_npz = np.load(f)

# files: points, descriptors, colors, segmentations, instances, segmentation_labels, OPENSFM_FEATURES_VERSION

points = features_npz["points"]
descriptors = features_npz["descriptors"]


#endregion
matches_dir = op.join(dataset_dir, "matches")
matches_files = glob.glob(op.join(matches_dir, "*.pkl.gz"))
matches_files = sorted(matches_files)
f1 = matches_files[0]

import gzip
import pickle


f1 = "/Users/noahmarkowitz/Documents/Boston_University/Courses/2024_Spring/ImageProcessing_CAS-CS585/term_project/datasets/marsh_chapel_step_by_step/matches/img01.JPG_matches.pkl"
with open(f1, "rb") as f:
    matches = pickle.load(f)


import cv2
import matplotlib.pyplot as plt

def plot_points_on_image(image_path, points):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    # Convert image from BGR to RGB
    image_rgb = image# cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the color and size of the cross
    color = (0, 255, 0)  # Green
    size = 10
    thickness = 2

    # Draw crosses on the image
    for (x, y) in points:
        cv2.drawMarker(image_rgb, (x, y), color=color, markerType=cv2.MARKER_CROSS, markerSize=size, thickness=thickness)

    # Window name in which image is displayed
    window_name = 'image'

    # Using cv2.imshow() method
    # Displaying the image
    cv2.imshow(window_name, image_rgb)

    # waits for user to press any key
    # (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

    # closing all open windows
    cv2.destroyAllWindows()


    # # Plot the image with points
    # plt.figure(figsize=(8, 6))
    # plt.imshow(image_rgb)
    # plt.axis('off')  # Hide axis
    # plt.show()

# Example usage
points_of_interest = [(50, 50), (200, 200), (300, 150)]  # List of (x, y) tuples
img_path = "/Users/noahmarkowitz/Documents/Boston_University/Courses/2024_Spring/ImageProcessing_CAS-CS585/term_project/datasets/marsh_chapel_step_by_step/images/img02.JPG"
points_of_interest = matches["img02.JPG"].tolist()
plot_points_on_image(img_path, points_of_interest)

