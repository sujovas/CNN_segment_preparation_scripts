import splitfolders

input_folder = "D:\\photo\\_DIPLOMKA\\Segmentation\\data\\data\\"
splitfolders.ratio(input_folder, output="D:\\photo\\_DIPLOMKA\\Segmentation\\data\\data_split\\", seed=1337,
                   ratio=(0.8, 0.1, 0.1), group_prefix=None, move=False)
