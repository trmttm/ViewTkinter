import interface_tk as intf


def input_entry(frame_ie='frame_input_entry',
                label_title='label_title',
                check_btn='check_btn',
                canvas_slider='canvas_slider',
                canvas_graph='canvas_graph',
                entry='entry',
                button_apply='button_apply',
                button_ok='button_ok',
                entry_min='entry_ie_min',
                entry_max='entry_ie_max',
                entry_uom='entry_ie_uom',
                entry_digit='entry_ie_digit',
                cmb_box='combo_box',
                btn_r='button_ie_right',
                btn_l='button_ie_left',
                pad_xy=(0, 0),
                cb_values=()) -> list:
    f = intf.widget_model

    r_2 = ((2,), (1,))
    r_0 = ((0,), (1,))
    c_0 = ((0,), (1,))
    c_1 = ((1,), (1,))
    c_2 = ((2,), (1,))
    fr = 'frame_local'
    fr_name_uom = 'frame_ie_name_uom'
    fr_control = 'frame_ie_control'
    fr_canvas = 'frame_two_canvases'
    fr_btn = 'frame_ie_buttons'
    label_min = 'label_ie_min'
    label_max = 'label_ie_max'
    label_digit = 'label_ie_digit'
    view_model = [
        f(frame_ie, fr, 'frame', 0, 0, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_2, c_0)),
        f(fr, fr_name_uom, 'frame', 0, 0, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_0, c_0)),
        f(fr_name_uom, label_title, 'label', 0, 0, 0, 0, 'nsew', pad_xy, **{'text': 'Input Entry: Revenue'}),
        f(fr_name_uom, 'label_uom', 'label', 0, 0, 1, 1, 'nsew', pad_xy, **{'text': 'Unit of Measure'}),
        f(fr_name_uom, entry_uom, 'entry', 0, 0, 2, 2, 'nsew', pad_xy, ),

        f(fr, fr_control, 'frame', 1, 1, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_2, c_2)),
        f(fr_control, check_btn, 'check_button', 0, 0, 0, 0, 'nsew', pad_xy, text='by slider'),
        f(fr_control, btn_l, 'button', 0, 0, 1, 1, 'nsew', pad_xy, **{'text': '◀', 'width': 0}),
        f(fr_control, cmb_box, 'combo_box', 0, 0, 2, 2, 'nsew', pad_xy, text='by slider', values=cb_values),
        f(fr_control, btn_r, 'button', 0, 0, 3, 3, 'nsew', pad_xy, **{'text': '▶', 'width': 0}),
        f(fr_control, label_min, 'label', 0, 0, 4, 4, 'nsew', pad_xy, text='min'),
        f(fr_control, entry_min, 'entry', 0, 0, 5, 5, 'nsew', pad_xy, width=5),
        f(fr_control, label_max, 'label', 0, 0, 6, 6, 'nsew', pad_xy, text='max'),
        f(fr_control, entry_max, 'entry', 0, 0, 7, 7, 'nsew', pad_xy, width=5),
        f(fr_control, label_digit, 'label', 0, 0, 8, 8, 'nsew', pad_xy, text='digit'),
        f(fr_control, entry_digit, 'entry', 0, 0, 9, 9, 'nsew', pad_xy, width=5),

        f(fr, fr_canvas, 'frame', 2, 2, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_0, c_1)),
        f(fr_canvas, canvas_slider, 'canvas', 0, 0, 0, 0, 'nsew', pad_xy, no_scroll_bars=True, bg='light yellow',
          width=30, height=100),
        f(fr_canvas, canvas_graph, 'canvas', 0, 0, 1, 2, 'nsew', pad_xy, no_scroll_bars=True, bg='pink', width=500,
          height=100),

        f(fr, fr_btn, 'frame', 3, 3, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_0, c_0)),
        f(fr_btn, entry, 'entry', 0, 0, 0, 0, 'nsew', pad_xy),
        f(fr_btn, button_apply, 'button', 0, 0, 1, 1, 'nsew', pad_xy, **{'text': 'Apply'}),
        f(fr_btn, button_ok, 'button', 0, 0, 2, 2, 'nsew', pad_xy, **{'text': 'OK'}),
    ]

    return view_model
