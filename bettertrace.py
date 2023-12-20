import argparse , requests

from prompt import RavePrompt as prompt

EMPTY = ''

parser = argparse.ArgumentParser(

    prog = 'Bettertrace IP tracer',
    
    description = 'Better IP tracer'
)

parser.add_argument('-i' , '--ip' , help = 'IP to trace')


args = parser.parse_args()

ip = args.ip.strip()


if ip == EMPTY:

    prompt.print_mult('Provide a valid ip.')

    exit(0)



def get_ip_info(ip):

    return requests.post('https://ipwhois.app/json/%s' % ip).json()


info : dict[str,str] = get_ip_info(ip)

beautiful = {key.capitalize().replace('_' , ' ') : value for key , value in info.items()}

prompt.vert (
    'IP Info',
    **beautiful
)

