"""
ST/SST Automation for SecureZone Migration
Randy Bitts, Amdocs SA, RAB Consulting
Coding Started 05/06/2024
"""

import os
import sys
import shutil
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

