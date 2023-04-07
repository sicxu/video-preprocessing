import os


# TODO: change the template


template = [[
"- name: 0408_download_%02d\n"%i,
"  sku: G1\n",
"  priority: high\n",
"  preemptible: False\n",
"  command:\n",
"  - cd /mnt/blob\n",
"  - ./azcopy copy \"https://igsharestorage.blob.core.windows.net/sichengxu/codes/video-preprocessing/txt.tar?sv=2020-10-02&se=2023-04-21T10%3A57%3A40Z&sr=c&sp=rwl&sig=1uzs0Kwvm%2Bz%2B2I1gGL0ygcUHYp%2Fw%2B4ufZvIhSr5QzxY%3D\" /tmp/ --recursive\n",
"  - cd /tmp\n",
"  - tar xvf txt.tar\n",
"  - cd /mnt/blob/codes/video-preprocessing\n",
"  - python crop_vox.py --workers 10 --dataset_version 2 --format .mp4 --annotations_folder /tmp/txt --video_folder /tmp/youtube --chunk_folder /tmp/chunks --out_folder /tmp/crop --bbox_folder /tmp/bbox --video_folder_f /mnt/blob/datasets/vox/vox2/youtube --chunk_folder_f /mnt/blob/datasets/vox/vox2/chunks --out_folder_f /mnt/blob/datasets/vox/vox2/crop --bbox_folder_f /mnt/blob/datasets/vox/vox2/bbox --data_range %d-%d --chunks_metadata metadatas/vox2_%02d\n"%(i * 209, min((i + 1) * 209, 10000), i),
# "  - sleep infinity\n",
"  submit_args:\n",
"    env:\n",
"      {MKL_THREADING_LAYER: GNU}\n",
"    container_args:\n",
"      shm_size: 512g\n\n"
] for i in range(48)]

with open("submit.yaml", "a+") as fd:
    for setting in template:
        fd.writelines(setting)