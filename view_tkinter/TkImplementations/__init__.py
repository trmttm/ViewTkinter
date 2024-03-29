import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import font
from tkinter import ttk
from tkinter.messagebox import askyesno
from typing import Callable
from typing import Tuple
from typing import Type
from typing import Union

import os_identifier

from . import canvas_actions
from . import keyboard_shortcut
from . import mouse
from . import tree_actions

try:
    import tkinterdnd2 as tkdnd

    root_class = tkdnd.TkinterDnD.Tk
    tkinterdnd2_imported = True
except ImportError:
    root_class = tk.Tk
    tkinterdnd2_imported = False


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
        return self._var.get()

    def set_value(self, value):
        self._var.set(value)

    def bind_focus_out(self, command):
        self.bind('<FocusOut>', command)

    def bind_update(self, command):
        self._var.trace('w', command)

    def highlight(self):
        self.configure(style='Highlight.TEntry')

    def remove_highlight(self):
        self.configure(style='TEntry')


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
        super(ComboBoxWithText, self).__init__(parent, **kwargs)

    def get_value(self) -> str:
        return self.get()

    def set_value(self, value):
        self.set(value)

    def set_values(self, values: tuple):
        self['values'] = values

    def bind_callback_upon_selection(self, callback):
        self.bind('<<ComboboxSelected>>', lambda _: callback(self.get_value()))


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.canvas = canvas = tk.Canvas(self, bg=_from_rgb((236, 236, 236)), highlightthickness=0, )
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        canvas.bind('<Configure>', self.resize_canvas_window)

        self.canvas_window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        canvas.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='nsew')

    def resize_canvas_window(self, event):
        '''
        Canvas' behavior is different from parent.grid_colmnconfigure + .grid(row, col, sticky)
        Event binding is required to resize the frame within canvas.
        '''
        self.canvas.itemconfig(self.canvas_window, width=event.width)


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
SCROLLABLE_FRAME = 'scrollable_frame'

# Tree actions
widget_tree_view = tree_actions.widget_tree_view
get_tree_selection_values = tree_actions.get_tree_values
bind_tree = tree_actions.bind_tree
bind_tree_click_heading = tree_actions.bind_tree_click_heading
unbind_tree = tree_actions.unbind_tree
bind_tree_left_click = tree_actions.bind_tree_left_click
bind_tree_right_click = tree_actions.bind_tree_right_click
bind_tree_middle_click = tree_actions.bind_tree_middle_click
bind_tree_left_click_release = tree_actions.bind_tree_left_click_release
bind_tree_right_click_release = tree_actions.bind_tree_right_click_release
bind_tree_middle_click_release = tree_actions.bind_tree_middle_click_release
bind_tree_enter = tree_actions.bind_tree_enter
bind_tree_leave = tree_actions.bind_tree_leave
add_treeview = tree_actions.add_treeview
update_tree = tree_actions.update_tree
set_tree_headings = tree_actions.set_tree_headings
get_tree_selection_text = tree_actions.get_tree_selection_text
tree_focused_values = tree_actions.tree_focused_values
tree_selected_values = tree_actions.tree_selected_values
get_selected_tree_item_orders = tree_actions.get_selected_tree_item_orders
focus_tree = tree_actions.focus_tree
select_multiple_tree_items = tree_actions.select_multiple_tree_items
tree_number_of_items = tree_actions.tree_number_of_items
get_all_tree_values = tree_actions.get_all_tree_values
deselect_tree_items = tree_actions.deselect_tree_items

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
set_text_value = canvas_actions.set_text_value
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
    ROOT: root_class,
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
    SCROLLABLE_FRAME: ScrollableFrame,
    INT_VAR: tk.IntVar,
}


def change_style(style: ttk.Style):
    all_themes = style.theme_names()
    current_theme = style.theme_use()
    current_theme_index = all_themes.index(current_theme)
    next_index = current_theme_index + 1
    if next_index == len(all_themes):
        next_index = 0
    selected_theme = all_themes[next_index]
    style.theme_use(selected_theme)


