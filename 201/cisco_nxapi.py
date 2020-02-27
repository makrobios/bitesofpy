import requests


def nxapi_show_version():
    url =  """http://sbx-nxos-mgmt.cisco.com"""
    switchuser = """admin"""
    switchpassword = """Admin_1234"""

    http_headers = {"username": switchuser, "password": switchpassword}
    payload = [{"jsonrpc": "2.0",
                "method": """cli_ascii""",
                "params": {"cmd": """show version""",
                           "version": 1}, "id": 1}]
    # 1. use requests to post to the switch
    response = requests.post(url, params=payload, verify=False, headers=http_headers)

    # 2. retrieve and return the kickstart_ver_str from the response
    # example response json:
    # {'result': {'body': {'bios_cmpl_time': '05/17/2018',
    #                      'kick_tmstmp': '07/11/2018 00:01:44',
    #                      'kickstart_ver_str': '9.2(1)',
    #                      ...
    #                      }
    #             }
    # }
    version = response.json()['result']['body']['kickstart_ver_str']
    return version


if __name__ == '__main__':
    result = nxapi_show_version()
    print(result)