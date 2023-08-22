#E:\\cyc_wraped_images\\coco_dataset\\JSON2YOLO\\dataset\\train\\via_project_22Aug2023_11h36m_coco.json
#E:\\cyc_wraped_images\\coco_dataset\\JSON2YOLO\\dataset\\train\\yolo_annotations
import json
import os

# Load COCO JSON annotations
with open('E:\\cyc_wraped_images\\coco_dataset\\JSON2YOLO\\dataset\\train\\via_project_22Aug2023_11h36m_coco.json', 'r') as f:
    coco_data = json.load(f)

# Output folder for YOLO annotations
output_folder = 'E:\\cyc_wraped_images\\coco_dataset\\JSON2YOLO\\dataset\\train\\yolo_annotations'
os.makedirs(output_folder, exist_ok=True)

# Iterate through images
for image_info in coco_data['images']:
    image_id = image_info['id']
    image_width = image_info['width']
    image_height = image_info['height']
    image_file_name = image_info['file_name']

    # List to store YOLO annotations
    yolo_annotations = []

    # Iterate through annotations for the current image
    for annotation in coco_data['annotations']:
        if annotation['image_id'] == image_id:
            category_id = annotation['category_id']

            # Check if the category should be included in YOLO annotations
            if category_id in [1, 2, 3]:  # Modify based on your category IDs
                x, y, w, h = annotation['bbox']
                x_center = (x + w / 2) / image_width
                y_center = (y + h / 2) / image_height
                bbox_width = w / image_width
                bbox_height = h / image_height
                yolo_annotations.append(f"{category_id - 1} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")

    # Write YOLO annotations to a .txt file
    output_txt_path = os.path.join(output_folder, os.path.splitext(image_file_name)[0] + '.txt')
    with open(output_txt_path, 'w') as txt_file:
        for annotation_line in yolo_annotations:
            txt_file.write(annotation_line + '\n')

print("Annotations converted to YOLO format and saved as .txt files.")
