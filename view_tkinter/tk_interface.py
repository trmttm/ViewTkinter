from typing import Tuple


def widget_model(parent_id, widget_id, widget_type, row1, row2, col1, col2, sticky, pad_xy=None, **options) -> tuple:
    return parent_id, widget_id, widget_type, row1, row2, col1, col2, sticky, pad_xy, options


def frame_options(rows_and_weights: Tuple[tuple, tuple], cols_and_weights: Tuple[tuple, tuple], propagate=True) -> dict:
    return {'frame options': {'rows_and_weights': rows_and_weights, 'cols_and_weights': cols_and_weights,
                              'propagate': propagate}}


def entry_options(default_value: str = None, auto_select_off: bool = None) -> dict:
    option = {}
    if default_value is not None:
        option.update({'default_value': default_value})
    if auto_select_off is not None:
        option.update({'auto_select_off': auto_select_off})
    return option


def button_options(text, command) -> dict:
    return {'text': text, 'command': command}


def paned_window_options(is_vertical: bool, frame_ids: tuple, weights: tuple = None) -> dict:
    options = {'is_vertical': is_vertical, 'frame_ids': frame_ids}
    if (weights is not None) and (len(frame_ids) == len(weights)):
        options.update({'weights': weights})
    return options


def notebook_options(frame_ids: tuple, frame_names: tuple) -> dict:
    return {'frame_ids': frame_ids, 'frame_names': frame_names}


def radio_button_options(frame_id, inv_var_id, names, is_vertical=False) -> dict:
    return {'frame_id': frame_id, 'int_var_id': inv_var_id, 'names': names, 'is_vertical': is_vertical}


def top_level_options(title: str, width_height: tuple = None) -> dict:
    options = {'title': title}
    if width_height is not None:
        options.update({'geometry': f'{width_height[0]}x{width_height[1]}'})
    return options
