import interface_tk as intf


def create_d_pad_model(frame_id, button_ids_x4: tuple, button_width=None) -> list:
    f = intf.widget_model
    b = button_ids_x4
    view_model = [f(frame_id, b[0], 'button', 0, 0, 0, 0, 'nsew', **{'text': '←', 'width': button_width}),
                  f(frame_id, b[1], 'button', 0, 0, 1, 1, 'nsew', **{'text': '↑', 'width': button_width}),
                  f(frame_id, b[2], 'button', 0, 0, 2, 2, 'nsew', **{'text': '↓', 'width': button_width}),
                  f(frame_id, b[3], 'button', 0, 0, 3, 3, 'nsew', **{'text': '→', 'width': button_width}),
                  ]
    return view_model
