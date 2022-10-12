import interface_tk as intf


def main_menu_contents(frame_id, button_width=None, padding: tuple = None) -> list:
    """
    Considered Notebook widget, but it'shapes too slow loading children widget everytime.
    """
    f = intf.widget_model
    fid = frame_id
    b = 'button'
    p = padding
    w = button_width
    style = 'a.TButton'
    fr_m = 'frame_middle'

    view_model = [
        f(fid, 'frame_left', 'frame', 0, 0, 0, 0, 'nsew', ),
        f(fid, fr_m, 'frame', 0, 0, 1, 1, 'nsew', ),
        f(fid, 'frame_right', 'frame', 0, 0, 2, 2, 'nsew', ),
        f(fr_m, 'm1', b, 0, 0, 0, 0, 'nsew', p, **{'text': 'Design', 'width': w, 'style': style, 'underline': 0}),
        f(fr_m, 'm2', b, 0, 0, 1, 1, 'nsew', p, **{'text': 'Templates', 'width': w, 'style': style, 'underline': 0}),
        f(fr_m, 'm3', b, 0, 0, 2, 2, 'nsew', p, **{'text': 'States', 'width': w, 'style': style, 'underline': 0}),
        f(fr_m, 'm4', b, 0, 0, 3, 3, 'nsew', p, **{'text': 'Macro', 'width': w, 'style': style, 'underline': 0}),
        f(fr_m, 'm5', b, 0, 0, 4, 4, 'nsew', p, **{'text': 'Setting', 'width': w, 'style': style, 'underline': 6}),
    ]
    return view_model
