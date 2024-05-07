"""
ST/SST Automation for SecureZone Migration
Randy Bitts, Amdocs SA, RAB Consulting
Coding Started 05/06/2024
"""

import os
import sys
import shutil
import time
from shutil import Error, ignore_patterns
import itertools
from termcolor import colored
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import codecs
import json
import glob

# # Code Share Locations
# st_path = rf"\\gsm1900.org\dfsroot\AS\amdocs_code_share\ST_SST\Samson\VST_ST_"
# sst_path = rf"\\gsm1900.org\dfsroot\AS\amdocs_code_share\ST_SST\Samson\VST_SST_"
# other_path = rf"\\gsm1900.org\dfsroot\AS\amdocs_code_share\ST_SST\Samson\VST_"
#
cc_version = "261200"
server_version = "261200"
server_list_2019 = ["ipolwxsam00001", "ipolwxsam00002"]
for server in server_list_2019:
    server_location = rf"\\{server}\Staging\Staging_v{server_version}\\"
    if (not os.path.exists(server_location)):
        print(f"Staging location {server_location} does not exist, creating.....")
        os.mkdir(server_location)

cc_build_area = rf"\\gsm1900.org\dfsroot\as\samson\citrix_dev\cconline_perforce\vsp{cc_version}\vsp\\"
cc_build_directories = ["bin32_storage", "DosView", "GN"]

try:
    print(f"Checking the source location at {cc_build_area}")
    if (os.path.exists(cc_build_area)):
        for server in server_list_2019:
            server_location = rf"\\{server}\Staging\Staging_v{server_version}\\"
            shutil.copytree(cc_build_area, server_location)
    else:
        print("Not able to read from the source location")
except:
    print(f"The Build are you specified is invalid: {cc_build_area}")

time.sleep(20)