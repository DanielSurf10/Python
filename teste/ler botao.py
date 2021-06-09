from win32gui import GetWindowText, GetForegroundWindow
from pynput.keyboard import Key, Listener

current_window = (GetWindowText(GetForegroundWindow()))
desired_window_name = (GetWindowText(GetForegroundWindow()))
def on_press(key):
    print('{0} pressed'.format(
        key))
def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
         return False

#Infinite loops are dangerous.
while True: #Don't rely on this line of code too much and make sure to adapt this to your project.
    # if current_window == desired_window_name:

       with Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
            # current_window = GetWindowText(GetForegroundWindow())
            listener.join()
