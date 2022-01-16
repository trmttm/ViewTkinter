import tkinter as tk
import tkinter.font as tkFont
from _tkinter import TclError
from tkinter import ttk
from typing import Callable
from typing import List
from typing import Type

import os_identifier

widget_canvas = tk.Canvas
widget_scroll_bar = ttk.Scrollbar
tk_shift = 'Shift'
tk_control = 'Control'
tk_command = 'Command'
tk_option = 'Option'
tk_alt = 'Alt'

arrows = {
    'last': tk.LAST,
    'end': tk.LAST,
    'to': tk.LAST,
    'both': tk.BOTH,
    'first': tk.FIRST,
    'start': tk.FIRST,
    'from': tk.FIRST,
    None: tk.NONE,
}


def add_canvas(options: dict, parent, widget_class: Type[tk.Canvas]):
    callback = None
    has_call_back_function = 'bind' in options
    if has_call_back_function:
        callback = options['bind']
        del options['bind']

    scroll = add_scroll_bars(options)
    if 'no_scroll_bars' in options:
        del options['no_scroll_bars']

    widget = widget_class(parent, **options)

    if scroll:
        scroll_x = widget_scroll_bar(parent, orient="horizontal", command=widget.xview)
        scroll_x.grid(row=1, column=0, sticky="ew")
        scroll_y = widget_scroll_bar(parent, orient="vertical", command=widget.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        widget.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        widget.configure(scrollregion=widget.bbox("all"))

    if has_call_back_function:
        bind_canvas(callback, widget)
    return widget


def add_scroll_bars(options: dict) -> bool:
    if 'no_scroll_bars' in options:
        return not options['no_scroll_bars']
    else:
        return True


def scroll_canvas(canvas: tk.Canvas, x=0, y=0):
    if canvas.bbox('all') is None:
        return
    x11, y11, x12, y12 = canvas_visible_region(canvas)
    x21, y21, x22, y22 = canvas.bbox('all')

    scrolling_left = 0 < x
    scrolling_right = x < 0
    scrolling_down = y < 0
    scrolling_up = 0 < y

    no_room_to_scroll_left = x11 <= x21
    no_room_to_scroll_right = x22 <= x12
    no_room_to_scroll_down = y22 <= y12
    no_room_to_scroll_up = y11 <= y21

    if scrolling_left and no_room_to_scroll_left:
        return
    elif scrolling_right and no_room_to_scroll_right:
        return
    elif scrolling_down and no_room_to_scroll_down:
        return
    elif scrolling_up and no_room_to_scroll_up:
        return

    canvas.xview_scroll(-1 * int(x / 1), "units")
    canvas.yview_scroll(-1 * int(y / 1), "units")


def canvas_visible_region(canvas: tk.Canvas):
    x1, y1 = canvas.canvasx(0), canvas.canvasy(0)
    w, h = canvas.winfo_width(), canvas.winfo_height()
    x2, y2 = canvas.canvasx(w), canvas.canvasy(h)
    return x1, y1, x2, y2


def update_canvas_scroll_region(canvas: tk.Canvas):
    bbox = canvas.bbox('all')
    if bbox is None:
        scroll_region = None
    else:
        x1, y1 = 0, 0
        x2, y2 = bbox[2:]
        scroll_region = (x1, y1, x2, y2)
    canvas.configure(scrollregion=scroll_region)


def add_text_box(canvas: tk.Canvas, view_model: list):
    for text_box_data in view_model:
        add_rectangle(canvas, text_box_data)
        add_text(canvas, text_box_data)


def add_text(canvas, text_box_data):
    w, h = text_box_data['width'], text_box_data['height']
    x1, y1 = text_box_data['x'], text_box_data['y']
    x2, y2 = x1 + w, y1 + h
    text_align = text_box_data.get('text_align', '')
    text_options = {
        'text': text_box_data['text'],
        'tags': text_box_data['tags'],
        'angle': text_box_data['text_rotation'],
        'font': tkFont.Font(family="Arial"),
    }
    text_x = (x1 + x2) / 2
    text_y = (y1 + y2) / 2
    if 'top' in text_align:
        text_y = y1
        text_options.update({'anchor': 'n'})
    if 'bottom' in text_align:
        text_y = y2
        text_options.update({'anchor': 's'})
    if 'left' in text_align:
        text_x = x1
        anchor = text_options.get('anchor', '') + 'w'
        text_options.update({'anchor': anchor})
    if 'right' in text_align:
        text_x = x2
        anchor = text_options.get('anchor', '') + 'e'
        text_options.update({'anchor': anchor})
    canvas.create_text(text_x, text_y, **text_options)


def add_rectangle(canvas, view_model):
    w, h = view_model['width'], view_model['height']
    x1, y1 = view_model['x'], view_model['y']
    x2, y2 = x1 + w, y1 + h
    rectangle_options = {
        'outline': view_model['border_color'],
        'width': view_model['border_width'],
        'fill': view_model['fill'],
        'tags': view_model['tags'],
    }
    canvas.create_rectangle(x1, y1, x2, y2, **rectangle_options)


def remove_shapes(canvas: tk.Canvas, view_model: list):
    for tag_to_remove in view_model:
        canvas.delete(tag_to_remove)


def move_shapes(canvas: tk.Canvas, view_model: dict):
    for tag, (delta_x, delta_y) in view_model.items():
        canvas.move(tag, delta_x, delta_y)


def set_coordinate(canvas: tk.Canvas, view_model: dict):
    for tag, new_coordinates in view_model.items():
        canvas.coords(tag, new_coordinates)


def connect_shapes(canvas: tk.Canvas, view_model: List[dict]):
    command_on_all_canvas_shapes(canvas, delete_line)
    for connection_data in view_model:
        point_from, point_to = connection_data['coordinates']
        color = connection_data['color']
        if 'arrow' in connection_data and connection_data['arrow'] in arrows:
            arrow = arrows[connection_data['arrow']]
        else:
            arrow = tk.LAST
        canvas.create_line(*point_from, *point_to, arrow=arrow, fill=color)


def delete_line(canvas: tk.Canvas, canvas_shape):
    if canvas.type(canvas_shape) == 'line':
        canvas.delete(canvas_shape)


def command_on_all_canvas_shapes(canvas: tk.Canvas, command: Callable):
    for canvas_shape in canvas.find_all():
        command(canvas, canvas_shape)


def highlight_shapes(canvas: tk.Canvas, view_model: dict):
    for canvas_id in canvas.find_all():
        tag = get_tag_from_canvas_id(canvas, canvas_id)
        if tag in view_model:
            data = view_model[tag]
            border_color = data['border_color']
            fill_color = data['fill']
            text_color = data['text_color']
            border_width = data['border_width']
            highlight_rectangle(border_color, canvas, canvas_id, fill_color, border_width)
            highlight_text(canvas, canvas_id, text_color)


def highlight_rectangle(border_color, canvas: tk.Canvas, canvas_id, fill_color, width):
    if canvas.type(canvas_id) == 'rectangle':
        canvas.itemconfigure(canvas_id, {'outline': border_color, 'fill': fill_color, 'width': width})


def highlight_text(canvas: tk.Canvas, canvas_id, text_color):
    if canvas.type(canvas_id) == 'text':
        canvas.itemconfigure(canvas_id, {'fill': text_color})


def draw_rectangle(canvas: tk.Canvas, view_model: dict):
    clear_all_rectangles(canvas)
    for rect_data in view_model.values():
        coords1, coords2 = rect_data['coordinate_from'], rect_data['coordinate_to']
        color = rect_data['line_color']
        width = rect_data['line_width']
        tags = rect_data['tags'] if 'tags' in rect_data else None
        fill = rect_data['fill'] if 'fill' in rect_data else None
        canvas.create_rectangle(*coords1, *coords2, outline=color, width=width, tags=tags, fill=fill)


def set_border_color(canvas: tk.Canvas, view_model: dict):
    for tag, color in view_model.items():
        canvas.itemconfigure(tag, fill=color)


def set_text_color(canvas: tk.Canvas, view_model: dict):
    for tag, color in view_model.items():
        canvas.itemconfigure(tag, fill=color)


def set_font_size(canvas: tk.Canvas, view_model: dict):
    for tag, font_size in view_model.items():
        font = ('', font_size)
        canvas.itemconfigure(tag, font=font)


def set_border_width(canvas: tk.Canvas, view_model: dict):
    for tag, width in view_model.items():
        canvas.itemconfigure(tag, width=width)


def set_line_arrow(canvas: tk.Canvas, view_model: dict):
    for tag, arrow_data in view_model.items():
        arrow = arrows[arrow_data]
        canvas.itemconfigure(tag, arrow=arrow)


def set_fill_color(canvas: tk.Canvas, view_model: dict):
    for tag, color in view_model.items():
        canvas.itemconfigure(tag, fill=color)


def add_line(canvas: tk.Canvas, view_model: dict):
    for line_data in view_model.values():
        coords1, coords2 = line_data['coordinate_from'], line_data['coordinate_to']
        color = line_data['line_color']
        width = line_data['line_width']
        if 'arrow' in line_data and line_data['arrow'] in arrows:
            arrow = arrows[line_data['arrow']]
        else:
            arrow = tk.LAST
        tags = line_data.get('tags', ())
        tags = ('line',) + tags
        canvas.create_line(*coords1, *coords2, fill=color, width=width, tags=tags, arrow=arrow)


def draw_line(canvas: tk.Canvas, view_model: dict):
    clear_all_lines(canvas)
    add_line(canvas, view_model)


def clear_all_text_boxes(canvas: tk.Canvas):
    clear_shapes_by_tag(canvas, 'TagTextBox')


def clear_all_rectangles(canvas: tk.Canvas):
    clear_shapes_by_tag(canvas, 'rectangle_selector')


def clear_all_lines(canvas: tk.Canvas):
    clear_shapes_by_tag(canvas, 'line')


def clear_shapes_by_tag(canvas: tk.Canvas, tag: str):
    command_on_all_canvas_shapes(canvas, lambda c, s: _clear_shapes_by_tag(c, s, tag))


def _clear_shapes_by_tag(canvas: tk.Canvas, canvas_shape, tag):
    if tag in canvas.itemcget(canvas_shape, 'tags'):
        canvas.delete(canvas_shape)


def get_tag_from_canvas_id(canvas: tk.Canvas, canvas_id):
    tags = canvas.itemcget(canvas_id, 'tags')
    tag = tags.split(' ')[0] if ' ' in tags else tags
    return tag


def bind_canvas(callback, widget: tk.Canvas):
    left = 'LEFT'
    right = 'RIGHT'
    middle = 'MIDDLE'

    """
    Right click
    2 on the Mac
    3 on unix and windows.
    """

    if os_identifier.is_mac:
        modifiers = [tk_shift, tk_control, tk_command, tk_option]
        bind_mouse_actions(1, left, callback, widget, modifiers)
        bind_mouse_actions(2, right, callback, widget, modifiers)
        bind_mouse_actions(3, middle, callback, widget, modifiers)
    else:
        modifiers = [tk_shift, tk_control, tk_alt]
        bind_mouse_actions(1, left, callback, widget, modifiers)
        bind_mouse_actions(3, right, callback, widget, modifiers)
        bind_mouse_actions(2, middle, callback, widget, modifiers)

    mouse_in = 'MOUSE_IN'
    mouse_out = 'MOUSE_OUT'
    cb = callback
    widget.bind('<Enter>', lambda event: cb(widget.canvasx(event.x), widget.canvasy(event.y), None, None, mouse_in))
    widget.bind('<Leave>', lambda event: cb(widget.canvasx(event.x), widget.canvasy(event.y), None, None, mouse_out))


def bind_change_canvas_size(callback: Callable, canvas: tk.Canvas):
    canvas.bind("<Configure>", callback)


def get_mouse_canvas_coordinates(canvas: tk.Canvas) -> tuple:
    x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    y = canvas.winfo_pointery() - canvas.winfo_rooty()
    return canvas.canvasx(x), canvas.canvasx(y)


def bind_mouse_actions(button_no, button: str, callback: Callable, widget: tk.Canvas, modifiers=None):
    click = 'CLICK'
    drag = 'CLICK_MOTION'
    release = 'CLICK_RELEASE'
    mouse_wheel = 'MOUSE_WHEEL'
    modifiers_mapper = {
        tk_shift: 'Shift',
        tk_control: 'Control',
        tk_command: 'Command',
        tk_option: 'Alt_Option',
        tk_alt: 'Alt_Option',
        None: None
    }

    def f(event, button_, modifier_, gesture_, **kwargs):
        """
        event.x, event.y are screen x, y
        canvasx, canvasy are canvas x, y
        """
        x = widget.canvasx(event.x)
        y = widget.canvasy(event.y)
        callback(x, y, button_, modifiers_mapper[modifier_], gesture_, **kwargs)

    def kw(event) -> dict:
        scroll_x = 0 if event.state == 0 else event.delta
        scroll_y = 0 if event.state == 1 else event.delta
        return {'scroll_x': scroll_x, 'scroll_y': scroll_y, }

    widget.bind(f'<Button-{button_no}>', lambda event: f(event, button, None, click))
    widget.bind(f'<B{button_no}-Motion>', lambda event: f(event, button, None, drag))
    widget.bind(f'<ButtonRelease-{button_no}>', lambda event: f(event, button, None, release))
    widget.bind(f'<MouseWheel>', lambda event: f(event, None, None, mouse_wheel, **kw(event)))

    for modifier in (modifiers or []):
        widget.bind(f'<{modifier}-Button-{button_no}>', lambda event, m=modifier: f(event, button, m, click))
        widget.bind(f'<{modifier}-B{button_no}-Motion>', lambda event, m=modifier: f(event, button, m, drag))
        widget.bind(f'<{modifier}-ButtonRelease-{button_no}>', lambda event, m=modifier: f(event, button, m, release))

        """
        Disabling below because, for unknown reason, modifier + mousewheel is invoked instead of MouseWheel...
        """
        # widget.bind(f'<{modifier}-MouseWheel>', lambda event, m=modifier: f(event, None, m, mouse_wheel, **kw(event)))


def clear_canvas(canvas: tk.Canvas):
    canvas.delete('all')


def get_canvas_width(canvas: tk.Canvas) -> float:
    return float(canvas.winfo_width())


def get_canvas_height(canvas: tk.Canvas) -> float:
    return float(canvas.winfo_height())


def add_tag_all(canvas: tk.Canvas, tag: str):
    canvas.addtag_all(tag)


def get_clicked_rectangle(canvas: tk.Canvas):
    item = canvas.find_withtag("current")
    if canvas.type(item) == 'rectangle':
        return item


def move_item_vertically_within_range(canvas: tk.Canvas, item, delta_x, delta_y, y_range: tuple):
    try:
        coords = canvas.coords(item)
    except TclError:
        return

    if item is not None and len(coords) == 4:
        x1, y1, x2, y2 = coords
        y = (y1 + y2) / 2
        y_min, y_max = y_range

        delta_y = min(y_max - y, delta_y)
        delta_y = max(y_min - y, delta_y)
        canvas.move(item, delta_x, delta_y)


def get_mid_y_coordinates_of_all_rectangles_on_canvas(canvas: tk.Canvas) -> tuple:
    coordinates = {}
    rectangles = tuple(item for item in canvas.find_all() if canvas.type(item) == 'rectangle')
    for rectangle_id in rectangles:
        x = canvas.coords(rectangle_id)[0]
        y = (canvas.coords(rectangle_id)[1] + canvas.coords(rectangle_id)[3]) / 2
        coordinates[x] = y
    y_coordinates_sorted_by_x = tuple(coordinates[x_] for x_ in sorted(coordinates.keys()))
    return y_coordinates_sorted_by_x


def save_canvas(canvas: tk.Canvas, file_name: str):
    canvas.postscript(file=file_name, colormode='color')
