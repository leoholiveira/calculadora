import flet as ft
from flet import colors
from decimal import Decimal

buttons = [
  {'operator': 'AC', 'source': colors.BLACK, 'background': colors.BLUE_GREY_100},
  {'operator': '±', 'source': colors.BLACK, 'background': colors.BLUE_GREY_100},
  {'operator': '%', 'source': colors.BLACK, 'background': colors.BLUE_GREY_100},
  {'operator': '/', 'source': colors.WHITE, 'background': colors.ORANGE},
  {'operator': '7', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '8', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '9', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '*', 'source': colors.WHITE, 'background': colors.ORANGE},
  {'operator': '4', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '5', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '6', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '-', 'source': colors.WHITE, 'background': colors.ORANGE},
  {'operator': '1', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '2', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '3', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '+', 'source': colors.WHITE, 'background': colors.ORANGE},
  {'operator': '0', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '.', 'source': colors.WHITE, 'background': colors.WHITE24},
  {'operator': '=', 'source': colors.WHITE, 'background': colors.ORANGE}
]

def main(page: ft.Page):

  # app config
  page.title = 'Calculadora'
  page.window_resizable = False
  page.window_width = 250
  page.window_height = 380
  page.bgcolor = '#000'
  page.window_always_on_top = True

  result = ft.Text(value = '0', color = colors.WHITE, size=20)

  def calculate(operator, value_at):
    try:
      value = eval(value_at)

      if operator == '%':
        value /= 100
      elif operator == '±':
        value = -value

      digits = min(abs(Decimal(value).as_tuple().exponent), 5)
      return format(value, f'.{digits}f')
    except:
      return 'Error'

  def select(e):
    value_at = result.value if result.value not in ('0', 'Error') else ''
    value = e.control.content.value

    if value.isdigit():
      value = value_at + value
    elif value == 'AC':
      value = '0'
    else:
      if value_at and value_at[-1] in ('/','*','-','+','.'):
        value_at = value_at[:-1]

      value = value_at + value

      if value[-1] in ('=','%','±'):
        value = calculate(operator = value[-1], value_at = value_at)

    result.value = value
    result.update()

  display = ft.Row(
    width=250,
    controls=[result],
    alignment = 'end',
  )

  btn = [ft.Container(
    content = ft.Text(value = btn['operator'], color = btn['source']),
    width=50,
    height=50,
    bgcolor=btn['background'],
    border_radius=100,
    alignment=ft.alignment.center,
    on_click=select
  ) for btn in buttons]

  keyboard = ft.Row(
    width=250,
    wrap=True,
    controls=btn,
    alignment='end'
  )

  page.add(display, keyboard)

ft.app(target = main)