#    ____  ____________    ______
#   / __ \/_  __/  _/ /   / ____/
#  / / / / / /  / // /   / __/   
# / /_/ / / / _/ // /___/ /___   
# \___\_\/_/ /___/_____/_____/   

import os
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#---------------#
#   SUPER KEY   #
#---------------#
mod = "mod4"

#---------------#
#   KEYBINDINGS #
#---------------#

keys = [

    #---    Move windows    ---#
    Key([mod], "Left", lazy.layout.shuffle_left()),
    Key([mod], "Right", lazy.layout.shuffle_right()),
    Key([mod], "Down", lazy.layout.shuffle_down()),
    Key([mod], "Up", lazy.layout.shuffle_up()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    

    #---    Browser     ---#
    Key([mod], "f", lazy.spawn("firefox")),

    #---    Terminal    ---#
    Key([mod], "Return", lazy.spawn("kitty")),
    
    #---    File manager    ---#
    Key([mod], "m", lazy.spawn("thunar")),

    #---    Launcher    ---#
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    #---    Toogle layout   ---#
    Key([mod], "Tab", lazy.next_layout()),

    #---    Kill window     ---#
    Key([mod], "w", lazy.window.kill()),

    #---    Reload Qtile    ---#
    Key([mod, "shift"], "r", lazy.reload_config()),

    #---    Exit Qtile      ---#
    Key([mod, "shift"], "e", lazy.shutdown()),

    #---    Brightness up   ---#
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),

    #---    Brightness down ---#
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    
    #---    Sleep machine ---#
    Key([], "XF86Sleep", lazy.spawn("systemctl suspend")),
    
    #---    Volume up   ---#
    Key(
            [], "XF86AudioRaiseVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")
    ),

    #---    Volume down ---#
    Key(
            [], "XF86AudioLowerVolume",
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")
    ),

    #---    Mute volume ---#
    Key(
            [], "XF86AudioMute",
            lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),

    #---    Print screen    ---#
    Key([], "Print", lazy.spawn("flameshot gui")),

    Key([mod], "d", lazy.spawn("python ~/.config/qtile/scripts/show_desktop.py"), desc="Mostrar el escritorio"),
]

#---------------#
#   WORKSPACES  #
#---------------#

groups = [Group(i) for i in [
    "   ",
]]

#---------------------------#
#   WINDOW STYLE IN LAYOUTS #
#---------------------------#

layouts = [
    layout.MonadTall(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.Max(),
    layout.Bsp(border_focus="#9ccfd8", border_normal="#31748f",
               border_width=1, margin=8),
    layout.MonadWide(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.RatioTile(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    # layout.Matrix(),
]

#-----#
# BAR #
#-----#

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=18,
    padding=4,
    
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=0,
                    rounded=True,
                    borderwidth=5
                ),
                widget.Image(
                    filename="~/.config/qtile/Archlinux-icon.svg",
                    scale="False"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    active="#ffffff",
                    rounded=True,
                    highlight_color="#232136",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#ffffff",
                    markup=True,
                    font="UbuntuMono Nerd Font",
                    fontsize=15,
                    max_chars=0,
                    padding=800
                ),
                widget.TextBox(
                    text='',
                    background="#232136",
                    foreground="#f6c177",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#f6c177",
                    foreground="#191724",
                    padding=7
                ),
                widget.CurrentLayout(
                    background="#f6c177",
                    foreground="#191724"
                ),
                widget.TextBox(
                    text='',
                    background="#f6c177",
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background="#e0def4",
                    foreground="191724",
                    format="󰘚 {load_percent}%"
                ),
                widget.TextBox(
                    text='',
                    foreground="#eb6f92",
                    background="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background="#eb6f92",
                    foreground="#191724",
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#eb6f92",
                    foreground="#9ccfd8",
                    padding=0,
                    fontsize=42
                ),
                widget.Net(
                    interface="enp1s0",
                    format=" {interface}: {down} ↓↑ {up}",
                    background="#9ccfd8",
                    foreground="#191724",
                    update_interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#9ccfd8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M - %d/%m/%Y",
                    update_interval=60.0
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#232136",
                    padding=0,
                    fontsize=42
                ),
                widget.Volume(
                    foreground="#e0def4",
                    fmt=" {}"
                ),
                widget.Systray(),
            ],
            25,
            background="#232136",
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#ffffff",
                    rounded=False,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="UbuntuMono Nerd Font",
                    fontsize=15,
                ),
                widget.TextBox(
                    text='',
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#e0def4",
                    foreground="#191724",
                    padding=2
                ),
                widget.CheckUpdates(
                    update_interval=18000,
                    display_format="{updates}",
                    colour_have_updates="#191724",
                    background="#e0def8"
                ),
                widget.TextBox(
                    text='',
                    background="#e0def8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M",
                    update_interval=60.0
                ),
            ],
            25,
            background="#232136",
        ),
    ),

]

#-----------------------#
#   FLOATING WINDOWS    #
#-----------------------#

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus="#9ccfd8",
    border_normal="#31748f"
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

#---------------#
#   AUTOSTART   #
#---------------#


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"