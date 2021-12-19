import pygame

import win32api
import win32gui
import win32con

import tkinter.simpledialog
import tkinter

root = tkinter.Tk()
root.withdraw()

pygame.init()
window = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h), 1)


transparency_color = (1,2,3)
# Set transparency color.


#REMOVE QUOTES TO MAKE TRANSPARENT
'''
hwnd = pygame.display.get_wm_info()["window"]
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency_color), 0, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
'''

development_mouse_pos = [[0,0], [0,0]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                development_mouse_pos[0] = list(pygame.mouse.get_pos())
            if event.key == pygame.K_f:
                development_mouse_pos[1] = list(pygame.mouse.get_pos())
                print("LEFT TOP WIDTH HEIGHT: ", development_mouse_pos[0][0], " " , development_mouse_pos[0][1], " ", development_mouse_pos[1][0]-development_mouse_pos[0][0], " ", development_mouse_pos[1][1] - development_mouse_pos[0][1])
            if event.key == pygame.K_q:
                exit()


    window.fill(transparency_color)
    pygame.display.update()