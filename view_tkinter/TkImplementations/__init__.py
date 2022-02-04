import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import askyesno
from typing import Callable
from typing import Tuple
from typing import Type
from typing import Union

from . import canvas_actions
from . import keyboard_shortcut
from . import tree_actions


class EntryWithText(ttk.Entry):
    def __init__(self, parent, *_, **kwargs):
        value = kwargs['default_value'] if 'default_value' in kwargs else ''
        auto_select_off = kwargs['auto_select_off'] if 'auto_select_off' in kwargs else False
        self._var = var = widgets[STRING_VAR](value=value)
        if 'default_value' in kwargs:
            del kwargs['default_value']
        if 'auto_select_off' in kwargs:
            del kwargs['auto_select_off']
        super(EntryWithText, self).__init__(parent, textvariable=var, **kwargs)

        if not auto_select_off:
            self.bind('<FocusIn>', lambda *_: self.selection_range(0, tk.END))

    def get_value(self):
        self._var.get()

    def set_value(self, value):
        self._var.set(value)

    def bind_focus_out(self, command):
        self.bind('<FocusOut>', command)

    def bind_update(self, command):
        self._var.trace('w', command)


class CheckbuttonWithBool(ttk.Checkbutton):
    def __init__(self, parent, *_, **kwargs):
        if 'value' in kwargs:
            value = kwargs['value']
            del kwargs['value']
        else:
            value = 0
        self._var = widgets[BOOLEAN_VAR](value=value)
        super(CheckbuttonWithBool, self).__init__(parent, variable=self._var, command=self._upon_change, **kwargs)

    def get_value(self) -> bool:
        return self._var.get()

    def set_value(self, value: bool):
        self._var.set(value)

    def _upon_change(self, *args, **kwargs):
        pass


class ComboBoxWithText(ttk.Combobox):
    def __init__(self, parent, *_, **kwargs):
        self._var = widgets[STRING_VAR](value='')
        super(ComboBoxWithText, self).__init__(parent, textvariable=self._var, **kwargs)

    def get_value(self) -> str:
        return self._var.get()

    def set_value(self, value):
        self._var.set(value)

    def bind_callback_upon_selection(self, callback):
        self.bind('<<ComboboxSelected>>', lambda _: callback(self.get_value()))


ROOT = 'root'
FRAME = 'frame'
BUTTON = 'button'
CANVAS = 'canvas'
ENTRY = 'entry'
STRING_VAR = 'string_var'
INT_VAR = 'int_var'
LABEL = 'label'
TREEVIEW = 'treeview'
PANED_WINDOW = 'paned_window'
NOTEBOOK = 'notebook'
TEXTBOX = 'text'
RADIOBUTTON = 'radio_button'
SCROLLBAR = 'scroll_bar'
TOPLEVEL = 'toplevel'
CHECK_BUTTON = 'check_button'
BOOLEAN_VAR = 'bool_var'
COMBO_BOX = 'combo_box'

# Tree actions
widget_tree_view = tree_actions.widget_tree_view
get_tree_selection_values = tree_actions.get_tree_values
bind_tree = tree_actions.bind_tree
add_treeview = tree_actions.add_treeview
update_tree = tree_actions.update_tree
get_tree_selection_text = tree_actions.get_tree_selection_text
tree_focused_values = tree_actions.tree_focused_values
tree_selected_values = tree_actions.tree_selected_values
get_selected_tree_item_orders = tree_actions.get_selected_tree_item_orders
focus_tree = tree_actions.focus_tree
select_multiple_tree_items = tree_actions.select_multiple_tree_items
tree_number_of_items = tree_actions.tree_number_of_items

