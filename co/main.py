import colmap
colmap = Colmap(colmap_path, working_dir, im_paths)
#colmap.sparse_reconstruction_unknown_calib()
colmap.sparse_reconstruction_known_calib(Ks, Ts, imdims)
colmap.dense_reconstruction()
