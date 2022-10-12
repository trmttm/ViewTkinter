import interface_tk as intf


def connection_manager(frame_ie='frame_connection_manager',
                       pad_xy=(0, 0)) -> list:
    f = intf.widget_model

    r_2 = ((2,), (1,))
    r_0 = ((0,), (1,))
    c_0 = ((0,), (1,))
    c_1 = ((1,), (1,))
    c_2 = ((2,), (1,))

    fr = 'frame_local'
    view_model = [
        f(frame_ie, fr, 'frame', 0, 0, 0, 0, 'nsew', pad_xy, **intf.frame_options(r_2, c_0)),
    ]

    return view_model
