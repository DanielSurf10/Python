from time import sleep
from win32gui import GetWindowText, GetForegroundWindow

current_window = (GetWindowText(GetForegroundWindow()))
desired_window_name = GetWindowText(GetForegroundWindow())

print(current_window)
print(desired_window_name)

c = 0

while True:
    print(GetWindowText(GetForegroundWindow()))
    sleep(1)

# while True:
#     current_window = GetWindowText(GetForegroundWindow())
#     if current_window == desired_window_name:
#         print(c)
#         c += 1
