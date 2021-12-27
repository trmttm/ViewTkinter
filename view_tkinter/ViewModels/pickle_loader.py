from .. import tk_interface as intf


def pickle_loader(frame_id, tree_id='tree_id', pickle_canvas='canvas', button_width=None) -> list:
    f = intf.widget_model
    pw_id = 'paned_window'
    fr1 = 'frame_vertical_split_1'
    fr2 = 'frame_vertical_split_2'
    fr_btn = 'frame_load_buttons'
    paned_window_options = intf.paned_window_options(False, (fr1, fr2))
    rows_weights = ((0,), (1,))
    cols_weights = ((1, 2,), (1, 1))
    view_model = [
        f(frame_id, pw_id, 'paned_window', 0, 0, 0, 0, 'nsew', **paned_window_options),
        f(fr1, tree_id, 'treeview', 0, 0, 0, 0, 'nsew', ),
        f(fr1, fr_btn, 'frame', 1, 1, 0, 0, 'nsew', **intf.frame_options(rows_weights, cols_weights)),
        f(fr_btn, 'button_delete_template', 'button', 1, 1, 0, 0, 'nsew', **{'text': '❌', 'width': button_width}),
        f(fr_btn, 'button_load_pickle', 'button', 1, 1, 1, 1, 'nsew', **{'text': 'Load', 'width': button_width}),
        f(fr_btn, 'button_merge_pickle', 'button', 1, 1, 2, 2, 'nsew', **{'text': 'Merge', 'width': button_width}),
        f(fr2, pickle_canvas, 'canvas', 0, 0, 0, 0, 'nsew', bg='light yellow'),
    ]
    return view_model
