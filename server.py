import socket
import time

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999)) # Replace with your Server Computer IP
    server_socket.listen(1)

    print("Server listening on port 9999...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        handle_client(client_socket)
print("Welcome To Rishi Anydesk BY Rishi Rao")
def handle_client(client_socket):
    while True:
        command = input("Enter command Sir : ")
        client_socket.send(command.encode())

        if command.lower() == 'exit':
            break
        elif command.lower() == 'help':
            display_help()

        response = client_socket.recv(1024).decode()
        print(f"Response from client: {response}")

def display_help():
    print("Available commands:")
    print("- 'open website {url}': Open the specified website in the client's browser.")
    print("- 'custom {your command}': Execute a custom command on the client's machine.")
    print("- 'type {text}': Simulate typing the specified text using PyAutoGUI.")
    print("- 'shortcut {keys}': Simulate pressing the specified shortcut keys using PyAutoGUI.")
    print("- 'open app {app_name}': Open a specific application on the client's machine.")
    print("- 'press key {key_name}': Simulate pressing the specified key using PyAutoGUI.")
    print("- 'screenshot': Capture a screenshot on the client's machine.")
    print("- 'upload file {file_path}': Upload a file to the client's machine.")
    print("- 'download file {file_path}': Download a file from the client's machine.")
    print("- 'system info': Retrieve system information from the client's machine.")
    print("- 'process list': List running processes on the client's machine.")
    print("- 'terminate process {process_name}': Terminate a specified process on the client's machine.")
    print("- 'shutdown': Shutdown the client's machine.")
    print("- 'restart': Restart the client's machine.")
    print("- 'log off': Log off the current user on the client's machine.")
    print("- 'clipboard get': Retrieve the current clipboard data from the client's machine.")
    print("- 'clipboard set {text_to_copy}': Set the clipboard data on the client's machine.")
    print("- 'help': Display this help message.")
    print("- 'exit': Exit the server.")

if __name__ == "__main__":
    start_server()
