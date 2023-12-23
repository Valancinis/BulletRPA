import flet as ft
import threading


class ScrollHandler:
    def __init__(self, column, controls):
        self.column = column
        self.controls = controls
        self.counter = 0
        self.sem = threading.Semaphore()

    def on_scroll(self, e: ft.OnScrollEvent):
        if e.pixels >= e.max_scroll_extent - 100:
            if self.sem.acquire(blocking=False):
                try:
                    for _ in range(10):
                        self.column.controls.append(self.controls)
                        self.counter += 1
                    self.column.update()
                finally:
                    self.sem.release()
