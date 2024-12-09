# .config/qtile/scripts/show_desktop.py

from libqtile.command.client import CommandClient

c = CommandClient()
windows = c.windows()
minimized = [win for win in windows if win['minimized']]
if minimized:
    for win in minimized:
        c.window[win['id']].toggle_minimize()
else:
    for win in windows:
        c.window[win['id']].toggle_minimize()
