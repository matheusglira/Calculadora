import PySimpleGUI as sg

bw = {'size': (7, 2), 'font': ('Franklin Gothic Book', 24), 'button_color': ('black', '#F8F8F8')}
bt = {'size': (7, 2), 'font': ('Franklin Gothic Book', 24), 'button_color': ('black', '#F1EABC')}
bo = {'size': (15, 2), 'font': ('Franklin Gothic Book', 24), 'button_color': ('black', '#ECA527'), 'focus': True}

layout = [
    [sg.Text('Calculadora', size=(50, 1), justification='right', background_color='#272533',
             text_color='white', font=('Franklin Gothic Book', 14, 'bold'))],
    [sg.Text('0.0000', size=(18, 1), justification='right', background_color='black', text_color='red',
             font=('Digital-7', 48), relief='sunken', key='DISPLAY')],
    [sg.Button('C', **bt), sg.Button('CE', **bt), sg.Button('%', **bt), sg.Button('/', **bt)],
    [sg.Button('7', **bw), sg.Button('8', **bw), sg.Button('9', **bw), sg.Button('*', **bt)],
    [sg.Button('4', **bw), sg.Button('5', **bw), sg.Button('6', **bw), sg.Button('-', **bt)],
    [sg.Button('1', **bw), sg.Button('2', **bw), sg.Button('3', **bw), sg.Button('+', **bt)],
    [sg.Button('0', **bw), sg.Button('.', **bw), sg.Button('=', **bo, bind_return_key=True)],
]

window = sg.Window('Calculadora', layout=layout, background_color='#272533', size=(580, 660),
                   return_keyboard_events=True)

var = {'primeiros': [], 'ultimos': [], 'decimal': False, 'x_val': 0.0, 'y_val': 0.0, 'resultado': 0.0, 'operador': ''}


def formatar_numero():
    return float(''.join(var['primeiros']).replace(',', '') + '.' + ''.join(var['ultimos']))


def atualizar_display(valor):
    try:
        window['DISPLAY'].update(value='{:,.4f}'.format(valor))
    except:
        window['DISPLAY'].update(value=valor)


def click_numero(event):
    global var
    if var['decimal']:
        var['ultimos'].append(event)
    else:
        var['primeiros'].append(event)
    atualizar_display(formatar_numero())


def limpar():
    global var
    var['primeiros'].clear()
    var['ultimos'].clear()
    var['decimal'] = False


def operador(event):
    global var
    var['operador'] = event
    try:
        var['x_val'] = formatar_numero()
    except:
        var['x_val'] = var['resultado']
    limpar()


def calcular():
    global var
    try:
        var['y_val'] = formatar_numero()
    except ValueError:
        var['x_val'] = var['resultado']
    try:
        var['resultado'] = eval(str(var['x_val']) + var['operador'] + str(var['y_val']))
        atualizar_display(var['resultado'])
        limpar()
    except:
        atualizar_display("ERROR! DIV/0")
        limpar()


while True:
    event, values = window.read()
    if event is None:
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        click_numero(event)
    if event in ['C', 'CE']:
        limpar()
        atualizar_display(0.0)
        var['resultado'] = 0.0
    if event in ['+', '-', '/', '*']:
        operador(event)
    if event == '=':
        calcular()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        atualizar_display(var['result'] / 100.0)
