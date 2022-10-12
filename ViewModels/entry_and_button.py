import interface_tk as intf


def entry_and_button(frame_id, entry_id, entry_width, button_id, button_text, button_width, default_entry: str = ''):
    f = intf.widget_model
    fmd_button_entry = [
        f(frame_id, entry_id, 'entry', 0, 0, 0, 0, 'nsew', **{'default_value': default_entry, 'width': entry_width}),
        f(frame_id, button_id, 'button', 0, 0, 1, 1, 'nsew', **{'text': button_text, 'width': button_width}),
    ]
    return fmd_button_entry
