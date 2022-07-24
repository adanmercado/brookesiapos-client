import re, os, subprocess, argparse

def run():
    args_parser = argparse.ArgumentParser(prog='ui-to-py', description='Convert UI file to PY')
    args_parser.add_argument('--input', type=str, help='Input file (.ui)', required=True)
    args_parser.add_argument('--output', type=str, help='Output file (.py)', required=True)
    args_parser.add_argument('--classname', type=str, help='Class name')

    args = args_parser.parse_args()

    process = subprocess.Popen(['pyside6-uic', args.input, '-o', args.output], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.communicate()

    if process.poll() == 0:
        with open(os.path.abspath(args.output), 'r') as file:
            data = file.read()

        if data:
            if args.classname:
                data = re.sub(r'(Ui_)(\w+)', args.classname, data, flags=re.M)
            else:
                data = re.sub(r'(Ui_)(\w+)', lambda x: f'{x.group(2).capitalize()}_UI', data, flags=re.M)

            data = re.sub('[..\/]+/qrc', 'qrc', data, flags=re.M)
            with open(os.path.abspath(args.output), 'w') as file:
                file.write(data)

run()