def define_styles():
    style = ttk.Style()
    # style.theme_use(style.theme_names()[4])
    style.configure('a.TFrame', )
    style.configure('a.TButton', foreground='blue')

    if os_identifier.is_windows:  # This enables highlighting entry background.
        style.theme_use('clam')
        style.configure('Highlight.TEntry', fieldbackground='yellow')
    else:
        style.configure('Highlight.TEntry', background='yellow')

    row_height = None
    tree_style_options = {'background': "white", 'foreground': "black", 'fieldbackground': "white"}
    if row_height is not None:
        tree_style_options.update({'rowheight': row_height})
    style.configure("Treeview", **tree_style_options)

    # ★バグ対応を処理
    style.map('Treeview', foreground=fixed_map('foreground', style), background=fixed_map('background', style))
    return style


# ★バグ対応用の関数を追加
def fixed_map(option, style):
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]


def instantiate_root(width: int = None, height: int = None, fullscreen=False) -> tk.Tk:
    if width is None:
        width = 900
    if height is None:
        height = 600
    root = widgets['root']()
    try:
        root.iconbitmap(default='applet.ico')
    except:
        pass  # Mac will cause error
    if fullscreen:
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry(f'{w}x{h}+0+1')
    else:
        root.geometry(f'{width}x{height}')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.style = define_styles()
    return root


def callback_keyboard(event, command):
    k = keyboard_shortcut
    state = event.state
    char = event.char
    keysym = event.keysym
    print(f'Typed... state:{state}, char:{char}, keysym:{keysym}')

    state = k.tk_interpret_state(state)
    key, adjustment = k.interpret_key(char, keysym, state)
    modifier = k.tk_state_adjustment(char, state, adjustment, keysym)
    print(f'Modifier:{modifier}, Key:{key}')
    command(modifier, key)


def bind_keyboard_shortcut(widget: Union[tk.Tk, tk.Toplevel], command: Callable):
    widget.bind('<Key>', lambda e: callback_keyboard(e, command))


def bind_left_click(command: Callable, widget: Union[tk.Widget, ttk.Widget]):
    _bind_click(mouse.LEFT_CLICK, widget, command)


def bind_right_click(command: Callable, widget: Union[tk.Widget, ttk.Widget]):
    _bind_click(mouse.RIGHT_CLICK, widget, command)


def bind_middle_click(command: Callable, widget: Union[tk.Widget, ttk.Widget]):
    _bind_click(mouse.MIDDLE_CLICK, widget, command)


def bind_left_click_release(command: Callable, widget: Union[tk.Widget, ttk.Widget]):
    _bind_click_release(mouse.LEFT_CLICK, widget, command)


def bind_right_click_release(command: Callable, widget: Union[tk.Widget, ttk.Widget]):
    _bind_click_release(mouse.RIGHT_CLICK, widget, command)


def bind_middle_click_release(command: Callable, widget: Union[tk.Widget, ttk.Widget]):
    _bind_click_release(mouse.MIDDLE_CLICK, widget, command)


def _bind_click(n: int, widget: Union[tk.Widget, ttk.Widget], command: Callable):
    if widget is not None:
        widget.bind(f'<Button-{n}>', lambda e: command(e))


def _bind_click_release(n: int, widget: Union[tk.Widget, ttk.Widget], command: Callable):
    if widget is not None:
        widget.bind(f'<ButtonRelease-{n}>', lambda e: command(e))


def get_focused_widget(root: tk.Tk):
    return root.focus_get()


def set_title(root: tk.Tk, title: str):
    root.title(title)


def set_exception_catcher(callback: Callable):
    tk.Tk.report_callback_exception = callback


