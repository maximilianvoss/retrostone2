#!/usr/bin/env python

import evdev
import uinput
from time import sleep
from evdev import InputDevice, KeyEvent, UInput, AbsInfo, ecodes as e
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector

DZONE = 200 # dead zone applied to joystick (mV)
VREF = 1350 # joystick Vcc (mV)
JOYOFFVAL = 2000 # Value read when joystick is not connected.
JOYSTICKCONNECTED = 0 # 1 if joystick is connected

events = ([
    uinput.BTN_DPAD_UP,
    uinput.BTN_DPAD_DOWN,
    uinput.BTN_DPAD_LEFT,
    uinput.BTN_DPAD_RIGHT,
    uinput.BTN_A,
    uinput.BTN_B,
    #		uinput.BTN_C,
    uinput.BTN_X,
    uinput.BTN_Y,
    #		uinput.BTN_Z,
    uinput.BTN_TL,
    uinput.BTN_TR,
    #		uinput.BTN_THUMBL,
    #		uinput.BTN_THUMBR,
    uinput.BTN_SELECT,
    uinput.BTN_START,
    uinput.BTN_TL2,
    uinput.BTN_TR2,
    uinput.ABS_X + (0,VREF,0,0),
    uinput.ABS_Y + (0,VREF,0,0),
    ])

gamepad = uinput.Device(events,"RetroStone2 Controle",0x00)

gamepad.emit(uinput.ABS_X, VREF/2, syn=False)
gamepad.emit(uinput.ABS_Y, VREF/2)

#--------------- define botoes -----------------
# ---- BRIGHTNESS CONTROL ---------#
button_plus = port.PC18
button_minus = port.PC22

# ---- PLAYER 1 ---------#
bt_up_p1 = port.PH19
bt_down_p1 = port.PH7
bt_left_p1 = port.PH4
bt_right_p1 = port.PH16

bt_l_p1 = port.PH23
bt_x_p1 = port.PH12
bt_y_p1 = port.PH20
bt_r_p1 = port.PH22
bt_b_p1 = port.PH11
bt_a_p1 = port.PH0

bt_select_p1 = port.PH15
bt_start_p1 = port.PH14

bt_left_trigger_p1 = port.PH27
bt_right_trigger_p1 = port.PH26

#optional buttons
bt_c_p1 = port.PH3
bt_z_p1 = port.PH13


#--------------------------------Initialize module. Always called first


gpio.init()
gpio.setcfg(button_plus, gpio.INPUT)
gpio.pullup(button_plus, gpio.PULLUP)

gpio.setcfg(button_minus, gpio.INPUT)
gpio.pullup(button_minus, gpio.PULLUP)

gpio.setcfg(bt_up_p1, gpio.INPUT)
gpio.pullup(bt_up_p1, gpio.PULLUP)

gpio.setcfg(bt_down_p1, gpio.INPUT)
gpio.pullup(bt_down_p1, gpio.PULLUP)

gpio.setcfg(bt_left_p1, gpio.INPUT)
gpio.pullup(bt_left_p1, gpio.PULLUP)

gpio.setcfg(bt_right_p1, gpio.INPUT)
gpio.pullup(bt_right_p1, gpio.PULLUP)


gpio.setcfg(bt_l_p1, gpio.INPUT)
gpio.pullup(bt_l_p1, gpio.PULLUP)

gpio.setcfg(bt_x_p1, gpio.INPUT)
gpio.pullup(bt_x_p1, gpio.PULLUP)

gpio.setcfg(bt_y_p1, gpio.INPUT)
gpio.pullup(bt_y_p1, gpio.PULLUP)

gpio.setcfg(bt_r_p1, gpio.INPUT)
gpio.pullup(bt_r_p1, gpio.PULLUP)

gpio.setcfg(bt_b_p1, gpio.INPUT)
gpio.pullup(bt_b_p1, gpio.PULLUP)

gpio.setcfg(bt_a_p1, gpio.INPUT)
gpio.pullup(bt_a_p1, gpio.PULLUP)

gpio.setcfg(bt_c_p1, gpio.INPUT)
gpio.pullup(bt_c_p1, gpio.PULLUP)

gpio.setcfg(bt_z_p1, gpio.INPUT)
gpio.pullup(bt_z_p1, gpio.PULLUP)

gpio.setcfg(bt_select_p1, gpio.INPUT)
gpio.pullup(bt_select_p1, gpio.PULLUP)

gpio.setcfg(bt_start_p1, gpio.INPUT)
gpio.pullup(bt_start_p1, gpio.PULLUP)

gpio.setcfg(bt_left_trigger_p1, gpio.INPUT)
gpio.pullup(bt_left_trigger_p1, gpio.PULLUP)