# Canvas actions
widget_canvas = canvas_actions.widget_canvas
add_canvas = canvas_actions.add_canvas
bind_canvas = canvas_actions.bind_canvas
add_text_box = canvas_actions.add_text_box
add_rectangle = canvas_actions.add_rectangle
add_text = canvas_actions.add_text
remove_shapes = canvas_actions.remove_shapes
connect_shapes = canvas_actions.connect_shapes
move_shapes = canvas_actions.move_shapes
set_coordinates = canvas_actions.set_coordinate
highlight_shapes = canvas_actions.highlight_shapes
draw_rectangle = canvas_actions.draw_rectangle
set_border_color = canvas_actions.set_border_color
set_text_color = canvas_actions.set_text_color
set_font_size = canvas_actions.set_font_size
set_fill_color = canvas_actions.set_fill_color
set_border_width = canvas_actions.set_border_width
set_line_arrow = canvas_actions.set_line_arrow
draw_line = canvas_actions.draw_line
add_line = canvas_actions.add_line
clear_canvas = canvas_actions.clear_canvas
update_canvas_scroll_region = canvas_actions.update_canvas_scroll_region
scroll_canvas = canvas_actions.scroll_canvas
get_canvas_width = canvas_actions.get_canvas_width
get_canvas_height = canvas_actions.get_canvas_height
bind_change_canvas_size = canvas_actions.bind_change_canvas_size
get_mouse_canvas_coordinates = canvas_actions.get_mouse_canvas_coordinates
save_canvas = canvas_actions.save_canvas
clear_shapes_by_tag = canvas_actions.clear_shapes_by_tag

get_mid_y_coordinates_of_all_rectangles_on_canvas = canvas_actions.get_mid_y_coordinates_of_all_rectangles_on_canvas
get_clicked_rectangle = canvas_actions.get_clicked_rectangle
move_item_vertically_within_range = canvas_actions.move_item_vertically_within_range

widgets = {
    ROOT: tk.Tk,
    FRAME: ttk.Frame,
    BUTTON: ttk.Button,
    CANVAS: widget_canvas,
    ENTRY: EntryWithText,
    STRING_VAR: tk.StringVar,
    LABEL: ttk.Label,
    TREEVIEW: widget_tree_view,
    PANED_WINDOW: ttk.Panedwindow,
    NOTEBOOK: ttk.Notebook,
    TEXTBOX: tk.Text,
    RADIOBUTTON: ttk.Radiobutton,
    SCROLLBAR: ttk.Scrollbar,
    TOPLEVEL: tk.Toplevel,
    CHECK_BUTTON: CheckbuttonWithBool,
    BOOLEAN_VAR: tk.BooleanVar,
    COMBO_BOX: ComboBoxWithText,
    INT_VAR: tk.IntVar,
}


def define_styles():
    style = ttk.Style()
    # style.theme_use(style.theme_names()[5])
    style.configure('a.TFrame', )
    style.configure('a.TButton', foreground='blue')


def instantiate_root(width: int = None, height: int = None) -> tk.Tk:
    if width is None:
        width = 900
    if height is None:
        height = 600
    root = widgets['root']()
    try:
        root.iconbitmap(default='applet.ico')
    except:
        pass  # Mac will cause error
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.geometry(f'{width}x{height}')
    define_styles()
    return root


def callback_keyboard(event, command):
    k = keyboard_shortcut
    state = event.state
    char = event.char
    keysym = event.keysym

    state = k.tk_interpret_state(state)
    key, adjustment = k.interpret_key(char, keysym, state)
    modifier = k.tk_state_adjustment(char, state, adjustment, keysym)
    command(modifier, key)


def bind_keyboard_shortcut(widget: Union[tk.Tk, tk.Toplevel], command: Callable):
    widget.bind('<Key>', lambda e: callback_keyboard(e, command))


def get_focused_widget(root: tk.Tk) -> str:
    return root.focus_get()


def set_title(root: tk.Tk, title: str):
    root.title(title)


def set_exception_catcher(callback: Callable):
    tk.Tk.report_callback_exception = callback


def add_widgets(widget_dictionary, view_model: Union[list, tuple]):
    for widget_data in view_model:
        parent_id, widget_id, widget_type, row1, row2, col1, col2, sticky, pad_xy, options = widget_data
        widget_class = widgets[widget_type]
        parent = widget_dictionary[parent_id]
        rowspan, columnspan = row2 - row1 + 1, col2 - col1 + 1
        padx, pady = pad_xy or (0, 0)

        if widget_type == FRAME:
            widget = add_frame(options, parent, widget_class)
        elif widget_type == ENTRY:
            widget = EntryWithText(parent, **options)
        elif widget_type == CANVAS:
            widget = add_canvas(options, parent, widget_class)
        elif widget_type == TREEVIEW:
            widget = add_treeview(options, parent, widget_class)
        elif widget_type == PANED_WINDOW:
            widget = add_paned_window(options, parent, widget_class, widget_dictionary)
        elif widget_type == NOTEBOOK:
            widget = add_notebook(options, parent, widget_dictionary)
        elif widget_type == RADIOBUTTON:
            widget = add_radio_button(options, parent, widget_dictionary)
        elif widget_type == TOPLEVEL:
            add_toplevel(options, parent, widget_class, widget_dictionary, widget_id)
            continue
        elif widget_type == CHECK_BUTTON:
            widget = CheckbuttonWithBool(parent, **options)
        else:
            widget = widget_class(parent, **options)

        widget_dictionary[widget_id] = widget
        widget.grid(row=row1, column=col1, rowspan=rowspan, columnspan=columnspan, sticky=sticky, padx=padx, pady=pady)