def add_widgets(widget_dictionary, view_model: Union[list, tuple]):
    key_scrollable_frames = 'scrollable_frames'
    for widget_data in view_model:
        parent_id, widget_id, widget_type, row1, row2, col1, col2, sticky, pad_xy, options = widget_data
        widget_class = widgets[widget_type]
        if parent_id in widget_dictionary.get(key_scrollable_frames, ()):
            scrollable_frame: ScrollableFrame = widget_dictionary[parent_id]
            parent = scrollable_frame.scrollable_frame
        else:
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
        elif widget_type == SCROLLABLE_FRAME:
            if 'frame options' in options:
                del options['frame options']
            widget = widget_class(parent, **options)
            if key_scrollable_frames in widget_dictionary:
                widget_dictionary[key_scrollable_frames].append(widget_id)
            else:
                widget_dictionary[key_scrollable_frames] = [widget_id]
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
    configure_frame_row_col(frame_options_, widget)
    return widget


def configure_frame_row_col(frame_options: dict, widget: ttk.Frame):
    if frame_options != {}:
        rows, weights = frame_options['rows_and_weights']
        for row, weight in zip(rows, weights):
            widget.grid_rowconfigure(row, weight=weight)
        cols, weights = frame_options['cols_and_weights']
        for col, weight in zip(cols, weights):
            widget.grid_columnconfigure(col, weight=weight)
        propagate = frame_options['propagate']
        widget.grid_propagate(propagate)


def add_paned_window(options: dict, parent, widget_class: Type[ttk.Panedwindow], widget_dictionary: dict):
    is_vertical = options['is_vertical']
    frame_ids = options['frame_ids']
    weights = options['weights'] if 'weights' in options else tuple(None for _ in frame_ids)

    frame_options = options.get('frame_options', None)
    scrollables = options.get('scrollable_frame', tuple(False for _ in frame_ids))

    orient = tk.VERTICAL if is_vertical else tk.HORIZONTAL
    paned_window = widget_class(parent, orient=orient)
    for n, (frame_id, weight, scrollable) in enumerate(zip(frame_ids, weights, scrollables)):
        frame = widgets[SCROLLABLE_FRAME if scrollable else FRAME](paned_window, style='a.TFrame')
        configure_frame_row_col_options(frame, frame_options, n)
        widget_dictionary[frame_id] = frame.scrollable_frame if scrollable else frame
        paned_window.add(frame, weight=weight)
    return paned_window


def configure_frame_row_col_options(frame, frame_options, n):
    if frame_options is not None:
        frame_option = frame_options[n]
        configure_frame_row_col(frame_option, frame)
    else:
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)


def set_paned_window_sash_position(paned_window: ttk.Panedwindow, position: int = None):
    if position is not None:
        paned_window.sashpos(0, position)


def add_notebook(options: dict, parent, widget_dictionary: dict) -> ttk.Notebook:
    frame_ids: tuple = options['frame_ids']
    frame_names: tuple = options['frame_names']
    notebook = widgets[NOTEBOOK](parent)

    frame_options = options.get('frame_options', None)
    scrollables = options.get('scrollable_frame', tuple(False for _ in frame_ids))

    for n, (frame_id, frame_name, scrollable) in enumerate(zip(frame_ids, frame_names, scrollables)):
        frame = widgets[SCROLLABLE_FRAME if scrollable else FRAME](notebook)
        configure_frame_row_col_options(frame, frame_options, n)
        notebook.add(frame, text=frame_name)
        widget_dictionary[frame_id] = frame.scrollable_frame if scrollable else frame
    return notebook


def select_note_book_tab(widget: ttk.Notebook, tab_id):
    widget.select(tab_id)


def add_radio_button(options: dict, parent, widget_dictionary: dict) -> ttk.Frame:
    int_var = widgets[INT_VAR]()
    int_var_id = options['int_var_id']
    widget_dictionary[int_var_id] = int_var

    frame_id = options['frame_id']
    vertical: bool = options['is_vertical']
    names: tuple = options['names']

    frame = widgets[FRAME](parent)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    widget_dictionary[frame_id] = frame

    for n, name in enumerate(names):
        rb = widgets[RADIOBUTTON](frame, text=name, variable=int_var, value=n)
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


