'''Functions with outputs'''

def format_name(f_name, l_name):
    f_name_title  = f_name.title()
    l_namez_title = l_name.title()
    return (f_name_title, l_namez_title )

f_name, l_name = format_name('KIM', 'lee')

print(format_name('KEN', 'WeiTh'))