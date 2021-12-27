from .. import tk_interface as intf


def canvas_save_setting(frame_id, entry_total_frames, entry_height, btn_canvas_save, default_entry=50,
                        default_height=200):
    f = intf.widget_model
    frame = 'frame_canvas_saves'
    rw = (2,), (1,)
    cw = (1,), (1,)
    fmd_button_entry = [
        f(frame_id, frame, 'frame', 0, 0, 0, 0, 'nsew', **intf.frame_options(rw, cw)),

        f(frame, 'lbl_total_frames', 'label', 0, 0, 0, 0, 'nsew', **{'text': 'Total Frames'}),
        f(frame, entry_total_frames, 'entry', 0, 0, 1, 1, 'nsew', **{'default_value': default_entry, }),

        f(frame, 'lbl_height', 'label', 1, 1, 0, 0, 'nsew', **{'text': 'Height'}),
        f(frame, entry_height, 'entry', 1, 1, 1, 1, 'nsew', **{'default_value': default_height, }),

        f(frame, btn_canvas_save, 'button', 2, 2, 0, 2, 'nsew', **{'text': 'Save'}),
    ]
    return fmd_button_entry
