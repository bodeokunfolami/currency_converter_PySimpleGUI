import PySimpleGUI as sg

font = ('Arial', 18)

sg.theme('Reddit')

currency_list = ['NGN', 'USD']
EXCHANGE = {
    'NGN': {
        'USD': (1 / 750),
        'NGN': 1
    },
    'USD': {
        'NGN': 750,
        'USD': 1
    }
}

layout = [
    [sg.Text('Enter Amount')],
    [sg.Input('', key='-amount-')],
    [sg.Text('From', expand_x=True), sg.Text('To', expand_x=True)],
    [
        sg.Combo(values=currency_list, default_value='NGN', key='-from-', expand_x=True),
        sg.Combo(values=currency_list, default_value='USD', key='-to-', expand_x=True),
    ],
    [sg.Text('Exchange')],
    [sg.Input('', key='-output-')],
    [sg.Text('$1 = 750')],
    [sg.Button('Convert', key='-convert-', expand_x=True, pad=(0, 10))]
]

window = sg.Window('Currency Converter', layout, font=font)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-convert-':
        _from = values['-from-']
        to = values['-to-']
        rate = EXCHANGE[_from][to]
        amount = values['-amount-']
        if amount:
            amount = float(amount)
            result = round(amount * rate, 2)
            window['-output-'].update(f'{result:,}')
window.close()