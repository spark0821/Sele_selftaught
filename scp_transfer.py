import paramiko

def scp_trans(local_path, remote_path, hostname, port, username, password=None):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh.connect(hostname, port, username, password)

    with paramiko.SFTPClient.from_transport(ssh.get_transport()) as sftp:
        sftp.put(local_path, remote_path)
    print(f"File {local_path} successfully transferred to {username}@{hostname}:{remote_path}")



    ssh.close()


local_file_path = "test/action.txt"

remote_host = "10.0.21.22"
remote_host_port = 22
remote_username = "root"
remote_pwd = "eji65j4"

remote_file_path = "/opt/H3G5/opt/CXL-RESTful-API/testing"

scp_trans(local_file_path, remote_file_path, remote_host, remote_host_port, remote_username, remote_pwd)
