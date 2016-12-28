import cPickle as pickle

from video_popup.utils import util

expr = 'two-men'

if(expr == 'two-men'):

    seg_file = '../../data/Two-men/images/broxmalik_size4/broxmalikResults' \
               '/f1t30/v5_d4/vw10_nn10_k5_thresh10000_max_occ10_op0_cw2.5/init200/mdl20_pw10_oc10_engine0_it5/results.pkl'

    with open(seg_file, 'r') as f:
        seg = pickle.load(f)

    W = seg['W']
    Z = seg['Z']
    labels = seg['labels_objects']
    images = seg['images']

    # plot the segmentation result
    # util.plot_nbor(seg['W'], seg['Z'], seg['s'], seg['images'], labels=seg['labels'],
    #                show_overlap=1, show_broken=1, plot_text=1, assignment=seg['assignment'])
    util.plot_traj2(seg['W'], seg['Z'], images, labels=labels, save_fig=0, frame_time = 0.1)