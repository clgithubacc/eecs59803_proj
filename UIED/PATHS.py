from pathlib import Path
import os.path
source_path = Path(__file__).resolve()
source_dir = source_path.parent
CNN_PATH = os.path.join(source_dir, "models/cnn-rico-1.h5")
EAST_PATH = os.path.join(source_dir, "models/east_icdar2015_resnet_v1_50_rbox")
print()