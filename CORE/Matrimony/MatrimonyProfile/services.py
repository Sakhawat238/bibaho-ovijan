import re
from django.shortcuts import render, redirect, get_object_or_404
from CORE.utils import getCommonResponse, getCommonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from bibahoovijan import settings
from AUTH.UserAuthentication.models import User, USER_TYPE

