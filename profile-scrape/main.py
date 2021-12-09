'''
Created on 

Course work: 

@author: Harini

Source:
    
'''

# Import necessary modules
import instaloader
from instaloader import Profile, Post
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get('ACC')
PASSWORD = os.environ.get('PASSWORD')

def download():

    instance = instaloader.Instaloader()

    instance.login(USER,PASSWORD)

    instance.download_profile(profile_name= "j.m")


def startpy():
    download()


if __name__ == '__main__':
    startpy()