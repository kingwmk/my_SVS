
from . import colmap

colmap_path = "/home/hadoop-pnc/wangmingkun/software/colmap/bin/colmap"
working_dir = "/home/hadoop-pnc/wangmingkun/datasets/MVS/theOldGate"
im_paths = "/home/hadoop-pnc/wangmingkun/datasets/MVS/theOldGate/images"
colmap = Colmap(colmap_path, working_dir, im_paths)
colmap.sparse_reconstruction_unknown_calib()
#colmap.sparse_reconstruction_known_calib(Ks, Ts, imdims)
colmap.dense_reconstruction()
