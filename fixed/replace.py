import os

RootPath = os.path.dirname(os.path.abspath(__file__))
Conffileloc = RootPath + "\Core\Inc\stm32g0xx_hal_conf.h"


def ReadAllLines(filename):
    lines = None
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def replaceline(lines, orignalline, replacewith):
    if orignalline in lines:
        lines[lines.index(orignalline)] = replacewith
        return lines
    else:
        return None


def WriteAllLines(filename, lines):
    with open(filename, 'w') as f:
        return f.writelines(lines)


confgfilelines = ReadAllLines(Conffileloc)

confgfilelines1 = replaceline(confgfilelines, "#define USE_HAL_TIM_REGISTER_CALLBACKS    0u\n",
                             "#define USE_HAL_TIM_REGISTER_CALLBACKS    1u\n")
confgfilelines2 = replaceline(confgfilelines, "#define USE_HAL_UART_REGISTER_CALLBACKS    0u\n",
                             "#define USE_HAL_UART_REGISTER_CALLBACKS    1u\n")
confgfilelines3 = replaceline(confgfilelines, "#define USE_HAL_USART_REGISTER_CALLBACKS    0u\n",
                             "#define USE_HAL_USART_REGISTER_CALLBACKS    1u\n")

if confgfilelines1 is not None or \
    confgfilelines2 is not None or \
        confgfilelines3 is not None:
    WriteAllLines(Conffileloc, confgfilelines)