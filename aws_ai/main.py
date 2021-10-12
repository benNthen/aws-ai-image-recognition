import image_helpers
import vehicle_detect

value = input("Please enter image path: ")

image_helpers.get_image_from_file(value)
vehicle_detect.detect_labels_local_file(value)
vehicle_detect.output_display(0)