def add_frame(options, parent, widget_class: Type[ttk.Frame]):
    if 'frame options' in options:
        frame_options_ = options['frame options']
        del options['frame options']
    else:
        frame_options_ = {}

    widget = widget_class(parent, **options)

    if frame_options_ != {}:
        rows, weights = frame_options_['rows_and_weights']
        for row, weight in zip(rows, weights):
            widget.grid_rowconfigure(row, weight=weight)
        cols, weights = frame_options_['cols_and_weights']
        for col, weight in zip(cols, weights):
            widget.grid_columnconfigure(col, weight=weight)
        propagate = frame_options_['propagate']
        widget.grid_propagate(propagate)
    return widget


def add_paned_window(options: dict, parent, widget_class: Type[ttk.Panedwindow], widget_dictionary: dict):
    is_vertical = options['is_vertical']
    frame_ids = options['frame_ids']
    weights = options['weights'] if 'weights' in options else tuple(None for _ in frame_ids)

    orient = tk.VERTICAL if is_vertical else tk.HORIZONTAL
    paned_window = widget_class(parent, orient=orient)
    for frame_id, weight in zip(frame_ids, weights):
        frame = widgets[FRAME](paned_window, style='a.TFrame')
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        widget_dictionary[frame_id] = frame
        paned_window.add(frame, weight=weight)
    return paned_window


def set_paned_window_sash_position(paned_window: ttk.Panedwindow, position: int = None):
    if position is not None:
        paned_window.sashpos(0, position)


def add_notebook(options: dict, parent, widget_dictionary: dict) -> ttk.Notebook:
    frame_ids: tuple = options['frame_ids']
    frame_names: tuple = options['frame_names']
    notebook = widgets[NOTEBOOK](parent)
    for frame_id, frame_name in zip(frame_ids, frame_names):
        frame = widgets[FRAME](notebook)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        notebook.add(frame, text=frame_name)
        widget_dictionary[frame_id] = frame
    return notebook


def add_radio_button(options: dict, parent, widget_dictionary: dict) -> ttk.Frame:
    int_var = widgets[INT_VAR]()
    int_var_id = options['inv_var_id']
    widget_dictionary[int_var_id] = int_var

    frame_id = options['frame_id']
    vertical: bool = options['is_vertical']
    names: tuple = options['names']

    frame = widgets[FRAME](parent)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    widget_dictionary[frame_id] = frame

    for n, name in enumerate(names):
        rb = ttk.Radiobutton(frame, text=name, variable=int_var, value=n)
        if vertical:
            rb.grid(row=n, column=0, sticky='nsew')
            frame.grid_columnconfigure(n, weight=1)
            frame.grid_rowconfigure(n, weight=1)
        else:
            rb.grid(row=0, column=n, sticky='nsew')
            frame.grid_columnconfigure(n, weight=1)

    return frame


def add_toplevel(options, parent, widget_class, widget_dictionary, widget_id):
    title, geometry = None, None
    if 'title' in options:
        title = options['title']
        del options['title']

    if 'geometry' in options:
        geometry = options['geometry']
        del options['geometry']

    widget: tk.Toplevel = widget_class(parent, **options)
    widget_dictionary[widget_id] = widget
    widget.grid_rowconfigure(0, weight=1)
    widget.grid_columnconfigure(0, weight=1)
    widget.grab_set()
    if title is not None:
        widget.title(title)
    if geometry is not None:
        widget.geometry(geometry)


def bind_notebook(callback: Callable, notebook: ttk.Notebook):
    on_click = callback
    notebook.bind('<Button-1>', on_click)


def get_mouse_coordinates(event) -> Tuple[int, int]:
    return event.x, event.y


