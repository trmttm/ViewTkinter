from typing import Callable
from typing import Tuple
from typing import Union

from interface_view import ViewABC

from . import TkImplementations as TkImpl


class View(ViewABC):

    def __init__(self, master=None, width=None, height=None, fullscreen=False):
        is_entry_point = master is None
        root = TkImpl.instantiate_root(width, height, fullscreen) if is_entry_point else master

        self._root = root
        self._is_entry_point_of_application = is_entry_point
        self._widget_dictionary = {'root': root}
        self._canvas_id = None
        self._status_bar_id = None
        self._tree_id = None

        self._view_state = {}

    def attach_to_event_upon_closing(self, observer):
        self._root.protocol("WM_DELETE_WINDOW", observer)

    # 1) Canvas related methods
    @property
    def current_canvas(self):
        return self._canvas_id

    def switch_canvas(self, canvas_id):
        self._canvas_id = canvas_id

    def get_canvas_width(self) -> float:
        canvas = self.get_widget(self._canvas_id)
        return TkImpl.get_canvas_width(canvas)

    def get_canvas_height(self) -> float:
        canvas = self.get_widget(self._canvas_id)
        return TkImpl.get_canvas_height(canvas)

    def bind_change_canvas_size(self, call_back: Callable, canvas_id=None):
        canvas = self.get_widget(self._canvas_id if canvas_id is None else canvas_id)
        TkImpl.bind_change_canvas_size(call_back, canvas)

    def clear_canvas_shapes_by_tag(self, tag):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.clear_shapes_by_tag(canvas, tag)

    def add_text_box(self, view_model: list):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.add_text_box(canvas, view_model)
        TkImpl.update_canvas_scroll_region(canvas)

    def add_rectangle(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.add_rectangle(canvas, view_model)
        TkImpl.update_canvas_scroll_region(canvas)

    def add_text(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.add_text(canvas, view_model)
        TkImpl.update_canvas_scroll_region(canvas)

    def remove_shape(self, view_model: list):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.remove_shapes(canvas, view_model)
        TkImpl.update_canvas_scroll_region(canvas)

    def connect_shapes(self, view_model: list):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.connect_shapes(canvas, view_model)

    def move_shapes(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.move_shapes(canvas, view_model)
        TkImpl.update_canvas_scroll_region(canvas)

    def move_lines(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_coordinates(canvas, view_model)
        TkImpl.update_canvas_scroll_region(canvas)

    def add_widgets(self, view_model: Union[list, tuple]):
        TkImpl.add_widgets(self._widget_dictionary, view_model)

    def highlight_shapes(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.highlight_shapes(canvas, view_model)

    def draw_rectangle(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.draw_rectangle(canvas, view_model)

    def set_border_color(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_border_color(canvas, view_model)

    def set_text_value(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_text_value(canvas, view_model)

    def set_text_color(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_text_color(canvas, view_model)

    def set_font_size(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_font_size(canvas, view_model)

    def set_border_width(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_border_width(canvas, view_model)

    def set_line_width(self, view_model: dict):
        self.set_border_width(view_model)

    def set_line_arrow(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_line_arrow(canvas, view_model)

    def set_fill_color(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.set_fill_color(canvas, view_model)

    def add_line(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.add_line(canvas, view_model)

    def draw_line(self, view_model: dict):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.draw_line(canvas, view_model)

    def clear_canvas(self, _: dict = None):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.clear_canvas(canvas)
        TkImpl.update_canvas_scroll_region(canvas)

    def scroll_canvas(self, x, y):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.scroll_canvas(canvas, x, y)

    def save_canvas_as_an_image(self, file_name):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.save_canvas(canvas, file_name)

    # 2) Mouse related methods
    def get_mouse_coordinates_captured(self, event) -> Tuple[int, int]:
        return TkImpl.get_mouse_coordinates(event)

    def get_mouse_canvas_coordinate(self) -> tuple:
        canvas = self.get_widget(self._canvas_id)
        return TkImpl.get_mouse_canvas_coordinates(canvas)

    # 3) General methods
    def set_foreground_color(self, widget_id, color: str):
        widget = self._widget_dictionary.get(widget_id, None)
        if widget:
            TkImpl.set_foreground_color(widget, color)

    def set_text(self, widget_id, text: str):
        widget = self._widget_dictionary.get(widget_id, None)
        if widget is not None:
            TkImpl.set_text(widget, text)

    def update(self):
        self._root.update()

    def widget_exists(self, widget_id) -> bool:
        return widget_id in self._widget_dictionary

    def remove_widget(self, widget_id):
        if widget_id in self._widget_dictionary:
            widget = self._widget_dictionary[widget_id]
            TkImpl.remove_widget(widget)
            del self._widget_dictionary[widget_id]

    def clear_frame(self, frame_id):
        if frame_id in self._widget_dictionary:
            frame = self._widget_dictionary[frame_id]
            TkImpl.clear_frame(frame)

    @property
    def focused_widget(self) -> str:
        dictionary = self._widget_dictionary
        widgets = tuple(id(v) for v in dictionary.values())
        widget_ids = dictionary.keys()

        focused_widget = id(TkImpl.get_focused_widget(self._root))
        widget_id = dict(zip(widgets, widget_ids)).get(focused_widget, '')
        return widget_id

    def set_title(self, title: str):
        TkImpl.set_title(self._root, title)

    def change_window_size(self, width=600, height=900):
        self._root.geometry(f'{width}x{height}')

    def set_exception_catcher(self, callback: Callable):
        TkImpl.set_exception_catcher(callback)

    def get_widget(self, widget_id):
        return self._widget_dictionary.get(widget_id, None)

    def get_value(self, widget_id):
        widget = self.get_widget(widget_id)
        return TkImpl.get_widget_value(widget)

    def set_combobox_values(self, widget_id, values: tuple):
        widget = self.get_widget(widget_id)
        TkImpl.set_combobox_values(widget, values)

    def set_values(self, widget_ids: tuple, values: tuple):
        for widget_id, value in zip(widget_ids, values):
            self.set_value(widget_id, value)

    def set_value(self, widget_id, value):
        widget = self.get_widget(widget_id)
        TkImpl.set_widget_value(widget, value)

    def focus(self, widget_id, **kwargs):
        TkImpl.focus(self._widget_dictionary[widget_id], **kwargs)

    def launch_app(self):
        if self._is_entry_point_of_application:
            self._root.mainloop()

    def bind_widget_entry(self, widget_id, command):
        widget = self.get_widget(widget_id)
        TkImpl.bind_widget_entry(command, widget)

    def bind_command_to_widget(self, widget_id, command):
        widget = self.get_widget(widget_id)
        TkImpl.bind_command_to_widget(command, widget)

    def unbind_command_from_widget(self, widget_id):
        widget = self.get_widget(widget_id)
        TkImpl.unbind_command_from_widget(widget)

    def bind_entry_update(self, entry_id, command):
        widget = self.get_widget(entry_id)
        TkImpl.entry_update(command, widget)

    def update_menu_bar(self, menu_bar_model: dict, toplevel_id=None):
        top_level = self.get_widget(toplevel_id)
        widget = top_level if top_level is not None else self._root
        TkImpl.update_menu_bar(widget, menu_bar_model)

    def switch_status_bar(self, status_bar_id):
        self._status_bar_id = status_bar_id

    def update_status_bar(self, view_model: dict):
        label_widget = self.get_widget(self._status_bar_id)
        TkImpl.update_status_bar(label_widget, view_model)

    def switch_frame(self, widget_id):
        frame = self.get_widget(widget_id)
        TkImpl.switch_frame(frame)

    def close(self, widget_id):
        widget = self._widget_dictionary[widget_id]
        TkImpl.close(widget)

    def quit(self):
        self.close('root')

    def get_mid_y_coordinates_of_all_rectangles_on_canvas(self):
        canvas = self.get_widget(self._canvas_id)
        return TkImpl.get_mid_y_coordinates_of_all_rectangles_on_canvas(canvas)

    def move_item_vertically_within_range(self, item, delta_x, delta_y, y_range: tuple):
        canvas = self.get_widget(self._canvas_id)
        TkImpl.move_item_vertically_within_range(canvas, item, delta_x, delta_y, y_range)

    def get_clicked_rectangle(self):
        canvas = self.get_widget(self._canvas_id)
        return TkImpl.get_clicked_rectangle(canvas)

    @staticmethod
    def ask_color(title='Choose color') -> str:
        return TkImpl.ask_color(title)[1]

    def bind_upon_drag_and_drop_enter(self, widget_id, callback: Callable):
        widget = self._widget_dictionary[widget_id]
        TkImpl.bind_drag_and_drop_enter(widget, callback)

    def bind_upon_drag_and_drop_leave(self, widget_id, callback: Callable):
        widget = self._widget_dictionary[widget_id]
        TkImpl.bind_drag_and_drop_leave(widget, callback)

    def bind_upon_drag_and_drop_drop(self, widget_id, callback: Callable):
        widget = self._widget_dictionary[widget_id]
        TkImpl.bind_drag_and_drop_drop(widget, callback)

    # 4) Tree related methods
    @property
    def current_tree(self):
        return self._tree_id

    def set_tree_headings(self, tree_id: str, headings: Tuple[str, ...]):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.set_tree_headings(headings, tree)

    def get_all_tree_values(self, tree_id=None):
        if tree_id is not None:
            tree = self.get_widget(tree_id)
            return TkImpl.get_all_tree_values(tree)
        elif self._tree_id is not None:
            tree = self.get_widget(self._tree_id)
            return TkImpl.get_all_tree_values(tree)

    def switch_tree(self, tree_id):
        self._tree_id = tree_id

    def update_tree(self, view_model):
        if self._tree_id is not None:
            tree = self.get_widget(self._tree_id)
            TkImpl.update_tree(tree, view_model)

    def tree_focused_values(self, tree_id=None) -> tuple:
        tree = self.get_widget(tree_id or self._tree_id)
        return TkImpl.tree_focused_values(tree)

    def tree_selected_values(self, tree_id=None) -> tuple:
        tree = self.get_widget(tree_id or self._tree_id)
        return TkImpl.tree_selected_values(tree)

    def get_selected_tree_item_indexes(self, tree_id=None) -> tuple:
        tree = self.get_widget(tree_id or self._tree_id)
        return TkImpl.get_selected_tree_item_orders(tree)

    def select_multiple_tree_items(self, tree_id=None, indexes=()):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.select_multiple_tree_items(tree, indexes)

    def tree_number_of_items(self, tree_id=None) -> int:
        tree = self.get_widget(tree_id or self._tree_id)
        return TkImpl.tree_number_of_items(tree)

    def select_tree_top_items_after_deleting_items(self, indexes: tuple, tree_id=None):
        if indexes:
            n = self.tree_number_of_items(tree_id)
            max_index = n - 1
            if n > 0:
                select_next = min(indexes[0], max_index)
                self.select_multiple_tree_items(tree_id, (select_next,))

    def bind_tree_left_click(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_left_click(command, tree)

    def bind_tree_right_click(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_right_click(command, tree)

    def bind_tree_middle_click(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_middle_click(command, tree)

    def bind_tree_left_click_release(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_left_click_release(command, tree)

    def bind_tree_right_click_release(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_right_click_release(command, tree)

    def bind_tree_middle_click_release(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_middle_click_release(command, tree)

    def bind_tree_enter(self, command: Callable, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.bind_tree_enter(command, tree)

    def deselect_tree_items(self, tree_id=None):
        tree = self.get_widget(tree_id or self._tree_id)
        TkImpl.deselect_tree_items(tree)

    def change_label_text_color(self, label_id, color):
        label = self.get_widget(label_id)
        TkImpl.change_label_text_color(label, color)

    # Disk IO
    def select_folder(self, initialdir=None):
        return TkImpl.select_folder(initialdir)

    def select_save_file(self, initialdir=None, initialfile=''):
        return TkImpl.ask_save_file(initialdir, initialfile)

    def select_open_file(self, initialdir=None):
        return TkImpl.ask_open_file(initialdir)

    # NoteBook

    def select_note_book_tab(self, widget_id, tab_id):
        widget = self.get_widget(widget_id)
        TkImpl.select_note_book_tab(widget, tab_id)

    # User Input
    def ask_yes_no(self, title, message) -> bool:
        return TkImpl.ask_yes_no(title, message)

    # Keyboard Shortcut
    def set_keyboard_shortcut_handler_to_root(self, keyboard_shortcut_handler: Callable):
        TkImpl.bind_keyboard_shortcut(self._root, keyboard_shortcut_handler)

    def set_keyboard_shortcut_handler(self, widget_id, keyboard_shortcut_handler: Callable):
        widget = self.get_widget(widget_id)
        TkImpl.bind_keyboard_shortcut(widget, keyboard_shortcut_handler)

    def set_paned_window_sash_position(self, paned_window_id, new_position: int):
        widget = self.get_widget(paned_window_id or self._tree_id)
        TkImpl.set_paned_window_sash_position(widget, new_position)

    def get_paned_window_sash_position(self, paned_window_id) -> int:
        widget = self.get_widget(paned_window_id or self._tree_id)
        return TkImpl.get_paned_window_sash_position(widget)
