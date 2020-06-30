def my_print(txt):
    print(txt)

msg_template = """ Hello {name},
Thank you for joining {website}, we are very
happay to have you with us.
"""

def format_msg(my_name='shakib', my_website='shakib.com'):
    my_msg = msg_template.format(name=my_name, website = my_website)
    
    return my_msg

