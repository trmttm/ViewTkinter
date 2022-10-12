import interface_tk as intf


def connector_canvas(frame_connector_canvas,
                     canvas_connector,
                     btn_close,
                     pad_xy=(0, 0),
                     ) -> list:
    f = intf.widget_model

    r_0 = ((0,), (1,))
    c_0 = ((0,), (1,))
    fr = 'frame_local'
    view_model = [
        f(frame_connector_canvas, fr, 'frame', 0, 0, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_0, c_0)),
        f(fr, canvas_connector, 'canvas', 0, 0, 0, 0, 'nsew', pad_xy, ),
        f(fr, btn_close, 'button', 2, 2, 0, 0, 'nse', pad_xy, **{'text': 'Close'}),
    ]

    return view_model