def bind_command_to_widget(callback: Callable, widget):
    type_check = type(widget)
    if type_check == widgets[CANVAS]:
        bind_canvas(callback, widget)
    elif type_check == widgets[TREEVIEW]:
        bind_tree(callback, widget)
    elif type_check == widgets[NOTEBOOK]:
        bind_notebook(callback, widget)
    elif type_check == widgets[ENTRY]:
        w: EntryWithText = widget
        w.bind_focus_out(callback)
    elif type_check == widgets[ROOT]:
        w: tk.Tk = widget
        w.bind("<MouseWheel>", callback)
    elif type_check == widgets[TOPLEVEL]:
        w: tk.Toplevel = widget
        w.protocol("WM_DELETE_WINDOW", callback)
    elif type_check == widgets[COMBO_BOX]:
        w: ComboBoxWithText = widget
        w.bind_callback_upon_selection(callback)
    else:
        widget.configure(command=callback)


def entry_update(callback: Callable, widget):
    type_check = type(widget)
    if type_check == widgets[ENTRY]:
        w: EntryWithText = widget
        w.bind_update(callback)


def update_menu_bar(root: tk.Tk, menu_bar_model: dict):
    root.option_add('*tearOff', tk.FALSE)
    menubar = tk.Menu(root)
    for menu_name, sub_menues_dict in menu_bar_model.items():
        top_level_menu = tk.Menu(menubar)
        menubar.add_cascade(label=menu_name, menu=top_level_menu)
        for sub_menu_name, command_or_menu in sub_menues_dict.items():
            if type(command_or_menu) == dict:
                menu_model = command_or_menu
                sub_sub_menu = tk.Menu(top_level_menu)
                top_level_menu.add_cascade(label=sub_menu_name, menu=sub_sub_menu)
                for sub_sub_menu_name, command in menu_model.items():
                    sub_sub_menu.add_command(label=sub_sub_menu_name, command=command)
            else:
                command = command_or_menu
                top_level_menu.add_command(label=sub_menu_name, command=command)
    root.config(menu=menubar)


def focus(widget, **kwargs):
    if type(widget) == widgets[TREEVIEW]:
        focus_tree(widget, kwargs)
    else:
        widget.focus()


def get_widget_value(widget):
    widget_type = type(widget)
    if widget_type == widgets[TREEVIEW]:
        return get_tree_selection_values(widget)
    elif widget_type == widgets[CHECK_BUTTON]:
        w: CheckbuttonWithBool = widget
        return w.get_value()
    else:
        try:
            return widget.get()
        except AttributeError:
            pass


def set_widget_value(widget, value):
    widget_type = type(widget)
    if widget_type == widgets[TREEVIEW]:
        view_model = value
        update_tree(widget, view_model)
    elif widget_type in (widgets[LABEL], widgets[BUTTON]):
        widget['text'] = value
    elif widget_type in (widgets[ENTRY], widgets[CHECK_BUTTON]):
        widget.set_value(value)
    elif widget_type == widgets[TEXTBOX]:
        widget.delete('0.0', tk.END)
        widget.insert('0.0', value)
    elif widget_type == widgets[COMBO_BOX]:
        widget.set_value(value)


def update_status_bar(label: ttk.Label, view_model: dict):
    label['text'] = view_model['text']
    color = view_model['text_color'] if 'text_color' in view_model else 'black'
    label['foreground'] = color

    if 'update' in view_model:
        if view_model['update']:
            label.update()


def switch_frame(frame: ttk.Frame):
    try:
        frame.tkraise()
    except AttributeError:
        pass


def ask_color(title: str):
    return colorchooser.askcolor(title=title)


def get_paned_window_sash_position(paned_window: ttk.Panedwindow) -> int:
    return paned_window.sashpos(0)


def select_folder(initialdir=None):
    user_feedback = filedialog.askdirectory(title='Choose Folder', initialdir=initialdir)
    return None if user_feedback is None else user_feedback


def ask_save_file(initialdir=None):
    user_feedback = filedialog.asksaveasfile(title='Save as...', initialdir=initialdir)
    return None if user_feedback is None else user_feedback.name


def ask_open_file(initialdir=None):
    user_feedback = filedialog.askopenfile(title='Select File', initialdir=initialdir)
    return None if user_feedback is None else user_feedback.name


def ask_yes_no(title, message) -> bool:
    return askyesno(title, message)


def close(widget):
    if type(widget) == widgets[TOPLEVEL]:
        widget.grab_release()  # entries on root will be enabled.

    widget.destroy()
