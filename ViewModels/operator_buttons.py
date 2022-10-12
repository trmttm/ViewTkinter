import interface_tk as intf


def operator_buttons(frame_id, button_width=None) -> list:
    f = intf.widget_model
    view_model = [
        f(frame_id, 'op1', 'button', 0, 0, 0, 0, 'nsew', **{'text': '+', 'width': button_width}),
        f(frame_id, 'op2', 'button', 0, 0, 1, 1, 'nsew', **{'text': '-', 'width': button_width}),
        f(frame_id, 'op3', 'button', 0, 0, 2, 2, 'nsew', **{'text': 'x', 'width': button_width}),
        f(frame_id, 'op4', 'button', 0, 0, 3, 3, 'nsew', **{'text': '/', 'width': button_width}), ]
    return view_model