def bind_widget_entry(callback: Callable, widget):
    type_check = type(widget)
    if type_check == widgets[TREEVIEW]:
        tree_actions.bind_tree_enter(callback, widget)
    else:
        widget.bind(f'<Enter>', lambda e: callback())


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
    elif type_check == widgets[TEXTBOX]:
        widget.bind('<FocusOut>', callback)
    else:
        widget.configure(command=callback)


def unbind_command_from_widget(widget):
    type_check = type(widget)
    if type_check == widgets[TREEVIEW]:
        unbind_tree(widget)


def entry_update(callback: Callable, widget):
    type_check = type(widget)
    if type_check == widgets[ENTRY]:
        w: EntryWithText = widget
        w.bind_update(callback)


def set_foreground_color(widget, color: str):
    widget.configure(foreground=color)


def set_text(widget, text: str):
    widget['text'] = text


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
    elif widget_type == EntryWithText:
        w: EntryWithText = widget
        return w.get_value()
    elif widget_type == widgets[TEXTBOX]:
        return widget.get("1.0", tk.END)
    elif widget_type == widgets[LABEL]:
        return widget['text']
    else:
        try:
            return widget.get()
        except AttributeError:
            pass


def set_combobox_values(widget: ComboBoxWithText, values: tuple):
    widget.set_values(values)


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


def remove_widget(widget: tk.Widget):
    widget.destroy()


def clear_frame(frame: tk.Frame):
    for widget in frame.winfo_children():
        widget.destroy()


def ask_color(title: str):
    return colorchooser.askcolor(title=title)


def get_paned_window_sash_position(paned_window: ttk.Panedwindow) -> int:
    return paned_window.sashpos(0)


def select_folder(initialdir=None):
    user_feedback = filedialog.askdirectory(title='Choose Folder', initialdir=initialdir)
    return None if user_feedback is None else user_feedback


def ask_save_file(initialdir=None, initialfile=''):
    with filedialog.asksaveasfile(title='Save as...', initialdir=initialdir, initialfile=initialfile) as user_feedback:
        return None if user_feedback is None else user_feedback.name


def ask_open_file(initialdir=None):
    with filedialog.askopenfile(title='Select File', initialdir=initialdir) as user_feedback:
        return None if user_feedback is None else user_feedback.name


def ask_yes_no(title, message) -> bool:
    return askyesno(title, message)


def close(widget):
    if type(widget) == widgets[TOPLEVEL]:
        widget.grab_release()  # entries on root will be enabled.

    widget.destroy()


def change_label_text_color(label: tk.Label, color):
    label.configure(foreground=color)


def change_label_font_size(label: tk.Label, size: int, font_name: str = 'Helvetica bold', overstrike=False):
    if size is not None:
        f = (font_name, size)
    else:
        fd = font.nametofont('TkTextFont').actual()
        f = (fd['slant'], fd['size'])

    if overstrike:
        f += ('overstrike',)
    label.config(font=f)


def change_label_image(label: tk.Label, image):
    label.configure(image=image)
    label.image = image


def bind_drag_and_drop_enter(widget: tk.Widget, callback: Callable):
    _bind_dnd('<<DropEnter>>', widget, callback)


def bind_drag_and_drop_leave(widget: tk.Widget, callback: Callable):
    _bind_dnd('<<DropLeave>>', widget, callback)


def bind_drag_and_drop_drop(widget: tk.Widget, callback: Callable):
    _bind_dnd('<<Drop>>', widget, callback)


def _bind_dnd(key: str, widget, callback: Callable):
    if tkinterdnd2_imported:
        widget.drop_target_register('DND_Files')
        widget.dnd_bind(key, lambda e: callback(e))


def highlight_entry(widget: EntryWithText):
    widget.highlight()


def remove_ighlight_entry(widget: EntryWithText):
    widget.remove_highlight()