gpio.setcfg(bt_right_trigger_p1, gpio.INPUT)
gpio.pullup(bt_right_trigger_p1, gpio.PULLUP)

_bt_up_p1 = False
_bt_down_p1 = False
_bt_left_p1 = False
_bt_right_p1 = False
_bt_a_p1 = False
_bt_b_p1 = False
_bt_x_p1 = False
_bt_y_p1 = False
_bt_c_p1 = False
_bt_z_p1 = False
_bt_l_p1 = False
_bt_r_p1 = False
_bt_select_p1 = False
_bt_start_p1 = False
_bt_left_trigger_p1 = False
_bt_right_trigger_p1 = False


while True:
    #------ brightness control -----------#
    #bt plus =====================
    if gpio.input(button_plus) == 0:
        f=open("/sys/class/backlight/backlight/actual_brightness", "r")
        brightness = int(f.read())
        if brightness < 100:
            brightness = brightness + 1
            f2=open("/sys/class/backlight/backlight/brightness", "w")
            f2.write(str(brightness))
            f2.close()

        f.close()

    #bt minus =====================

    if gpio.input(button_minus) == 0:
        f=open("/sys/class/backlight/backlight/actual_brightness", "r")
        brightness = int(f.read())
        if brightness > 0:
            brightness = brightness - 1
            f2=open("/sys/class/backlight/backlight/brightness", "w")
            f2.write(str(brightness))
            f2.close()

        f.close()

    #------ player 1 -----------#

    ####DIRECTIONS P1 ###########################

    #bt up =====================
    if (not _bt_up_p1) and (gpio.input(bt_up_p1) == 0):
        _bt_up_p1 = True
        gamepad.emit(uinput.BTN_DPAD_UP, 1)
    if (_bt_up_p1) and (gpio.input(bt_up_p1) == 1):
        _bt_up_p1 = False
        gamepad.emit(uinput.BTN_DPAD_UP, 0)
    #bt down =====================
    if (not _bt_down_p1) and (gpio.input(bt_down_p1) == 0):
        _bt_down_p1 = True
        gamepad.emit(uinput.BTN_DPAD_DOWN, 1)
    if (_bt_down_p1) and (gpio.input(bt_down_p1) == 1):
        _bt_down_p1 = False
        gamepad.emit(uinput.BTN_DPAD_DOWN, 0)
    #bt left =====================
    if (not _bt_left_p1) and (gpio.input(bt_left_p1) == 0):
        _bt_left_p1 = True
        gamepad.emit(uinput.BTN_DPAD_LEFT, 1)
    if (_bt_left_p1) and (gpio.input(bt_left_p1) == 1):
        _bt_left_p1 = False
        gamepad.emit(uinput.BTN_DPAD_LEFT, 0)
    #bt right =====================
    if (not _bt_right_p1) and (gpio.input(bt_right_p1) == 0):
        _bt_right_p1 = True
        gamepad.emit(uinput.BTN_DPAD_RIGHT, 1)
    if (_bt_right_p1) and (gpio.input(bt_right_p1) == 1):
        _bt_right_p1 = False
        gamepad.emit(uinput.BTN_DPAD_RIGHT, 0)

    #bt a =====================
    if (not _bt_a_p1) and (gpio.input(bt_a_p1) == 0):
        _bt_a_p1 = True
        gamepad.emit(uinput.BTN_A, 1)
    if (_bt_a_p1) and (gpio.input(bt_a_p1) == 1):
        _bt_a_p1 = False
        gamepad.emit(uinput.BTN_A, 0)
    #bt b =====================

    if (not _bt_b_p1) and (gpio.input(bt_b_p1) == 0):
        _bt_b_p1 = True
        gamepad.emit(uinput.BTN_B, 1)
    if (_bt_b_p1) and (gpio.input(bt_b_p1) == 1):
        _bt_b_p1 = False
        gamepad.emit(uinput.BTN_B, 0)

    #bt X =====================

    if (not _bt_x_p1) and (gpio.input(bt_x_p1) == 0):
        _bt_x_p1 = True
        gamepad.emit(uinput.BTN_X, 1)
    if (_bt_x_p1) and (gpio.input(bt_x_p1) == 1):
        _bt_x_p1 = False
        gamepad.emit(uinput.BTN_X, 0)
    #bt Y =====================

    if (not _bt_y_p1) and (gpio.input(bt_y_p1) == 0):
        _bt_y_p1 = True
        gamepad.emit(uinput.BTN_Y, 1)
    if (_bt_y_p1) and (gpio.input(bt_y_p1) == 1):
        _bt_y_p1 = False
        gamepad.emit(uinput.BTN_Y, 0)

    #bt C =====================

    if (not _bt_c_p1) and (gpio.input(bt_c_p1) == 0):
        _bt_c_p1 = True
        gamepad.emit(uinput.BTN_C, 1)
    if (_bt_c_p1) and (gpio.input(bt_c_p1) == 1):
        _bt_c_p1 = False
        gamepad.emit(uinput.BTN_C, 0)
    #bt Z =====================

    if (not _bt_z_p1) and (gpio.input(bt_z_p1) == 0):
        _bt_z_p1 = True
        gamepad.emit(uinput.BTN_Z, 1)
    if (_bt_z_p1) and (gpio.input(bt_z_p1) == 1):
        _bt_z_p1 = False
        gamepad.emit(uinput.BTN_Z, 0)

    #bt L =====================
    if (not _bt_l_p1) and (gpio.input(bt_l_p1) == 0):
        _bt_l_p1 = True
        gamepad.emit(uinput.BTN_TL, 1)
    if (_bt_l_p1) and (gpio.input(bt_l_p1) == 1):
        _bt_l_p1 = False
        gamepad.emit(uinput.BTN_TL, 0)
    #bt R =====================
    if (not _bt_r_p1) and (gpio.input(bt_r_p1) == 0):
        _bt_r_p1 = True
        gamepad.emit(uinput.BTN_TR, 1)
    if (_bt_r_p1) and (gpio.input(bt_r_p1) == 1):
        _bt_r_p1 = False
        gamepad.emit(uinput.BTN_TR, 0)
    #bt select =====================
    if (not _bt_select_p1) and (gpio.input(bt_select_p1) == 0):
        _bt_select_p1 = True
        gamepad.emit(uinput.BTN_SELECT, 1)
    if (_bt_select_p1) and (gpio.input(bt_select_p1) == 1):
        _bt_select_p1 = False
        gamepad.emit(uinput.BTN_SELECT, 0)
    #bt start =====================
    if (not _bt_start_p1) and (gpio.input(bt_start_p1) == 0):
        _bt_start_p1 = True
        gamepad.emit(uinput.BTN_START, 1)
    if (_bt_start_p1) and (gpio.input(bt_start_p1) == 1):
        _bt_start_p1 = False
        gamepad.emit(uinput.BTN_START, 0)
    #bt L2 =====================
    if (not _bt_left_trigger_p1) and (gpio.input(bt_left_trigger_p1) == 0):
        _bt_left_trigger_p1 = True
        gamepad.emit(uinput.BTN_TL2, 1)
    if (_bt_left_trigger_p1) and (gpio.input(bt_left_trigger_p1) == 1):
        _bt_left_trigger_p1 = False
        gamepad.emit(uinput.BTN_TL2, 0)
    #bt R2 =====================
    if (not _bt_right_trigger_p1) and (gpio.input(bt_right_trigger_p1) == 0):
        _bt_right_trigger_p1 = True
        gamepad.emit(uinput.BTN_TR2, 1)
    if (_bt_right_trigger_p1) and (gpio.input(bt_right_trigger_p1) == 1):
        _bt_right_trigger_p1 = False
        gamepad.emit(uinput.BTN_TR2, 0)
    #joystick =====================

    if (JOYSTICKCONNECTED == 1):
        f3scale=open("/sys/bus/iio/devices/iio:device0/in_voltage3_scale", "r")
        f4scale=open("/sys/bus/iio/devices/iio:device0/in_voltage4_scale", "r")
        f3raw=open("/sys/bus/iio/devices/iio:device0/in_voltage3_raw", "r")
        f4raw=open("/sys/bus/iio/devices/iio:device0/in_voltage4_raw", "r")

        joystick_LR = int(int(f3raw.read())*float(f3scale.read()))
        joystick_UD = int(int(f4raw.read())*float(f4scale.read()))


        if (joystick_LR > (VREF/2 + DZONE)) or (joystick_LR < (VREF/2 - DZONE)):
            if (joystick_LR > VREF):
                if (joystick_LR < JOYOFFVAL):
                    gamepad.emit(uinput.ABS_X, 0)
            else:
                gamepad.emit(uinput.ABS_X, VREF - joystick_LR )
        else:#Center the sticks if within deadzone
            gamepad.emit(uinput.ABS_X, VREF/2)

        if (joystick_UD > (VREF/2 + DZONE)) or (joystick_UD < (VREF/2 - DZONE)):
            if (joystick_UD > VREF):
                if (joystick_UD < JOYOFFVAL):
                    gamepad.emit(uinput.ABS_Y, VREF )
            else:
                gamepad.emit(uinput.ABS_Y, joystick_UD )
        else:#Center the sticks if within deadzone
            gamepad.emit(uinput.ABS_Y, VREF/2)

        f3raw.close()
        f4raw.close()
        f3scale.close()
        f4scale.close()

    sleep(.02)